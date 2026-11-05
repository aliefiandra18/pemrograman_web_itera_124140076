"""Program utama untuk menguji seluruh fungsi pada modul math_operations."""

# Cara impor 1: mengimpor seluruh modul (dipanggil dengan awalan modul)
import math_operations

# Cara impor 2: mengimpor fungsi dan konstanta tertentu secara langsung
from math_operations import (
    PI,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
    keliling_lingkaran,
    luas_lingkaran,
)

LEBAR_GARIS = 60


def cetak_judul(judul: str) -> None:
    """Mencetak judul bagian dengan garis pemisah.

    Parameter:
        judul (str): Teks judul yang akan dicetak.

    Return:
        None
    """
    print("\n" + "=" * LEBAR_GARIS)
    print(judul.center(LEBAR_GARIS))
    print("=" * LEBAR_GARIS)


def uji_persegi() -> None:
    """Menguji fungsi luas dan keliling persegi dengan beberapa nilai."""
    cetak_judul("PERSEGI")
    for sisi in [4, 7.5, 12]:
        luas = math_operations.luas_persegi(sisi)
        keliling = math_operations.keliling_persegi(sisi)
        print(
            f"Sisi {sisi:>5} | Luas: {luas:>8.2f} | "
            f"Keliling: {keliling:>7.2f}"
        )


def uji_persegi_panjang() -> None:
    """Menguji fungsi luas dan keliling persegi panjang."""
    cetak_judul("PERSEGI PANJANG")
    for panjang, lebar in [(10, 5), (8.5, 3.2), (20, 15)]:
        luas = math_operations.luas_persegi_panjang(panjang, lebar)
        keliling = math_operations.keliling_persegi_panjang(panjang, lebar)
        print(
            f"P {panjang:>5} x L {lebar:>5} | Luas: {luas:>8.2f} | "
            f"Keliling: {keliling:>7.2f}"
        )


def uji_lingkaran() -> None:
    """Menguji fungsi luas dan keliling lingkaran (impor langsung)."""
    cetak_judul(f"LINGKARAN (PI = {PI})")
    for jari_jari in [3, 7, 10.5]:
        luas = luas_lingkaran(jari_jari)
        keliling = keliling_lingkaran(jari_jari)
        print(
            f"r {jari_jari:>5} | Luas: {luas:>8.2f} | "
            f"Keliling: {keliling:>7.2f}"
        )


def uji_konversi_suhu() -> None:
    """Menguji fungsi konversi suhu Celsius ke Fahrenheit dan Kelvin."""
    cetak_judul("KONVERSI SUHU")
    print(f"{'Celsius':>10}{'Fahrenheit':>15}{'Kelvin':>12}")
    print("-" * LEBAR_GARIS)
    for celsius in [-40, 0, 25, 36.6, 100]:
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>10.2f}{fahrenheit:>15.2f}{kelvin:>12.2f}")


def main() -> None:
    """Menjalankan seluruh pengujian fungsi pada modul math_operations."""
    print("PENGUJIAN MODUL math_operations")
    uji_persegi()
    uji_persegi_panjang()
    uji_lingkaran()
    uji_konversi_suhu()


if __name__ == "__main__":
    main()
