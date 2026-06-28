FROM python:3.11-slim

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --default-timeout=1000 \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    --no-cache-dir -r requirements-api.txt


COPY api/ ./api/
COPY src/ ./src/
COPY models/ ./models/

ENV MODEL_PATH=/app/models/resnet18_best.pth
ENV CLASS_NAMES_PATH=/app/models/class_names.json

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]