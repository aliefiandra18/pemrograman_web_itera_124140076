"""Driver pengujian Sistem Manajemen Perpustakaan Terpadu Berbasis OOP.

Jalankan dengan:  python main.py
"""

from library import Library
from library_item import Book, LibraryItem, Magazine, format_rupiah
from member import Member


def bagian(judul: str) -> None:
    """Mencetak pemisah antar skenario."""
    print(f"\n{'=' * 70}\n{judul}\n{'=' * 70}")


def main() -> None:
    """Menjalankan seluruh skenario operasional perpustakaan."""
    perpus = Library("Perpustakaan Teknik Informatika ITERA")

    bagian("1. PERSIAPAN KOLEKSI")
    buku1 = Book(
        "BK-001", "Dasar Pemrograman Python", 2022,
        "Budi Santoso", 320, "Teknologi",
    )
    buku2 = Book(
        "BK-002", "Algoritma dan Struktur Data", 2020,
        "Siti Rahma", 412, "Teknologi",
    )
    majalah1 = Magazine(
        "MG-001", "Sains Populer Indonesia", 2024, 125, "Maret"
    )
    majalah2 = Magazine("MG-002", "Ragam Informatika", 2024, 87, "Juni")
    for item in (buku1, buku2, majalah1, majalah2):
        perpus.tambah_item(item)
    perpus.tambah_item(buku1)  # ID duplikat -> ditolak

    bagian("2. REGISTRASI ANGGOTA")
    alief = Member("M-001", "Aliefiandra Akbar Syahputra")
    rina = Member("M-002", "Rina Anggraini")
    perpus.registrasi_member(alief)
    perpus.registrasi_member(rina)
    perpus.registrasi_member(Member("M-001", "Duplikat"))  # ID duplikat

    bagian("3. KATALOG LENGKAP")
    perpus.tampilkan_katalog()

    bagian("4. PEMINJAMAN SUKSES")
    alief.pinjam_item(buku1)
    alief.pinjam_item(majalah1)
    rina.pinjam_item(buku2)

    bagian("5. PERCOBAAN MEMINJAM ITEM YANG SUDAH DIPINJAM")
    rina.pinjam_item(buku1)     # dipinjam anggota lain
    alief.pinjam_item(buku1)    # sudah dipinjam sendiri

    bagian("6. KATALOG HANYA YANG TERSEDIA")
    perpus.tampilkan_katalog(hanya_tersedia=True)

    bagian("7. PENCARIAN ITEM")
    for kata_kunci in ("python", "MG-00", "tidak-ada"):
        hasil = perpus.cari_item(kata_kunci)
        print(f"Pencarian '{kata_kunci}': {len(hasil)} hasil")
        for item in hasil:
            print(f"  -> {item}")

    bagian("8. DETAIL ITEM (get_detail) & DAFTAR PINJAMAN")
    print(buku1.get_detail())
    print()
    print(majalah1.get_detail())
    print()
    alief.tampilkan_pinjaman()
    rina.tampilkan_pinjaman()

    bagian("9. PENGEMBALIAN TEPAT WAKTU")
    alief.kembalikan_item(majalah1)

    bagian("10. PENGEMBALIAN TERLAMBAT (DENDA POLIMORFIK)")
    alief.kembalikan_item(buku1, hari_terlambat=5)   # 5 x Rp 2.000
    rina.kembalikan_item(buku2, hari_terlambat=3)    # 3 x Rp 2.000
    dimas = Member("M-003", "Dimas Pratama")
    perpus.registrasi_member(dimas)
    dimas.pinjam_item(majalah2)
    dimas.kembalikan_item(majalah2, hari_terlambat=5)  # 5 x Rp 1.000

    print("\nDenda 7 hari untuk semua item (satu loop, tanpa cek tipe):")
    for item in (buku1, buku2, majalah1, majalah2):
        denda = format_rupiah(item.hitung_denda(7))
        print(f"  {item.item_id} ({item.kategori:<7}): {denda}")

    bagian("11. PENANGANAN KONDISI ERROR")
    alief.kembalikan_item(buku2)                     # tidak sedang dipinjam
    alief.pinjam_item(buku2)
    alief.kembalikan_item(buku2, hari_terlambat=-2)  # hari negatif
    alief.kembalikan_item(buku2)                     # pengembalian benar
    alief.pinjam_item("bukan item")                      # tipe salah

    print("\nUji enkapsulasi & abstract class:")
    try:
        print(buku1.__is_dipinjam)
    except AttributeError as err:
        print(f"  Akses atribut private ditolak (AttributeError): {err}")
    try:
        LibraryItem("X-001", "Tidak Boleh", 2024, "Umum")
    except TypeError as err:
        print(f"  Instansiasi abstract class ditolak (TypeError): {err}")

    bagian("12. KATALOG AKHIR")
    perpus.tampilkan_katalog()
    print(
        f"\nTotal item: {perpus.jumlah_item} | "
        f"Total anggota: {perpus.jumlah_member}"
    )


if __name__ == "__main__":
    main()
