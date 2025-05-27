import os
import cv2
import albumentations as A
from tqdm import tqdm

# Folder root input dan output
input_root = r'D:\data-preprocessing\dataset-ori'
output_root = r'D:\data-preprocessing\dataset-aug'

# Transformasi augmentasi
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=20, p=0.5),
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=15, p=0.5),
    A.Blur(p=0.2),
    A.Resize(224, 224)
])

# Bikin folder output root
os.makedirs(output_root, exist_ok=True)

# Loop semua folder class
for class_name in os.listdir(input_root):
    class_input_path = os.path.join(input_root, class_name)
    class_output_path = os.path.join(output_root, class_name)

    if not os.path.isdir(class_input_path):
        continue

    os.makedirs(class_output_path, exist_ok=True)

    for img_name in tqdm(os.listdir(class_input_path), desc=f"Augmenting {class_name}"):
        img_path = os.path.join(class_input_path, img_name)
        image = cv2.imread(img_path)
        if image is None:
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Simpan gambar original (optional)
        ori_out_path = os.path.join(class_output_path, f"{os.path.splitext(img_name)[0]}_ori.jpg")
        cv2.imwrite(ori_out_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # Buat 3 augmentasi per gambar
        for i in range(3):
            augmented = transform(image=image)['image']
            aug_name = f"{os.path.splitext(img_name)[0]}_aug{i}.jpg"
            aug_path = os.path.join(class_output_path, aug_name)
            cv2.imwrite(aug_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))
