import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path



from transforms import train_transform


# Select one sample image
image_path = next(Path("data/train/Tomato___healthy").glob("*.jpg"))

image = Image.open(image_path).convert("RGB")

fig, axes = plt.subplots(2, 4, figsize=(12, 6))

# Original image
axes[0, 0].imshow(image)
axes[0, 0].set_title("Original")
axes[0, 0].axis("off")

# Generate 7 augmented versions
for i, ax in enumerate(axes.flat[1:], start=1):
    aug_img = train_transform(image)

    # Convert tensor back to image format for display
    aug_img = aug_img.permute(1, 2, 0).numpy()

    # Undo normalization for visualization
    aug_img = (aug_img - aug_img.min()) / (aug_img.max() - aug_img.min())

    ax.imshow(aug_img)
    ax.set_title(f"Aug {i}")
    ax.axis("off")

plt.tight_layout()
plt.savefig("augmentation_grid.png")
plt.show()