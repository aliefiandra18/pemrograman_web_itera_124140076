"""Tugas 2: Program Pengelolaan Data Nilai Mahasiswa.

Program menghitung nilai akhir dan grade tiap mahasiswa, menampilkannya
dalam bentuk tabel, lalu mencari mahasiswa dengan nilai akhir tertinggi
dan terendah.
"""

# Bobot persentase komponen nilai
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

# List berisi dictionary data mahasiswa
DATA_MAHASISWA = [
    {
        "nama": "Budi Santoso",
        "nim": "124140001",
        "nilai_uts": 78,
        "nilai_uas": 85,
        "nilai_tugas": 90,
    },
    {
        "nama": "Siti Aminah",
        "nim": "124140002",
        "nilai_uts": 92,
        "nilai_uas": 88,
        "nilai_tugas": 95,
    },
    {
        "nama": "Andi Pratama",
        "nim": "124140003",
        "nilai_uts": 65,
        "nilai_uas": 70,
        "nilai_tugas": 72,
    },
    {
        "nama": "Dewi Lestari",
        "nim": "124140004",
        "nilai_uts": 55,
        "nilai_uas": 60,
        "nilai_tugas": 58,
    },
    {
        "nama": "Rian Hidayat",
        "nim": "124140005",
        "nilai_uts": 40,
        "nilai_uas": 45,
        "nilai_tugas": 50,
    },
    {
        "nama": "Eko Prasetyo",
        "nim": "124140006",
        "nilai_uts": 82,
        "nilai_uas": 75,
        "nilai_tugas": 80,
    },
    {
        "nama": "Maya Putri",
        "nim": "124140007",
        "nilai_uts": 70,
        "nilai_uas": 68,
        "nilai_tugas": 74,
    },
]


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir berdasarkan bobot UTS, UAS, dan Tugas.

    Rumus: (30% * UTS) + (40% * UAS) + (30% * Tugas)

    Parameter:
        uts (float): Nilai Ujian Tengah Semester.
        uas (float): Nilai Ujian Akhir Semester.
        tugas (float): Nilai tugas.

    Return:
        float: Nilai akhir hasil pembobotan.
    """
    return (BOBOT_UTS * uts) + (BOBOT_UAS * uas) + (BOBOT_TUGAS * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade huruf berdasarkan nilai akhir.

    Parameter:
        nilai_akhir (float): Nilai akhir mahasiswa.

    Return:
        str: Grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def proses_data(daftar_mahasiswa: list) -> list:
    """Menambahkan nilai akhir dan grade ke setiap data mahasiswa.

    Parameter:
        daftar_mahasiswa (list): List dictionary data mahasiswa.

    Return:
        list: List dictionary baru yang sudah memiliki kunci
            'nilai_akhir' dan 'grade'.
    """
    hasil = []
    for mhs in daftar_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(
            mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
        )
        data_baru = dict(mhs)
        data_baru["nilai_akhir"] = nilai_akhir
        data_baru["grade"] = tentukan_grade(nilai_akhir)
        hasil.append(data_baru)
    return hasil


def cetak_tabel(daftar_mahasiswa: list) -> None:
    """Mencetak data mahasiswa dalam format tabel yang rapi.

    Parameter:
        daftar_mahasiswa (list): List dictionary mahasiswa yang sudah
            memiliki kunci 'nilai_akhir' dan 'grade'.

    Return:
        None
    """
    garis = "=" * 78
    print(garis)
    print(
        f"{'No':<4}{'Nama':<20}{'NIM':<12}{'UTS':>6}{'UAS':>6}"
        f"{'Tugas':>8}{'Nilai Akhir':>14}{'Grade':>8}"
    )
    print(garis)
    for nomor, mhs in enumerate(daftar_mahasiswa, start=1):
        print(
            f"{nomor:<4}{mhs['nama']:<20}{mhs['nim']:<12}"
            f"{mhs['nilai_uts']:>6}{mhs['nilai_uas']:>6}"
            f"{mhs['nilai_tugas']:>8}{mhs['nilai_akhir']:>14.2f}"
            f"{mhs['grade']:>8}"
        )
    print(garis)


def cari_tertinggi_terendah(daftar_mahasiswa: list) -> tuple:
    """Mencari mahasiswa dengan nilai akhir tertinggi dan terendah.

    Parameter:
        daftar_mahasiswa (list): List dictionary mahasiswa yang sudah
            memiliki kunci 'nilai_akhir'.

    Return:
        tuple: (dictionary mahasiswa tertinggi, dictionary terendah).
    """
    tertinggi = max(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])
    return tertinggi, terendah


def cetak_info_mahasiswa(judul: str, mhs: dict) -> None:
    """Mencetak informasi ringkas seorang mahasiswa.

    Parameter:
        judul (str): Judul blok informasi yang ditampilkan.
        mhs (dict): Dictionary data mahasiswa lengkap dengan nilai akhir.

    Return:
        None
    """
    print(f"\n{judul}")
    print(f"  Nama        : {mhs['nama']}")
    print(f"  NIM         : {mhs['nim']}")
    print(f"  Nilai Akhir : {mhs['nilai_akhir']:.2f}")
    print(f"  Grade       : {mhs['grade']}")


def main() -> None:
    """Menjalankan alur program pengelolaan nilai mahasiswa."""
    print("DAFTAR NILAI MAHASISWA")
    daftar = proses_data(DATA_MAHASISWA)
    cetak_tabel(daftar)

    tertinggi, terendah = cari_tertinggi_terendah(daftar)
    cetak_info_mahasiswa("Mahasiswa dengan nilai akhir TERTINGGI:", tertinggi)
    cetak_info_mahasiswa("Mahasiswa dengan nilai akhir TERENDAH:", terendah)


if __name__ == "__main__":
    main()
