# Pertemuan 09: List dan Pengolahan Data Numerik

## Identitas

* **Nama:** [Nama Lengkap Anda]
* **NIM:** [NIM Anda]
* **Kelas:** [Kelas Anda]
* **Program Studi:** S1 Pendidikan Matematika FKIP Untirta

---

## Tujuan Pembelajaran

* Menyimpan dan mengolah kumpulan data numerik menggunakan list Python.
* Mengakses elemen list dengan indeks positif, negatif, dan slicing.
* Melakukan manipulasi elemen (mengubah, menambah, menyisipkan, menghapus).
* Menghitung nilai agregasi (total, rata-rata, minimum, maksimum) serta filter kelulusan.
* Mengemas proses statistik ke dalam fungsi dan mengunggah repositori ke GitHub.

---

## Struktur Repositori

```text
pertemuan-09-list-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama repositori:

```bash
# Menjalankan program praktik utama
python3 praktik/analisis_nilai_mahasiswa.py

# Menjalankan salah satu file latihan (contoh latihan 1)
python3 latihan/01_buat_list.py
```

## Hasil Pengujian

| Data Input | Uji Komponen | Hasil Ekspektasi | Hasil Aktual | Status |
| --- | --- | --- | --- | --- |
| `[60, 70, 80]` | Rata-rata | `70.00` | `70.00` | Lulus |
| `[60, 70, 80]` | Minimum / Maksimum | `60` / `80` | `60` / `80` | Lulus |
| `[60, 70, 80]` | Jumlah Lulus (>= 60) | `3` | `3` | Lulus |
| `[59, 60, 61]` | Batas Kelulusan | `2` Lulus, `1` Belum | `2` Lulus, `1` Belum | Lulus |
| `[]` | Robustness List Kosong | `0.00` (bebas ZeroDivisionError) | `0.00` | Lulus |

## Refleksi

 **Hal yang Dipahami:** List memungkinkan penyimpanan kumpulan nilai heterogen/homogen dalam satu variabel berurutan. Penggunaan indeks `0` hingga `-1` mempermudah navigasi data, dan integrasi fungsi `sum()` & `len()` mempermudah kalkulasi statistik.
 **Perbaikan Kesalahan:** Pada penanganan data kosong, pembagian rata-rata berpotensi menyebabkan `ZeroDivisionError`. Hal ini ditangani dengan menambahkan kondisi validasi `if len(data) == 0: return 0.0`.
