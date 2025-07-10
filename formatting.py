import os
from PIL import Image

DATA_DIR = "dataset_output"

for label in os.listdir(DATA_DIR):
    label_path = os.path.join(DATA_DIR, label)
    if not os.path.isdir(label_path):
        continue

    for img_name in os.listdir(label_path):
        path = os.path.join(label_path, img_name)
        try:
            with Image.open(path) as im:
                rgb_im = im.convert("RGB")
                new_name = os.path.splitext(img_name)[0] + ".jpg"
                new_path = os.path.join(label_path, new_name)
                rgb_im.save(new_path, "JPEG")
                if img_name != new_name:
                    os.remove(path)
        except Exception as e:
            print(f"Format convert error on {img_name}: {e}")
