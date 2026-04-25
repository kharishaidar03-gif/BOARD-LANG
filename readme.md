# 🎲 Board-lang (v1.0)

**Board-lang** adalah bahasa pemrograman *open-source* sederhana yang dirancang khusus untuk membuat logika **Board Game** (permainan papan) tanpa harus pusing dengan bahasa pemrograman yang rumit.

Bahasa ini dibuat untuk dijalankan di **Termux** (Android) dengan tujuan memudahkan pengembang game pemula merancang mekanisme permainan mereka sendiri.

---

## 💡 Filosofi Board-lang
"Game adalah aturan. Aturan adalah kode."
Board-lang diciptakan agar siapapun bisa menuliskan aturan main seolah-olah sedang berbicara dengan teman. Kamu tidak perlu belajar `class` atau `function` yang berat, cukup gunakan perintah **BUAT**, **tulis**, dan **acak**.

---

## 🛠️ Panduan Perintah (Sintaks)

Berikut adalah perintah dasar yang didukung oleh Board-lang saat ini:

### 1. Membuat Arena (`BUAT papan`)
Digunakan untuk mendefinisikan ukuran papan permainan.
- **Sintaks:** `BUAT papan [Lebar x Tinggi]`
- **Contoh:** `BUAT papan [8x8]` (untuk Catur)

### 2. Mendaftarkan Pemain (`BUAT pemain`)
Digunakan untuk memasukkan daftar nama pemain ke dalam sesi.
- **Sintaks:** `BUAT pemain {Nama1, Nama2, ...}`
- **Contoh:** `BUAT pemain {Merah, Biru, Kuning}`

### 3. Menampilkan Pesan (`tulis`)
Digunakan untuk mencetak teks atau instruksi ke layar terminal.
- **Sintaks:** `tulis [Pesan Kamu]`
- **Contoh:** `tulis Giliran pemain Merah!`

### 4. Elemen Keberuntungan (`acak`)
Digunakan untuk simulasi acak seperti melempar dadu.
- **Sintaks:** `acak dadu`
- **Output:** Menghasilkan angka acak 1 sampai 6.

---

## 🚀 Cara Instalasi di Termux

1. Pastikan folder `BOARDLANG` sudah ada di penyimpanan kamu.
2. Buka Termux dan arahkan ke folder tersebut:
   ```bash
   cd /sdcard/BOARDLANG
