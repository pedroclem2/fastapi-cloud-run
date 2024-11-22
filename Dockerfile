# Use a lightweight Python 3.9 image
FROM python:3.9-slim@sha256:980b778550c0d938574f1b556362b27601ea5c620130a572feb63ac1df03eda5 

# Set Python to unbuffered mode for consistent logs
ENV PYTHONUNBUFFERED True

# Set the working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy the application code
COPY src/ ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Use the PORT environment variable for Cloud Run
ENV PORT 8080
EXPOSE 8080

# Start the application
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 1
