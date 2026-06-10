from pathlib import Path
import random
import shutil

random.seed(42)

classes = [
    "Tomato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold"
]

source_root = Path("data/raw")
train_root = Path("data/train")
val_root = Path("data/val")

for cls in classes:
    source_dir = source_root / cls

    train_dir = train_root / cls
    val_dir = val_root / cls

    train_dir.mkdir(parents=True, exist_ok=True)
    val_dir.mkdir(parents=True, exist_ok=True)

    images = list(source_dir.glob("*"))

    random.shuffle(images)

    split_idx = int(0.8 * len(images))

    train_imgs = images[:split_idx]
    val_imgs = images[split_idx:]

    for img in train_imgs:
        shutil.copy(img, train_dir / img.name)

    for img in val_imgs:
        shutil.copy(img, val_dir / img.name)

    print(
        f"{cls}: "
        f"{len(train_imgs)} train, "
        f"{len(val_imgs)} val"
    )