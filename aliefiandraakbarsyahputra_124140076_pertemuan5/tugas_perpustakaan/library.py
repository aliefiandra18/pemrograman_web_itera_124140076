"""Modul library.

Berisi class ``Library`` sebagai pusat pengelolaan koleksi dan anggota.
"""

from typing import List

from library_item import LibraryItem
from member import Member


class Library:
    """Pusat pengelolaan perpustakaan (katalog item dan registrasi anggota).

    Attributes:
        nama_perpustakaan: Nama perpustakaan.
    """

    def __init__(self, nama_perpustakaan: str):
        self.nama_perpustakaan = nama_perpustakaan
        self.__koleksi_item: List[LibraryItem] = []   # private
        self.__daftar_member: List[Member] = []       # private

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan buku/majalah ke katalog.

        Returns:
            True jika berhasil, False jika tipe tidak valid atau ID
            sudah terdaftar.
        """
        if not isinstance(item, LibraryItem):
            print("[GAGAL] Hanya Book/Magazine yang dapat ditambahkan.")
            return False
        if any(k.item_id == item.item_id for k in self.__koleksi_item):
            print(f"[GAGAL] Item ID {item.item_id} sudah ada di katalog.")
            return False
        self.__koleksi_item.append(item)
        print(f"[OK] Item '{item.judul}' ({item.item_id}) masuk katalog.")
        return True

    def registrasi_member(self, member: Member) -> bool:
        """Mendaftarkan anggota baru.

        Returns:
            True jika berhasil, False jika tipe tidak valid atau ID
            sudah terdaftar.
        """
        if not isinstance(member, Member):
            print("[GAGAL] Objek yang didaftarkan bukan Member.")
            return False
        if any(m.member_id == member.member_id for m in self.__daftar_member):
            print(f"[GAGAL] Member ID {member.member_id} sudah terdaftar.")
            return False
        self.__daftar_member.append(member)
        print(f"[OK] Anggota '{member.nama}' ({member.member_id}) terdaftar.")
        return True

    def cari_item(self, keyword: str) -> List[LibraryItem]:
        """Mencari item berdasarkan potongan judul atau ID.

        Pencarian tidak peka huruf besar/kecil.

        Returns:
            List item yang cocok (kosong jika tidak ada atau keyword kosong).
        """
        kata_kunci = keyword.strip().lower()
        if not kata_kunci:
            return []
        return [
            item
            for item in self.__koleksi_item
            if kata_kunci in item.judul.lower()
            or kata_kunci in item.item_id.lower()
        ]

    def tampilkan_katalog(self, hanya_tersedia: bool = False) -> None:
        """Menampilkan katalog lengkap atau hanya item yang siap dipinjam."""
        judul = "KATALOG TERSEDIA" if hanya_tersedia else "KATALOG LENGKAP"
        print(f"=== {judul} - {self.nama_perpustakaan} ===")
        daftar = [
            item for item in self.__koleksi_item
            if not (hanya_tersedia and item.is_dipinjam)
        ]
        if not daftar:
            print("  (tidak ada item)")
            return
        for nomor, item in enumerate(daftar, start=1):
            print(f"  {nomor}. {item}")  # polimorfik: __str__ Book/Magazine
        print(f"  Total: {len(daftar)} item")

    @property
    def jumlah_item(self) -> int:
        """Jumlah seluruh item di katalog."""
        return len(self.__koleksi_item)

    @property
    def jumlah_member(self) -> int:
        """Jumlah anggota terdaftar."""
        return len(self.__daftar_member)
