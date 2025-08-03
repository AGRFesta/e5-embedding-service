FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY app /app

# Set environment variable for model path
ENV MODEL_PATH=/app/e5_model

# Install dependencies and clean up pip and OS package cache
RUN apt-get update && apt-get install -y git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    apt-get remove -y git && apt-get autoremove -y && apt-get clean

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
