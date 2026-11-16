"""Latihan 1b - Perbandingan pendekatan prosedural dan OOP (studi kasus: stok produk)."""

# ---------------------------------------------------------------------------
# PENDEKATAN 1: PROSEDURAL (data dan fungsi terpisah)
# ---------------------------------------------------------------------------
produk_proc = {"nama": "Buku Tulis", "stok": 10, "harga": 5000}


def jual_prosedural(produk, jumlah):
    """Mengurangi stok dan mengembalikan total harga penjualan."""
    if jumlah <= 0 or jumlah > produk["stok"]:
        print("[Prosedural] Penjualan gagal: jumlah tidak valid / stok kurang.")
        return 0
    produk["stok"] -= jumlah
    return jumlah * produk["harga"]


print("=== Pendekatan Prosedural ===")
print("Total:", jual_prosedural(produk_proc, 3), "| Sisa stok:", produk_proc["stok"])
produk_proc["stok"] = -99  # siapa pun bisa merusak data tanpa validasi
print("Stok setelah dimanipulasi langsung:", produk_proc["stok"])


# ---------------------------------------------------------------------------
# PENDEKATAN 2: OOP (data dan perilaku menyatu dalam class)
# ---------------------------------------------------------------------------
class Produk:
    """Representasi produk toko beserta perilaku penjualannya."""

    def __init__(self, nama: str, stok: int, harga: int):
        self.nama = nama
        self.stok = stok
        self.harga = harga

    def jual(self, jumlah: int) -> int:
        """Mengurangi stok dan mengembalikan total harga penjualan."""
        if jumlah <= 0 or jumlah > self.stok:
            print(f"[OOP] Penjualan {self.nama} gagal: jumlah tidak valid / stok kurang.")
            return 0
        self.stok -= jumlah
        return jumlah * self.harga

    def __str__(self) -> str:
        return f"{self.nama} | stok: {self.stok} | harga: Rp {self.harga:,}"


print("\n=== Pendekatan OOP ===")
pensil = Produk("Pensil 2B", 20, 2500)
print(pensil)
print("Total:", pensil.jual(4))
pensil.jual(100)  # ditolak oleh logika di dalam class
print(pensil)
# Catatan: atribut masih public, perlindungan penuh dibahas di latihan 04 (encapsulation).
