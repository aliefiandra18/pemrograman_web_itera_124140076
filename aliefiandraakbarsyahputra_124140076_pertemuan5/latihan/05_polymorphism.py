"""Latihan 5 - Polymorphism: overriding, duck typing, loop koleksi, dan operator overloading."""


class Ekspedisi:
    """Antarmuka umum layanan pengiriman barang."""

    def __init__(self, nama: str):
        self.nama = nama

    def hitung_ongkir(self, berat_kg: float) -> float:
        """Harus di-override oleh subclass."""
        raise NotImplementedError("Subclass wajib mengimplementasikan hitung_ongkir()")


class Reguler(Ekspedisi):
    """Pengiriman reguler: Rp 8.000 per kg."""

    def __init__(self):
        super().__init__("Reguler")

    def hitung_ongkir(self, berat_kg: float) -> float:
        return 8_000 * berat_kg


class Kilat(Ekspedisi):
    """Pengiriman kilat: Rp 15.000 per kg + biaya prioritas Rp 5.000."""

    def __init__(self):
        super().__init__("Kilat")

    def hitung_ongkir(self, berat_kg: float) -> float:
        return 15_000 * berat_kg + 5_000


class KurirLokal:
    """Tidak mewarisi Ekspedisi, tetapi punya hitung_ongkir() -> valid via duck typing."""

    nama = "Kurir Lokal"

    def hitung_ongkir(self, berat_kg: float) -> float:
        return 10_000  # tarif flat


def bandingkan_ongkir(daftar_layanan: list, berat_kg: float) -> None:
    """Fungsi polimorfik: tidak perlu if-elif untuk mengecek tipe layanan."""
    print(f"Ongkir untuk paket {berat_kg} kg:")
    for layanan in daftar_layanan:
        print(f"  - {layanan.nama:<12}: Rp {layanan.hitung_ongkir(berat_kg):>9,.0f}")


class Vektor:
    """Vektor 2D untuk mendemonstrasikan operator overloading."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, skalar):
        if isinstance(skalar, (int, float)):
            return Vektor(self.x * skalar, self.y * skalar)
        return NotImplemented

    def __eq__(self, other):
        return isinstance(other, Vektor) and (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        if isinstance(other, Vektor):
            return self.panjang() > other.panjang()
        return NotImplemented

    def panjang(self) -> float:
        """Panjang (magnitudo) vektor."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self) -> str:
        return f"Vektor({self.x}, {self.y})"


if __name__ == "__main__":
    layanan = [Reguler(), Kilat(), KurirLokal()]
    bandingkan_ongkir(layanan, 2.5)

    print("\n--- Operator overloading ---")
    a, b = Vektor(3, 4), Vektor(1, 2)
    print("a       :", a)
    print("b       :", b)
    print("a + b   :", a + b)
    print("a * 2   :", a * 2)
    print("a == b  :", a == b)
    print("a > b   :", a > b)
