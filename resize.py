from PIL import Image
import os
from tqdm import tqdm

input_root = 'makam-raja-ali-haji'
output_root = 'makam-raja-ali-haji-resize'
size = (224, 224)

os.makedirs(output_root, exist_ok=True)

for filename in tqdm(os.listdir(input_root), desc="Resizing images"):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_root, filename)
        output_path = os.path.join(output_root, filename)

        try:
            img = Image.open(input_path).convert('RGB')
            img = img.resize(size)
            img.save(output_path)
        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")

print("✅ Semua gambar udah resize ke 224x224. Siap training lagi nggak nih?! 😤💕")
