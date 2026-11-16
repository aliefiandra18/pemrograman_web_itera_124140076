"""Modul library_item.

Berisi abstract class ``LibraryItem`` beserta dua turunannya, ``Book`` dan
``Magazine``, yang dipakai oleh sistem manajemen perpustakaan.
"""

from abc import ABC, abstractmethod


def format_rupiah(nominal: float) -> str:
    """Mengubah angka menjadi format rupiah, contoh: 12000 -> 'Rp 12.000'."""
    return "Rp " + f"{nominal:,.0f}".replace(",", ".")


class LibraryItem(ABC):
    """Abstract class untuk seluruh koleksi perpustakaan (buku, majalah, dst.).

    Attributes:
        item_id: Kode unik item.
        judul: Judul item.
        tahun_terbit: Tahun terbit item.
    """

    def __init__(
        self, item_id: str, judul: str, tahun_terbit: int, kategori: str
    ):
        self.item_id = item_id
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self._kategori = kategori      # protected
        self.__is_dipinjam = False     # private

    # ------------------------------------------------------------------
    # Property & pengelolaan status peminjaman
    # ------------------------------------------------------------------
    @property
    def is_dipinjam(self) -> bool:
        """Status peminjaman (read-only dari luar class)."""
        return self.__is_dipinjam

    @property
    def kategori(self) -> str:
        """Kategori item (mengakses atribut protected ``_kategori``)."""
        return self._kategori

    @property
    def status(self) -> str:
        """Teks status: 'Dipinjam' atau 'Tersedia'."""
        return "Dipinjam" if self.__is_dipinjam else "Tersedia"

    def pinjam(self) -> bool:
        """Menandai item sebagai dipinjam.

        Returns:
            True jika berhasil, False jika item sedang dipinjam.
        """
        if self.__is_dipinjam:
            return False
        self.__is_dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Menandai item sebagai sudah dikembalikan.

        Returns:
            True jika berhasil, False jika item memang tidak sedang dipinjam.
        """
        if not self.__is_dipinjam:
            return False
        self.__is_dipinjam = False
        return True

    # ------------------------------------------------------------------
    # Kontrak yang wajib diimplementasikan subclass
    # ------------------------------------------------------------------
    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan dalam rupiah."""

    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail lengkap item dalam bentuk teks."""

    # ------------------------------------------------------------------
    # Utilitas untuk subclass
    # ------------------------------------------------------------------
    @staticmethod
    def _validasi_hari(hari_terlambat: int) -> int:
        """Memastikan jumlah hari terlambat berupa bilangan bulat >= 0."""
        if (
            not isinstance(hari_terlambat, int)
            or isinstance(hari_terlambat, bool)
            or hari_terlambat < 0
        ):
            raise ValueError("hari_terlambat harus berupa bilangan bulat >= 0")
        return hari_terlambat

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}"
            f"(item_id={self.item_id!r}, judul={self.judul!r})"
        )


class Book(LibraryItem):
    """Buku perpustakaan dengan denda Rp 2.000 per hari keterlambatan."""

    TARIF_DENDA_PER_HARI = 2_000

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        penulis: str,
        jumlah_halaman: int,
        genre: str,
    ):
        super().__init__(item_id, judul, tahun_terbit, kategori="Buku")
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman
        self.genre = genre

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Denda buku: Rp 2.000 x hari terlambat."""
        hari = self._validasi_hari(hari_terlambat)
        return float(hari * self.TARIF_DENDA_PER_HARI)

    def get_detail(self) -> str:
        return (
            f"[{self.item_id}] {self.judul}\n"
            f"  Kategori : {self.kategori}\n"
            f"  Penulis  : {self.penulis}\n"
            f"  Terbit   : {self.tahun_terbit}\n"
            f"  Halaman  : {self.jumlah_halaman}\n"
            f"  Genre    : {self.genre}\n"
            f"  Denda    : {format_rupiah(self.TARIF_DENDA_PER_HARI)}/hari\n"
            f"  Status   : {self.status}"
        )

    def __str__(self) -> str:
        return (
            f"[{self.item_id}] Buku    | {self.judul} - {self.penulis} "
            f"({self.tahun_terbit}) | {self.genre} | "
            f"{self.jumlah_halaman} hlm | {self.status}"
        )


class Magazine(LibraryItem):
    """Majalah perpustakaan dengan denda Rp 1.000 per hari keterlambatan."""

    TARIF_DENDA_PER_HARI = 1_000

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        edisi: int,
        bulan_terbit: str,
    ):
        super().__init__(item_id, judul, tahun_terbit, kategori="Majalah")
        self.edisi = edisi
        self.bulan_terbit = bulan_terbit

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Denda majalah: Rp 1.000 x hari terlambat."""
        hari = self._validasi_hari(hari_terlambat)
        return float(hari * self.TARIF_DENDA_PER_HARI)

    def get_detail(self) -> str:
        return (
            f"[{self.item_id}] {self.judul}\n"
            f"  Kategori : {self.kategori}\n"
            f"  Edisi    : {self.edisi}\n"
            f"  Terbit   : {self.bulan_terbit} {self.tahun_terbit}\n"
            f"  Denda    : {format_rupiah(self.TARIF_DENDA_PER_HARI)}/hari\n"
            f"  Status   : {self.status}"
        )

    def __str__(self) -> str:
        return (
            f"[{self.item_id}] Majalah | {self.judul} - Edisi {self.edisi} "
            f"({self.bulan_terbit} {self.tahun_terbit}) | {self.status}"
        )
