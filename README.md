## Caricare modello
git clone https://huggingface.co/intfloat/e5-large app/e5_model

## Creare immagine
docker build -t e5-embedder .

## Lanciare container
docker run -p 8000:8000 e5-embedder
