# 🖼️ Image Preprocessing & Augmentation Toolkit

Toolkit ini digunakan untuk mempersiapkan dataset gambar sebelum digunakan untuk training model image classification atau object detection. Fitur-fitur utama meliputi:

- **Resize semua gambar ke 224x224**
- **Konversi format ke `.jpg`**
- **Augmentasi gambar (flip, rotate, blur, dll)**
- **Rename gambar agar konsisten**

Seluruh proses otomatis mempertahankan struktur folder per kelas (class-based folders).

---

## 📁 Struktur Folder

```
project/
├── dataset/                    # Folder original berisi gambar (per kelas)
│   ├── rumah-hakim/
│   
├── dataset_224x/              # Output hasil resize 224x224
├── dataset-aug/               # Output hasil augmentasi
│   ├── rumah-hakim/
│
├── resize.py                  # Script resize gambar
├── augmentasi.py              # Script augmentasi
├── labelling.py               # Rename hasil augmentasi
├── formatting.py              # Konversi format ke JPG
├── requirements.txt           # Daftar dependency Python
└── README.md
```

---

## ⚙️ Fitur Script

### 🔄 1. Resize ke 224x224

- Input: `dataset/`
- Output: `dataset_224x/`
- Semua gambar akan disimpan dalam ukuran fix 224x224 pixel.

### 🧪 2. Augmentasi Gambar

- Library: `albumentations`, `opencv-python`
- Augmentasi meliputi:
  - Horizontal Flip
  - Rotate
  - Brightness/Contrast
  - ShiftScaleRotate
  - Blur
- Output disimpan di `dataset-aug/` dengan struktur folder yang sama.

### 🏷️ 3. Rename Otomatis

- Semua gambar hasil augmentasi akan diberi nama ulang menjadi:
  ```
  <nama_kelas>_<index>.jpg
  ```

### 🧼 4. Format Converter

- Semua file (misalnya `.webp`, `.png`, `.jpeg`) akan dikonversi ke `.jpg` dan format warna ke RGB.
- Dijalankan sebelum proses resize atau augmentasi.

---

## 🚀 Cara Menjalankan

1. **Persiapkan struktur folder awal di `dataset/`**
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan script sesuai urutan:

   ### 🔧 Format Konversi (Opsional tapi disarankan)
   ```bash
   python format_convert.py
   ```

   ### 🪄 Resize Gambar
   ```bash
   python resize.py
   ```

   ### 🎨 Augmentasi Gambar
   ```bash
   python augmentasi.py
   ```

   ### ✍️ Rename File Augmented
   ```bash
   python rename_augmented.py
   ```

---

## 📦 Requirements

Daftar dependencies (lihat juga di `requirements.txt`):

- pillow
- opencv-python
- albumentations
- tqdm

Install semua sekaligus:

```bash
pip install -r requirements.txt
```

---

## 🧠 Tips Penting

- Pastikan struktur folder di `dataset/` sudah per kelas.
- Hindari file kosong, korup, atau berekstensi aneh.
- Jangan lupa cek hasil akhir di `dataset_224x/` dan `dataset-aug/` sebelum training.

---

## 🙋‍♀️ Credits & Notes

> Dibuat dengan semangat penuh cinta oleh Tim AI.  
> Gunakan dengan bijak — jangan cuma augmentasi gambar, tapi juga semangat kamu! 🚀💪
