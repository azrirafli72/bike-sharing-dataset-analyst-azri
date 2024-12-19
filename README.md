# **AnalisisDataset Bike Sharing (2011-2012)**

## **Kualitas Peminjaman Sepeda**

Performa peminjaman sepeda pada tahun 2011 hingga 2012 menunjukkan tren yang positif. Terdapat peningkatan signifikan yang terjadi pada kuartal 2 hingga kuartal 3 setiap tahunnya, yang diikuti dengan penurunan pada kuartal terakhir tahun tersebut. Tren ini dapat memberikan wawasan mengenai pola musiman dalam permintaan layanan sepeda berbagi.

## **Kapan Situasi dan Kondisi dengan Peminjaman Tertinggi??**

Berdasarkan analisis data peminjaman sepeda, berikut adalah situasi dan kondisi dengan total peminjaman tertinggi selama dua tahun tersebut:

- **Musim Gugur**: Musim ini tercatat sebagai periode dengan total peminjaman tertinggi dibandingkan dengan musim lainnya, menunjukkan adanya preferensi pengguna terhadap kondisi cuaca pada musim tersebut.
- **Cuaca Cerah dan Sedikit Berawan**: Kondisi cuaca ini memiliki tingkat peminjaman tertinggi, menunjukkan bahwa peminjam lebih memilih untuk menggunakan sepeda saat cuaca yang tidak terlalu ekstrem.
- **Jam Peminjaman Tertinggi**: Waktu dengan peminjaman tertinggi terjadi antara pukul 17:00-18:00 dan pukul 08:00 pagi, yang menunjukkan adanya permintaan tinggi pada awal pagi dan sore hari setelah jam kerja.
- **Hari Kerja vs Akhir Pekan**: Peminjaman sepeda lebih tinggi pada hari Senin hingga Jumat, dengan lonjakan signifikan pada akhir pekan (Sabtu dan Minggu) terutama pada pukul 12:00 hingga 15:00.

## **Statistik Informasi Peminjam Sepeda**

- **Peminjam Terdaftar (Registered Customers)**: Jumlah peminjam sepeda yang terdaftar jauh lebih banyak dibandingkan dengan peminjam kasual, menandakan bahwa pelanggan yang terdaftar cenderung lebih setia dan sering menggunakan layanan.
- **Peminjam Kasual (Casual Customers)**: Meskipun jumlah peminjam kasual lebih sedikit, ada peluang untuk memperluas basis pelanggan dengan menarik lebih banyak peminjam baru melalui pemasaran yang lebih efektif.

## **Kesimpulan dan Saran**

Berdasarkan analisis data peminjaman sepeda selama tahun 2011 dan 2012, dapat disimpulkan bahwa terdapat pola musiman dan harian yang mempengaruhi jumlah peminjaman. Untuk meningkatkan performa layanan, berikut adalah beberapa rekomendasi strategis:

- **Mengembangkan Segmentasi Peminjam Baru**: Fokuskan upaya pemasaran untuk menarik lebih banyak peminjam kasual, sehingga dapat memperluas pangsa pasar dan meningkatkan frekuensi peminjaman.
- **Mengoptimalkan Waktu dan Kondisi Cuaca**: Manfaatkan pola waktu peminjaman yang tinggi dan kondisi cuaca yang mendukung untuk melakukan promosi dan meningkatkan ketersediaan sepeda pada periode-periode tersebut.
  
Dengan menerapkan rekomendasi ini, perusahaan dapat mengoptimalkan potensi pertumbuhan dan memperluas basis pelanggan, sehingga meningkatkan performa bisnis secara keseluruhan.

---

# **Dashboard Bike Sharing Dataset (2011-2012)**

## **Panduan Instalasi dan Setup**

Untuk menjalankan dashboard ini secara lokal, berikut adalah langkah-langkah yang perlu dilakukan.

### **Instalasi Dependencies**

#### **Menggunakan Anaconda**

1. Buat environment baru dengan Python versi 3.11.9:
    ```bash
    conda create --name main-ds python=3.11.9
    conda activate main-ds
    ```

2. Instal dependencies dengan menjalankan perintah berikut:
    ```bash
    pip install -r requirements.txt
    ```

#### **Menggunakan Shell/Terminal**

1. Buat direktori proyek:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```

2. Instal dependencies dengan `pipenv`:
    ```bash
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

### **Menjalankan Dashboard Secara Lokal**

Jalankan aplikasi Streamlit:
```bash
streamlit run dashboard.py
```

---

# **Bike Sharing Dataset - Dicoding**

Dokumentasi ini disusun untuk mempermudah proses analisis dan implementasi dashboard Bike Sharing Dataset, serta untuk memberikan wawasan mendalam tentang tren peminjaman sepeda pada tahun 2011-2012. Selamat mencoba!
