# Machine-Learning

Repositori ini berisi pipeline lengkap untuk proyek Machine Learning yang berfokus pada pemrosesan data medis berbentuk tabular menjadi teks naratif, melakukan anonimisasi dengan pendekatan hybrid, melakukan preprocessing NLP, melakukan weak labelling berbasis Quasi-Identifier (QI), melakukan ekstraksi fitur teks, serta membangun model machine learning dan deep learning untuk klasifikasi risiko. Seluruh tahapan disusun secara sistematis sehingga dapat direplikasi untuk keperluan akademik maupun eksperimen lanjutan.

## 1. Fitur Utama
Proyek ini mencakup seluruh tahapan pemrosesan data teks secara end-to-end, antara lain:

- **Serialisasi Data**  
  Mengubah data tabular menjadi narasi menggunakan LLM (Large Language Model). Tujuannya adalah membuat data tekstual yang lebih kaya konteks dari tabel mentah.

- **Hybrid Anonymization**  
  Menghilangkan informasi sensitif melalui:
  - Pseudonymization (mengganti identitas dengan kode hash)
  - Generalization (penyederhanaan nilai seperti usia → rentang)
  - Semantic Perturbation (pengubahan kalimat tingkat ringan tanpa mengubah makna)

- **Preprocessing NLP**  
  Membersihkan teks dari noise, normalisasi angka, menghapus stopwords, dan mempersiapkan teks untuk pemodelan.

- **Weak Labelling QI (Quasi-Identifier)**  
  Melakukan pelabelan otomatis berdasarkan pola risiko, seperti usia, jenis kelamin, lokasi, dan kondisi spesifik yang berpotensi sensitif.

- **Feature Extraction**  
  Mengubah teks menjadi representasi numerik menggunakan:
  - Bag-of-Words (BoW)
  - TF-IDF
  - Bigram

- **Feature Selection (Chi-Square)**  
  Memilih fitur paling relevan untuk meningkatkan kinerja model klasik.

- **Model Machine Learning Klasik**  
  Benchmark dengan:
  - Naive Bayes  
  - Logistic Regression  

- **Model Deep Learning**  
  Menggunakan:
  - RNN (Bidirectional)
  - LSTM (Bidirectional)
  - FT-LSTM (Fine-Tuned LSTM)
  - LoRA-BERT (Fine-tuning parameter-efficient)

- **Analisis Error**  
  Mengidentifikasi pola kesalahan model untuk interpretasi lanjutan.

## 2. Struktur Folder
Struktur folder menunjukkan pembagian tugas yang jelas untuk setiap tahap pipeline.

```
notebook/
├── 1.anonimisasi_ml.py              # Serialisasi + anonimisasi
├── 2.preprocessing.py               # Preprocessing teks
├── 3.weak_labbeling_qi.py           # Weak labelling QI
├── 4.pendekatan_fitur_klasik.py     # BoW, TF-IDF, Bigram
├── 5.feature_selection.py           # Seleksi fitur
├── 6.benchmark.py                   # Benchmark ML klasik
├── 7.uji_model.py                   # Evaluasi model
├── 8.deep_learning.py               # Deep learning (RNN/LSTM/FT-LSTM)
└── 9.analisis_error.py              # Analisis error

src/
├── anonymization/                   # Modul anonimisasi
├── classical_ml/                    # Benchmark ML klasik
├── deep_learning/                   # Arsitektur deep learning
├── features/                        # BoW, TF-IDF, Bigram, Chi-Square
├── lora/                            # Fine-tuning BERT dengan LoRA
├── models/                          # Model yang disimpan
├── preprocessing/                   # Pembersihan teks
└── qi_labelling/                    # Weak labelling berbasis QI

scripts/
├── run_full_pipeline.py             # Menjalankan seluruh pipeline otomatis
└── run_deep_learning.py             # Fokus pada training deep learning

dataset project ml/
├── Data Anonimisasi/
├── Data Preprocessed/
├── Data Labelling/
├── Data Pendekatan Klasik/
├── Data Feature Selection/
├── Data Benchmark/
├── Data Serialisasi/
├── Data Error Analisis/
└── Data Uji Model/
```

## 3. Instalasi
Pastikan semua dependensi terinstal dengan menjalankan:

```
pip install -r requirements.txt
```

Penggunaan virtual environment direkomendasikan agar tidak terjadi konflik versi paket Python.

## 4. Menjalankan Pipeline
Setiap bagian pipeline dapat dijalankan secara manual melalui notebook, tetapi tersedia juga script otomatis untuk mempercepat eksekusi.

### Menjalankan pipeline lengkap:
```
python scripts/run_full_pipeline.py
```

### Menjalankan model deep learning saja:
```
python scripts/run_deep_learning.py
```

### Menjalankan tiap tahap secara manual:
Gunakan notebook sesuai nomor urut pada folder `notebook/`.

## 5. Hasil Eksperimen
Proyek ini mengevaluasi beberapa model dan menemukan hasil berikut:

- **Logistic Regression + BoW**  
  Memberikan performa tinggi dengan akurasi hingga **0.98**, stabil pada kedua dataset.

- **Fine-Tuned LSTM (FT-LSTM)**  
  Model terbaik secara keseluruhan dengan akurasi:
  - **0.98** untuk Clinical Dataset
  - **0.96** untuk Demographic Dataset  

- **LoRA-BERT**  
  Memberikan hasil baik (0.82–0.91) namun sensitif terhadap data imbalance dan preprocessing.

Hasil ini menunjukkan bahwa pendekatan deep learning yang dituning dengan baik memberikan performa yang sangat kompetitif meskipun data telah dianonimkan.

## 6. Dokumentasi Tambahan
Penjelasan lengkap tentang metodologi, eksperimen, dan analisis dapat ditemukan pada laporan penelitian terkait. Repositori ini disusun agar mudah direplikasi untuk kebutuhan akademik dan penelitian lanjutan.

