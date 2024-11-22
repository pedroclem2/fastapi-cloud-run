from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    """Root endpoint to verify that the API is running."""
    return {"message": "FastAPI is running on Google Cloud Run!"}

@app.get("/prices")
async def get_prices(from_date: str, to_date: str):
    """
    Example endpoint to fetch data based on dates.
    Replace this logic with your own API integration or business logic.
    """
    try:
        # Example validation and mock response
        from_date_parsed = datetime.strptime(from_date, "%Y-%m-%d")
        to_date_parsed = datetime.strptime(to_date, "%Y-%m-%d")
        return {"data": [{"from_date": from_date, "to_date": to_date, "example": "data"}]}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
