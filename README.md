# E5 Embedder API

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://semver.org)

This is a simple FastAPI-based service that provides two main endpoints:

- **`/embed`**: Generates normalized sentence embeddings using the [`intfloat/e5-large`](https://huggingface.co/intfloat/e5-large) model.
- **`/count-tokens`**: Counts the number of tokens for each input sentence using the Hugging Face tokenizer.

---

## 🔧 Requirements

- [Docker](https://www.docker.com/) installed

---

## 📦 Clone and Prepare the Model

To include the model in the build context, clone the Hugging Face repository inside the `app` folder:

```bash
git clone https://huggingface.co/intfloat/e5-large app/e5_model
```
Make sure the directory structure is like this:

```
.
├── app
│   ├── main.py
│   ├── requirements.txt
│   └── e5_model
│       ├── config.json
...
```

## 🛠 Build the Docker Image

You can build the Docker image and assign it a specific version (e.g. `v0.1.0`):

```bash
docker build -t e5-embedder:v0.1.0 .
```

---

## ▶️ Run the Container

To run the service and expose it on port 8000:

```bash
docker run -p 8000:8000 e5-embedder:v0.1.0
```

The API will be accessible at: [http://localhost:8000](http://localhost:8000)

---

## 📬 Available Endpoints

### POST `/embed`

**Request:**

```json
{
  "sentences": ["What is the capital of France?", "Tell me about Python."]
}
```

**Response:**

```json
{
  "vectors": [[...], [...]]
}
```

Each vector is a normalized embedding of the input sentence.

---

### POST `/count-tokens`

**Request:**

```json
{
  "sentences": ["Hello world!", "This is a test."]
}
```

**Response:**

```json
{
  "token_counts": [
    {"sentence": "Hello world!", "token_count": 4},
    {"sentence": "This is a test.", "token_count": 6}
  ]
}
```

---

## 📁 Project Structure

```
.
├── Dockerfile
├── app
│   ├── main.py
│   ├── requirements.txt
│   └── e5_model/         # Cloned model files here
```

---

## 🧼 Clean Up

To remove the container after testing:

```bash
docker ps -a          # Find container ID
docker rm <container_id>
```

To remove the image:

```bash
docker rmi e5-embedder:v0.1.0
```

---
