"""Modul math_operations: kumpulan fungsi geometri dan konversi suhu."""

# Konstanta
PI = 3.14159


# ---------------------------------------------------
# Geometri: Persegi
# ---------------------------------------------------
def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Parameter:
        sisi (float): Panjang sisi persegi.

    Return:
        float: Luas persegi (sisi * sisi).
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Parameter:
        sisi (float): Panjang sisi persegi.

    Return:
        float: Keliling persegi (4 * sisi).
    """
    return 4 * sisi


# ---------------------------------------------------
# Geometri: Persegi Panjang
# ---------------------------------------------------
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Parameter:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Return:
        float: Luas persegi panjang (panjang * lebar).
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Parameter:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Return:
        float: Keliling persegi panjang (2 * (panjang + lebar)).
    """
    return 2 * (panjang + lebar)


# ---------------------------------------------------
# Geometri: Lingkaran
# ---------------------------------------------------
def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran menggunakan konstanta PI.

    Parameter:
        jari_jari (float): Jari-jari lingkaran.

    Return:
        float: Luas lingkaran (PI * jari_jari * jari_jari).
    """
    return PI * jari_jari * jari_jari


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran menggunakan konstanta PI.

    Parameter:
        jari_jari (float): Jari-jari lingkaran.

    Return:
        float: Keliling lingkaran (2 * PI * jari_jari).
    """
    return 2 * PI * jari_jari


# ---------------------------------------------------
# Konversi Temperatur
# ---------------------------------------------------
def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Parameter:
        celsius (float): Suhu dalam derajat Celsius.

    Return:
        float: Suhu dalam derajat Fahrenheit (C * 9/5 + 32).
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin.

    Parameter:
        celsius (float): Suhu dalam derajat Celsius.

    Return:
        float: Suhu dalam Kelvin (C + 273.15).
    """
    return celsius + 273.15


# Pengujian mandiri modul (tidak dijalankan saat modul di-import)
if __name__ == "__main__":
    print("[TEST MODUL] math_operations")
    print("Luas persegi sisi 5       :", luas_persegi(5))
    print("Luas lingkaran r = 7      :", luas_lingkaran(7))
    print("100 Celsius ke Fahrenheit :", celsius_ke_fahrenheit(100))
