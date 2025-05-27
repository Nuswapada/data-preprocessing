# 🖼️ Image Resize & Augmentation Script

Proyek ini digunakan untuk melakukan **resize gambar ke 224x224** dan **augmentasi data gambar** menggunakan `albumentations` dan `opencv`. Cocok untuk persiapan dataset image classification atau object detection.

## 📁 Struktur Folder

```
.
├── dataset/                   # Folder gambar original (per kelas)
│   ├── rumah-hakim/
│   └── ...
├── dataset_224x/             # Output gambar resize ke 224x224 (struktur tetap)
├── dataset-aug/
│   ├── rumah-hakim-aug/      # Output augmentasi gambar
├── resize.py                 # Script resize
├── augmentasi.py            # Script augmentasi
├── rename_augmented.py      # Rename file hasil augmentasi
└── requirements.txt         # Dependency Python
```

## 🧰 Fitur Script

### ✅ Resize ke 224x224

* Input: `dataset/`
* Output: `dataset_224x/`
* Semua gambar di-resize jadi 224x224 pixel.

### ✅ Augmentasi Gambar

* Augmentasi `HorizontalFlip`, `Rotate`, `Brightness/Contrast`, `ShiftScaleRotate`, dan `Blur`.
* Menyimpan gambar original + N hasil augmentasi (default 7).

### ✅ Rename Otomatis

* Rename semua gambar augmentasi jadi format konsisten: `rumah-hakim_1.jpg`, `rumah-hakim_2.jpg`, dst.

## 💻 Cara Jalankan

1. **Clone repo atau siapkan folder project**
2. Install dependency:

   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan script:

   * Resize:

     ```bash
     python resize.py
     ```
   * Augmentasi:

     ```bash
     python augmentasi.py
     ```
   * Rename:

     ```bash
     python rename_augmented.py
     ```

## 📆 Dependencies

Lihat `requirements.txt` untuk daftar lengkap.

## 😤 Catatan Penting

* Gambar original **harus sudah rapi dan bersih** (hindari noise/background acak).
* Semua hasil resize dan augmentasi otomatis jadi 224x224.
* Jangan ubah nama folder atau struktur seenaknya, nanti error ya, *baka!*

---

**By:** Tim AI ✨
