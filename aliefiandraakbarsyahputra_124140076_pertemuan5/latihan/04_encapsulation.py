"""Latihan 4 - Encapsulation: public, protected, private, name mangling, dan @property."""


class Tabungan:
    """Rekening tabungan sederhana dengan data yang terlindungi."""

    def __init__(self, nomor: str, pemilik: str, saldo_awal: float, pin: str):
        self.nomor = nomor              # public
        self._pemilik = pemilik         # protected (konvensi)
        self.__saldo = max(0.0, float(saldo_awal))  # private
        self.__pin = str(pin)           # private
        self.__batas_tarik = 1_000_000.0
        self._riwayat = []

    # --- Property read-only ---------------------------------------------
    @property
    def saldo(self) -> float:
        """Getter saldo (tanpa setter, sehingga tidak bisa diubah langsung)."""
        return self.__saldo

    # --- Property dengan getter + setter + validasi ---------------------
    @property
    def batas_tarik(self) -> float:
        """Batas maksimal penarikan per transaksi."""
        return self.__batas_tarik

    @batas_tarik.setter
    def batas_tarik(self, nilai: float) -> None:
        if not isinstance(nilai, (int, float)):
            raise TypeError("Batas tarik harus berupa angka!")
        if nilai <= 0:
            raise ValueError("Batas tarik harus lebih besar dari 0!")
        self.__batas_tarik = float(nilai)

    # --- Perilaku bisnis ------------------------------------------------
    def setor(self, nominal: float) -> bool:
        """Menambah saldo jika nominal valid."""
        if nominal <= 0:
            print("Gagal: nominal setor harus > 0")
            return False
        self.__saldo += nominal
        self._riwayat.append(f"Setor +{nominal:,.0f}")
        print(f"Setor Rp {nominal:,.0f} berhasil. Saldo: Rp {self.__saldo:,.0f}")
        return True

    def tarik(self, nominal: float, pin: str) -> bool:
        """Mengurangi saldo jika PIN benar dan seluruh syarat terpenuhi."""
        if pin != self.__pin:
            print("Gagal: PIN salah")
            return False
        if nominal <= 0 or nominal > self.__batas_tarik:
            print("Gagal: nominal tidak valid / melebihi batas tarik")
            return False
        if nominal > self.__saldo:
            print("Gagal: saldo tidak cukup")
            return False
        self.__saldo -= nominal
        self._riwayat.append(f"Tarik -{nominal:,.0f}")
        print(f"Tarik Rp {nominal:,.0f} berhasil. Saldo: Rp {self.__saldo:,.0f}")
        return True


if __name__ == "__main__":
    rek = Tabungan("001-124-076", "Aliefiandra", 500_000, "246810")

    print("Nomor (public)    :", rek.nomor)
    print("Pemilik (protected):", rek._pemilik)
    print("Saldo (@property) : Rp", rek.saldo)

    rek.setor(250_000)
    rek.tarik(100_000, "000000")   # PIN salah
    rek.tarik(100_000, "246810")   # sukses
    rek.tarik(5_000_000, "246810") # melebihi batas

    print("\n--- Setter dengan validasi ---")
    rek.batas_tarik = 2_000_000
    print("Batas tarik baru:", rek.batas_tarik)
    try:
        rek.batas_tarik = -1
    except ValueError as err:
        print("ValueError:", err)

    print("\n--- Saldo bersifat read-only ---")
    try:
        rek.saldo = 999_999_999
    except AttributeError as err:
        print("AttributeError:", err)

    print("\n--- Name mangling ---")
    try:
        print(rek.__saldo)
    except AttributeError:
        print("rek.__saldo tidak bisa diakses langsung (AttributeError)")
    print("Via nama hasil mangling :", rek._Tabungan__saldo)
    print("Riwayat                 :", rek._riwayat)
