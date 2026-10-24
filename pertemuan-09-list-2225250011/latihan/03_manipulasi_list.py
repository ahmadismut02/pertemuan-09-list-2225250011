"""Mengubah, menambah, menyisipkan, dan menghapus elemen list."""

nilai = [75, 80, 65]
print("List awal     :", nilai)

nilai[1] = 82        # Mengubah nilai pada indeks 1
nilai.append(90)     # Menambah elemen di akhir list
nilai.insert(1, 70)  # Menyisipkan nilai 70 pada indeks 1
nilai.remove(65)     # Menghapus angka 65 dari list

print("List setelah manipulasi:", nilai)
