FROM python:3.10-slim

# Imposta working directory
WORKDIR /app

# Copia i file dell'app
COPY app /app

# Variabile d'ambiente per percorso modello
ENV MODEL_PATH=/app/e5_model

# Installa dipendenze e pulisce cache pip
RUN apt-get update && apt-get install -y git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    apt-get remove -y git && apt-get autoremove -y && apt-get clean

# Espone la porta FastAPI
EXPOSE 8000

# Avvia l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

