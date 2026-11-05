"""Tugas 1: Program Penghitung BMI (Body Mass Index) sederhana.

Program meminta berat badan (kg) dan tinggi badan (m), menghitung BMI,
lalu menampilkan nilai BMI beserta kategori status berat badannya.
"""


def minta_angka(pesan: str, minimum: float, maksimum: float) -> float:
    """Meminta input angka dari pengguna sampai nilainya valid.

    Parameter:
        pesan (str): Teks prompt yang ditampilkan ke pengguna.
        minimum (float): Batas bawah nilai yang diterima (eksklusif).
        maksimum (float): Batas atas nilai yang diterima (inklusif).

    Return:
        float: Angka valid yang dimasukkan pengguna.
    """
    while True:
        teks = input(pesan).strip().replace(",", ".")
        try:
            nilai = float(teks)
        except ValueError:
            print("  Input tidak valid. Contoh: 65 atau 1.70")
            continue

        if minimum < nilai <= maksimum:
            return nilai
        print(f"  Masukkan nilai di atas {minimum} sampai {maksimum}.")


def hitung_bmi(berat: float, tinggi: float) -> float:
    """Menghitung nilai BMI dengan rumus berat / (tinggi * tinggi).

    Parameter:
        berat (float): Berat badan dalam kilogram (kg).
        tinggi (float): Tinggi badan dalam meter (m).

    Return:
        float: Nilai BMI hasil perhitungan.
    """
    return berat / (tinggi * tinggi)


def kategori_bmi(bmi: float) -> str:
    """Menentukan kategori status berat badan berdasarkan nilai BMI.

    Parameter:
        bmi (float): Nilai BMI yang akan dikategorikan.

    Return:
        str: Kategori berat badan (kurang, normal, berlebih, atau obesitas).
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main() -> None:
    """Menjalankan alur program: input, hitung BMI, lalu cetak hasil."""
    print("=== PROGRAM PENGHITUNG BMI ===")
    berat = minta_angka("Masukkan berat badan (kg) : ", 0, 500)
    tinggi = minta_angka("Masukkan tinggi badan (m) : ", 0, 2.8)

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Berat badan  : {berat:.1f} kg")
    print(f"Tinggi badan : {tinggi:.2f} m")
    print(f"Nilai BMI    : {bmi:.2f}")
    print(f"Kategori     : {kategori}")


if __name__ == "__main__":
    main()
