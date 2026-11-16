"""Latihan 6 - Abstract Class & Interface menggunakan modul abc."""

from abc import ABC, abstractmethod


class Karyawan(ABC):
    """Abstract class: kontrak yang harus dipenuhi semua jenis karyawan."""

    def __init__(self, nama: str):
        self.nama = nama

    @property
    @abstractmethod
    def jabatan(self) -> str:
        """Abstract property: jabatan wajib ditentukan oleh subclass."""

    @abstractmethod
    def hitung_gaji(self) -> float:
        """Abstract method: cara menghitung gaji berbeda tiap jenis karyawan."""

    def cetak_slip(self) -> None:
        """Concrete method yang memanggil abstract method secara polimorfik."""
        print(f"[{self.jabatan}] {self.nama} - Gaji: Rp {self.hitung_gaji():,.0f}")


class KaryawanTetap(Karyawan):
    """Karyawan dengan gaji pokok + tunjangan."""

    def __init__(self, nama: str, gaji_pokok: float, tunjangan: float):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    @property
    def jabatan(self) -> str:
        return "Karyawan Tetap"

    def hitung_gaji(self) -> float:
        return self.gaji_pokok + self.tunjangan


class Freelancer(Karyawan):
    """Pekerja lepas yang dibayar per jam."""

    def __init__(self, nama: str, jam_kerja: int, tarif_per_jam: float):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    @property
    def jabatan(self) -> str:
        return "Freelancer"

    def hitung_gaji(self) -> float:
        return self.jam_kerja * self.tarif_per_jam


class FileStorage(ABC):
    """Interface murni: seluruh method bersifat abstract."""

    @abstractmethod
    def upload_file(self, nama_file: str, data: bytes) -> bool:
        """Menyimpan file."""

    @abstractmethod
    def download_file(self, nama_file: str) -> bytes:
        """Mengambil file yang sudah disimpan."""


class MemoryStorage(FileStorage):
    """Implementasi konkret yang menyimpan data di dalam memori (simulasi)."""

    def __init__(self):
        self.__isi = {}

    def upload_file(self, nama_file: str, data: bytes) -> bool:
        self.__isi[nama_file] = data
        print(f"[MemoryStorage] '{nama_file}' tersimpan ({len(data)} byte)")
        return True

    def download_file(self, nama_file: str) -> bytes:
        if nama_file not in self.__isi:
            raise FileNotFoundError(f"'{nama_file}' tidak ditemukan")
        return self.__isi[nama_file]


if __name__ == "__main__":
    print("--- Polimorfisme lewat abstract class ---")
    for k in [KaryawanTetap("Sari", 5_000_000, 1_000_000), Freelancer("Dimas", 40, 75_000)]:
        k.cetak_slip()

    print("\n--- Enforcement oleh Python ---")
    try:
        Karyawan("Tidak Boleh")
    except TypeError as err:
        print("Instansiasi abstract class ditolak:", err)

    class KaryawanCacat(Karyawan):
        """Sengaja lupa mengimplementasikan hitung_gaji()."""

        @property
        def jabatan(self) -> str:
            return "Cacat"

    try:
        KaryawanCacat("Lupa Override")
    except TypeError as err:
        print("Subclass tidak lengkap ditolak:", err)

    print("\n--- Interface FileStorage ---")
    storage = MemoryStorage()
    storage.upload_file("catatan.txt", b"Praktikum OOP Python")
    print("Isi file:", storage.download_file("catatan.txt").decode())
    try:
        storage.download_file("tidak_ada.txt")
    except FileNotFoundError as err:
        print("FileNotFoundError:", err)
