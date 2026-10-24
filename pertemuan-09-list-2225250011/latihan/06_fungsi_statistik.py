"""Membuat fungsi untuk menghitung rata-rata nilai."""


def rata_rata(data):
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]
hasil_mean = rata_rata(nilai)

print(f"Rata-rata = {hasil_mean:.2f}")
