"""Latihan 2 - Class & Object: atribut class, atribut instance, dan dunder method."""


class Mahasiswa:
    """Merepresentasikan mahasiswa Teknik Informatika ITERA."""

    # Atribut class (dipakai bersama oleh semua objek)
    universitas = "Institut Teknologi Sumatera"
    jumlah_objek = 0

    def __init__(self, nama: str, nim: str, ipk: float = 0.0):
        # Atribut instance (unik untuk setiap objek)
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
        self.matkul = []
        Mahasiswa.jumlah_objek += 1

    def ambil_matkul(self, nama_matkul: str) -> None:
        """Menambahkan mata kuliah ke daftar mata kuliah mahasiswa."""
        self.matkul.append(nama_matkul)
        print(f"[{self.nama}] mengambil {nama_matkul}")

    def predikat(self) -> str:
        """Mengembalikan predikat akademik berdasarkan IPK."""
        if self.ipk >= 3.5:
            return "Sangat Memuaskan"
        if self.ipk >= 3.0:
            return "Memuaskan"
        if self.ipk >= 2.0:
            return "Cukup"
        return "Perlu Bimbingan"

    def __str__(self) -> str:
        return f"{self.nama} ({self.nim}) - IPK {self.ipk:.2f} - {self.universitas}"

    def __repr__(self) -> str:
        return f"Mahasiswa(nama={self.nama!r}, nim={self.nim!r}, ipk={self.ipk})"


if __name__ == "__main__":
    print("Jumlah objek awal :", Mahasiswa.jumlah_objek)
    mhs1 = Mahasiswa("Aliefiandra Akbar Syahputra", "124140076", 3.60)
    mhs2 = Mahasiswa("Mahasiswa Contoh", "124140001", 3.10)
    print("Jumlah objek akhir:", Mahasiswa.jumlah_objek)

    mhs1.ambil_matkul("Pengembangan Aplikasi Web")
    mhs1.ambil_matkul("Basis Data")
    mhs2.ambil_matkul("Kecerdasan Buatan")
    print("\nMatkul mhs1:", mhs1.matkul)
    print("Matkul mhs2:", mhs2.matkul)

    print("\nPredikat mhs1:", mhs1.predikat())
    print("Predikat mhs2:", mhs2.predikat())

    print("\nprint(mhs1)  ->", mhs1)
    print("repr(mhs2)   ->", repr(mhs2))

    Mahasiswa.universitas = "ITERA"
    print("\nSetelah atribut class diubah:")
    print("mhs1.universitas =", mhs1.universitas)
    print("mhs2.universitas =", mhs2.universitas)
