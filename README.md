# Aplikasi Newton-Raphson dengan Kivy (Python)

## Deskripsi Proyek  
Program ini merupakan "aplikasi GUI (Graphical User Interface)" berbasis **Python dan Kivy** untuk menghitung akar suatu persamaan menggunakan "Metode Newton-Raphson".  
Metode ini digunakan untuk mencari akar fungsi non-linear melalui pendekatan iteratif.  
Aplikasi ini dibuat sebagai bagian dari tugas "UTS Praktikum Komputasi Numerik".


## Fitur Utama  
  **Input parameter:**
- `x₀` → tebakan awal akar  
- `ε (epsilon)` → batas toleransi kesalahan  
- `n` → jumlah iterasi maksimum  

 **Output hasil iterasi dalam bentuk tabel:**
- Nomor iterasi  
- Nilai `xᵢ`  
- Nilai `f(xᵢ)`  
- Nilai turunan `f’(xᵢ)`  
- Selisih `|xᵢ₊₁ − xᵢ|`  

✅ Tampilan hasil iterasi dalam "tabel yang dapat discroll"  
✅ Pewarnaan lembut untuk antarmuka  
✅ Pesan otomatis untuk "input tidak valid" atau "turunan bernilai nol"


## Rumus yang Digunakan  
Metode Newton-Raphson didasarkan pada rumus:

\[
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
\]

Dengan fungsi yang digunakan dalam program ini:

\[
f(x) = x^4 - 5x^2 + 4
\]

\[
f'(x) = 4x^3 - 10x
\]


## Tim Pengembang 
  **Kelompok 1 UTS Praktikum Komputasi Numerik:**
  - Abdi Dzil Ikram (2408107010024)
  - Aulia Lutfi (2408107010033)
  - Annisa Rahma Fathia (2408107010027)
  - Dara Ramadhani (2408107010028)
  - Putroe Fatimah Azzahra (2408107010002)
