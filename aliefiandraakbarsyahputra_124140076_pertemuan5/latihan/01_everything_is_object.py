"""Latihan 1a - Membuktikan bahwa 'everything is an object' di Python."""

angka = 7
teks = "Pemrograman Web ITERA"
daftar = [1, 2, 3]
kamus = {"kelas": "RA"}


def sapa(nama):
    """Fungsi sederhana untuk membuktikan bahwa fungsi juga merupakan objek."""
    return f"Halo, {nama}!"


print("=== 1. Setiap nilai punya class asal ===")
contoh = [
    ("angka", angka),
    ("teks", teks),
    ("daftar", daftar),
    ("kamus", kamus),
    ("sapa (fungsi)", sapa),
]
for label, nilai in contoh:
    print(f"{label:<15}: {type(nilai).__name__}")

print("\n=== 2. Objek memiliki method bawaan ===")
print("teks.lower()       :", teks.lower())
print("teks.split()       :", teks.split())
daftar.append(4)
print("daftar.append(4)   :", daftar)
print("(7).bit_length()   :", angka.bit_length())

print("\n=== 3. Fungsi adalah objek tingkat pertama ===")
alias = sapa  # fungsi dapat disimpan di variabel lain
print("alias('Alief')     :", alias("Alief"))
sapa.versi = "1.0"  # fungsi bahkan boleh memiliki atribut
print("sapa.versi         :", sapa.versi)
print("alias is sapa      :", alias is sapa)

print("\n=== 4. Semua class bermuara pada object ===")
print("isinstance(angka, object):", isinstance(angka, object))
print("isinstance(sapa, object) :", isinstance(sapa, object))
print("MRO int                  :", [c.__name__ for c in int.__mro__])
