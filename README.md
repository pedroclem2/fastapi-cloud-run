# FastAPI Cloud Run Deployment

This repository contains everything you need to deploy a FastAPI application to Google Cloud Run.

## Prerequisites

- Python 3.9+
- Docker installed locally
- Google Cloud SDK installed and configured
- A Google Cloud project with billing enabled

## Local Development

1. Install dependencies:

   ```bash
   pip install -r src/requirements.txt
   ```

2. Run the app locally:

   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
   ```

3. Test the app:
   - Visit: `http://127.0.0.1:8080/`
   - Example API: `http://127.0.0.1:8080/prices?from_date=2024-11-19&to_date=2024-11-20`

## Build and Test Locally with Docker

1. Build the Docker image:

   ```bash
   docker build -t fastapi-cloud-run .
   ```

2. Run the container locally:

   ```bash
   docker run -dp 8080:8080 -e PORT=8080 fastapi-cloud-run
   ```

3. Test the container:
   - Visit: `http://127.0.0.1:8080/`
   - Example API: `http://127.0.0.1:8080/prices?from_date=2024-11-19&to_date=2024-11-20`

## Deploy to Google Cloud Run

1. Build and submit the Docker image to Google Cloud Build:

   ```bash
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/fastapi-cloud-run
   ```

2. Deploy to Cloud Run:

   ```bash
   gcloud run deploy fastapi-cloud-run        --image gcr.io/<PROJECT-ID>/fastapi-cloud-run        --platform managed        --region us-central1        --allow-unauthenticated
   ```

3. Test the deployed app:
   - Retrieve the URL:
     ```bash
     gcloud run services describe fastapi-cloud-run --region us-central1 --format 'value(status.url)'
     ```
   - Access the app at the URL.

## Clean Up

To delete the deployed service:

```bash
gcloud run services delete fastapi-cloud-run --region us-central1
```
