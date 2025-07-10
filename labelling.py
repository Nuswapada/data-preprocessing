import os

# Path ke folder dataset hasil augment
base_folder = r'D:\data-preprocessing\dataset-aug'  # sesuaikan path relatif dari script

# Ekstensi gambar yang mau di-rename
ext = ".jpg"

# Loop semua folder class
for class_name in os.listdir(base_folder):
    class_path = os.path.join(base_folder, class_name)

    if not os.path.isdir(class_path):
        continue

    print(f"🔧 Merename file di: {class_name}")
    for i, filename in enumerate(os.listdir(class_path)):
        if filename.endswith(ext):
            new_name = f"{class_name}_{i+1}{ext}"
            old_path = os.path.join(class_path, filename)
            new_path = os.path.join(class_path, new_name)
            os.rename(old_path, new_path)
            print(f"  Renamed: {filename} → {new_name}")

print("✅ Semua file udah di-rename! Sekarang dataset-mu lebih rapi! Tapi kamu masih berantakan sih… hmph!")
