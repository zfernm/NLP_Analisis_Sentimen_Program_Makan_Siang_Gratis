# Analisis Sentimen Program Makan Siang Gratis

## Deskripsi Projek

Projek ini merupakan bagian dari **Ujian Praktikum Machine Learning** dengan tema **Natural Language Processing (NLP)**. Fokus dari projek ini adalah melakukan analisis sentimen terhadap program makan siang gratis menggunakan data yang diambil dari Twitter/X.

### Alur Kerja Projek:
1. **Pengumpulan Dataset:**
   - Data dikumpulkan dengan cara **scraping** dari Twitter/X menggunakan API resmi.
2. **Pembersihan Data:**
   - Dataset yang telah dikumpulkan dirapikan, digabungkan, dan duplikasi dihapus.
3. **Analisis Sentimen:**
   - Proses analisis dilakukan untuk menghasilkan statistik sentimen, contoh kalimat tiap sentimen, performa model, dan representasi visual.

---

## Langkah-Langkah Implementasi

### 1. **Mendapatkan API Twitter/X**
- Masuk ke portal pengembang Twitter/X: [Twitter/X Developer Portal](https://developer.x.com/en/portal/dashboard).
- Buka **Projects & Apps > Overview**.
- Salin **Bearer Token** dari bagian **Keys and Tokens**.
- Tempelkan token tersebut ke file `scrapping.py`.

### 2. **Menginstal Dependensi**
Instal semua paket yang diperlukan dengan menjalankan perintah:
```bash
pip install -r requirements.txt
```

### 3. **Menjalankan Scraping**
Eksekusi file `scrapping.py` untuk mulai mengambil data dari Twitter/X:
```bash
python scrapping.py
```

Output dari proses ini akan tampak seperti berikut:

![program_makan_siang_gratis_1](<csv1.png>)

![program_makan_siang_gratis_2](<csv2.png>)

![program_makan_siang_gratis_3](<csv3.png>)


> **Catatan Penting:**
> - API Twitter/X memiliki batasan:
>   - Maksimal 10 permintaan setiap 15 menit.
>   - Total 100 permintaan per akun per bulan.
> - Pengumpulan data bisa memakan waktu hingga 2 jam 30 menit.

### 4. **Membersihkan Dataset**
Setelah scraping selesai, jalankan file `cleaning.py` untuk merapikan data dan menghapus duplikasi:
```bash
python cleaning.py
```
Output dari proses ini akan tampak seperti berikut:

![Output_Codingan_Cleaning](<Output_Codingan_Cleaning.png>)

### 5. **Analisis Sentimen**
Proses analisis akan menghasilkan empat output utama:
- Data statistik.
- Contoh kalimat untuk setiap sentimen.
- Analisis performa model klasifikasi sentimen.
- Representasi visual (wordcloud) dari data teks.

---

## Hasil Analisis

### 1. **Data Statistik**
Distribusi sentimen dalam dataset:

![Data_Statistik](<output_statistik.png>)

### 2. **Contoh Kalimat Tiap Sentimen**
Berikut adalah contoh kalimat untuk masing-masing kategori sentimen:

![Kalimat_Tiap_Sentimen](<Output_Kalimat_Tiap_Sentimen.png>)

### 3. **Performa Model Klasifikasi Sentimen**
Evaluasi performa model yang digunakan untuk klasifikasi:

![Output_Klasifikasi_Sentimen](<Output_Klasifikasi_Sentimen.png>)

![Output_Performa_Model](<Output_Performa_Model.png>)

### 4. **Representasi Visual (Wordcloud)**
Visualisasi wordcloud dari dataset berdasarkan kategori sentimen:

![Representasi_Visual1](<representasi visual1.png>)
![Representasi_Visual2](<representasi visual2.png>)
![Representasi_Visual3](<representasi visual3.png>)
![Representasi_Visual4](<representasi visual4.png>)
![Representasi_Visual5](<representasi visual5.png>)
![Representasi_Visual6](<representasi visual6.png>)
![Representasi_Visual7](<representasi visual7.png>)
![Representasi_Visual8](<representasi visual8.png>)
![Representasi_Visual9](<representasi visual9.png>)

---

## Google Colab
Projek ini juga dapat diakses melalui Google Colab:
[Google Colab Link](https://colab.research.google.com/drive/1ClGGyzAw6XEJfpv92NTrnddQiiRsbAqd?usp=sharing)

---


## Catatan Akhir
Projek ini dirancang untuk memberikan wawasan tentang bagaimana sentimen publik terhadap program makan siang gratis. Dengan memanfaatkan teknik NLP, hasil ini dapat membantu pengambil kebijakan memahami persepsi masyarakat dan meningkatkan program tersebut di masa depan.

---

### Dikembangkan oleh: **[zfernm](https://www.linkedin.com/in/samuel-hamonangan-s-099604255/)**