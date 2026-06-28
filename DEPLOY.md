# Leaf Disease Detection API Deployment

## Prerequisites

* Docker Desktop installed
* Docker service running

## Build Docker Image

```bash
docker build -t leaf-disease-api .
```

## Run Docker Container

```bash
docker run -p 8000:8000 leaf-disease-api
```

## Environment Variables

* MODEL_PATH=/app/models/resnet18_best.pth
* CLASS_NAMES_PATH=/app/models/class_names.json

## API Endpoints

### Health Check

GET

```
http://localhost:8000/health
```

Response

```json
{
  "status": "healthy"
}
```

### Prediction

POST

```
http://localhost:8000/predict
```

Upload a tomato leaf image using Swagger UI at:

```
http://localhost:8000/docs
```

The API returns:

* predicted class
* confidence score
* inference time (milliseconds)
