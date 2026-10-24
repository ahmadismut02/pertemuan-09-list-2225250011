"""Analisis statistik nilai mahasiswa dan penyaringan kelulusan."""


def rata_rata(data):
    """Menghitung rata-rata data numerik, atau 0.0 jika data kosong."""
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan nilai yang memenuhi atau melebihi batas kelulusan."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil


def analisis_utama():
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    batas_kkm = 60

    list_lulus = nilai_lulus(nilai, batas=batas_kkm)

    banyak_data = len(nilai)
    total_nilai = sum(nilai)
    mean_nilai = rata_rata(nilai)
    nilai_min = min(nilai) if nilai else 0
    nilai_max = max(nilai) if nilai else 0

    jumlah_lulus = len(list_lulus)
    jumlah_belum_lulus = banyak_data - jumlah_lulus

    print("=" * 45)
    print("      ANALISIS NILAI MAHASISWA (PY-09)      ")
    print("=" * 45)
    print(f"Data Nilai        : {nilai}")
    print(f"Banyak Data       : {banyak_data} mahasiswa")
    print("-" * 45)
    print(f"Total Nilai       : {total_nilai}")
    print(f"Rata-rata Nilai   : {mean_nilai:.2f}")
    print(f"Nilai Terendah    : {nilai_min}")
    print(f"Nilai Tertinggi   : {nilai_max}")
    print("-" * 45)
    print(f"Batas Kelulusan   : {batas_kkm}")
    print(f"Daftar Nilai Lulus: {list_lulus}")
    print(f"Jumlah Lulus      : {jumlah_lulus} mahasiswa")
    print(f"Jumlah Belum Lulus: {jumlah_belum_lulus} mahasiswa")
    print("=" * 45)


if __name__ == "__main__":
    analisis_utama()
