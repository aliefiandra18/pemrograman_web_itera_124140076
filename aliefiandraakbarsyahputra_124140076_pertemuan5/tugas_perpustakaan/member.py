"""Modul member.

Berisi class ``Member`` yang merepresentasikan anggota perpustakaan.
"""

from typing import List, Optional

from library_item import LibraryItem, format_rupiah


class Member:
    """Anggota perpustakaan yang dapat meminjam dan mengembalikan item.

    Attributes:
        member_id: ID unik anggota.
        nama: Nama lengkap anggota.
    """

    def __init__(self, member_id: str, nama: str):
        self.member_id = member_id
        self.nama = nama
        self.__daftar_pinjaman: List[LibraryItem] = []  # private

    @property
    def jumlah_pinjaman(self) -> int:
        """Jumlah item yang sedang dipinjam anggota."""
        return len(self.__daftar_pinjaman)

    def pinjam_item(self, item: LibraryItem) -> bool:
        """Meminjam sebuah item.

        Args:
            item: Objek turunan LibraryItem yang akan dipinjam.

        Returns:
            True jika peminjaman berhasil, False jika gagal.
        """
        if not isinstance(item, LibraryItem):
            print("[GAGAL] Objek yang dipinjam bukan item yang valid.")
            return False

        if item in self.__daftar_pinjaman:
            print(f"[GAGAL] {self.nama} sudah meminjam '{item.judul}'.")
            return False

        if not item.pinjam():
            print(f"[GAGAL] '{item.judul}' sedang dipinjam anggota lain.")
            return False

        self.__daftar_pinjaman.append(item)
        print(f"[OK] {self.nama} berhasil meminjam '{item.judul}'.")
        return True

    def kembalikan_item(
        self, item: LibraryItem, hari_terlambat: int = 0
    ) -> Optional[float]:
        """Mengembalikan item yang dipinjam dan mencetak denda jika terlambat.

        Args:
            item: Item yang dikembalikan.
            hari_terlambat: Hari keterlambatan (default 0 = tepat waktu).

        Returns:
            Besar denda (float), atau None jika pengembalian gagal.
        """
        if item not in self.__daftar_pinjaman:
            nama_item = getattr(item, "judul", item)
            print(f"[GAGAL] {self.nama} tidak sedang meminjam '{nama_item}'.")
            return None

        try:
            denda = item.hitung_denda(hari_terlambat)  # polimorfik
        except ValueError as err:
            print(f"[GAGAL] Pengembalian '{item.judul}' dibatalkan: {err}")
            return None

        self.__daftar_pinjaman.remove(item)
        item.kembalikan()

        if denda > 0:
            print(
                f"[OK] '{item.judul}' dikembalikan {self.nama} terlambat "
                f"{hari_terlambat} hari. Denda: {format_rupiah(denda)}"
            )
        else:
            print(
                f"[OK] '{item.judul}' dikembalikan {self.nama} "
                "tepat waktu. Tanpa denda."
            )
        return denda

    def tampilkan_pinjaman(self) -> None:
        """Menampilkan seluruh item yang sedang dipinjam anggota."""
        print(f"Daftar pinjaman {self.nama} ({self.member_id}):")
        if not self.__daftar_pinjaman:
            print("  (tidak ada item yang sedang dipinjam)")
            return
        for nomor, item in enumerate(self.__daftar_pinjaman, start=1):
            print(f"  {nomor}. {item}")

    def __str__(self) -> str:
        return (
            f"Member({self.member_id}) {self.nama} "
            f"| pinjaman aktif: {self.jumlah_pinjaman}"
        )
