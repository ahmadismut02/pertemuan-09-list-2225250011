"""Menghitung total, rata-rata, minimum, dan maksimum dari list."""

nilai = [75, 80, 65, 90, 88]

total = sum(nilai)
banyak = len(nilai)
rata_rata = total / banyak
nilai_min = min(nilai)
nilai_max = max(nilai)

print(f"Total     = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Minimum   = {nilai_min}")
print(f"Maksimum  = {nilai_max}")
