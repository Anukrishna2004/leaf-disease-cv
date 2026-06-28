from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
import time
from torchvision import transforms, models

app = FastAPI()

CLASS_NAMES = [
"Tomato___healthy",
"Tomato___Early_blight",
"Tomato___Late_blight",
"Tomato___Leaf_Mold"
]

model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 4)
model.load_state_dict(
torch.load("models/resnet18_best.pth", map_location="cpu")
)
model.eval()

transform = transforms.Compose([
transforms.Resize((224, 224)),
transforms.ToTensor(),
transforms.Normalize(
mean=[0.485, 0.456, 0.406],
std=[0.229, 0.224, 0.225]
)
])

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    image = transform(image).unsqueeze(0)

    start = time.time()
    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        confidence, pred = torch.max(probs, 1)

    inference_ms = (time.time() - start) * 1000

    return {
        "class": CLASS_NAMES[pred.item()],
        "confidence": round(confidence.item() * 100, 2),
        "inference_ms": round(inference_ms, 2)
    }

