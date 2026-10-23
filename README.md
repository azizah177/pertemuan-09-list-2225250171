
# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Nurul Azizah  
**NIM:** 2225250171  
**Kelas:** ...

## Tujuan

Mengolah kumpulan data numerik dengan list Python, memahami penggunaan indeks dan slicing, melakukan manipulasi list, menghitung statistik sederhana, serta menyaring data berdasarkan kondisi tertentu.

## Struktur Program

Program terdiri dari folder `latihan` dan `praktik`.

Folder `latihan` berisi enam program sebagai berikut.

1. `01_buat_list.py` untuk membuat list dan menghitung banyak data.
2. `02_indeks_slicing.py` untuk mengakses elemen list menggunakan indeks dan slicing.
3. `03_manipulasi_list.py` untuk mengubah, menambah, dan menghapus elemen list.
4. `04_agregasi_nilai.py` untuk menghitung total, rata-rata, nilai minimum, dan maksimum.
5. `05_filter_kelulusan.py` untuk menyaring nilai mahasiswa yang memenuhi batas kelulusan.
6. `06_fungsi_statistik.py` untuk menghitung rata-rata menggunakan fungsi.

Folder `praktik` berisi file `analisis_nilai_mahasiswa.py`. Program ini digunakan untuk menganalisis sekumpulan nilai mahasiswa, menghitung statistik nilai, menentukan nilai yang lulus, serta menghitung jumlah mahasiswa yang lulus dan belum lulus berdasarkan batas kelulusan 60.

Struktur folder program:

```text
pertemuan-09-list-2225250171/
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

## Cara Menjalankan

Program dijalankan melalui terminal dari folder utama repository menggunakan Python.

Untuk menjalankan program praktik, gunakan perintah:

```bash
py praktik/analisis_nilai_mahasiswa.py
```

Untuk menjalankan program latihan, gunakan perintah berikut sesuai file yang ingin dijalankan:

```bash
py latihan/01_buat_list.py
py latihan/02_indeks_slicing.py
py latihan/03_manipulasi_list.py
py latihan/04_agregasi_nilai.py
py latihan/05_filter_kelulusan.py
py latihan/06_fungsi_statistik.py
```

## Test Case

| Data | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| `[60, 70, 80]` | Rata-rata `70.00` | 70.00 | Berhasil |
| `[60, 70, 80]` | Minimum `60` dan maksimum `80` | Minimum 60 dan maksimum 80 | Berhasil |
| `[60, 70, 80]` | Jumlah lulus `3` | 3 mahasiswa lulus | Berhasil |
| `[59, 60, 61]` | Jumlah lulus `2` | 2 mahasiswa lulus | Berhasil |
| `[]` | Fungsi rata-rata tidak error | Mengembalikan nilai `0` | Berhasil |

## Refleksi

Hal yang dipahami dari latihan ini adalah list Python dapat digunakan untuk menyimpan banyak data dalam satu variabel. Setiap elemen list dapat diakses menggunakan indeks yang dimulai dari `0`. Selain itu, list dapat dimanipulasi dengan menambah, mengubah, dan menghapus elemen, serta digunakan untuk menghitung statistik sederhana.

Kesalahan yang berhasil diperbaiki adalah memastikan fungsi rata-rata dapat menangani list kosong. Jika list kosong langsung dibagi dengan jumlah datanya, program dapat mengalami kesalahan pembagian dengan nol. Oleh karena itu, fungsi `rata_rata()` diperiksa terlebih dahulu menggunakan `if len(data) == 0` agar mengembalikan nilai `0` ketika tidak ada data.
