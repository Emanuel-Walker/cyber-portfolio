# Minimal reproducible image for the triage agent.
# Ollama itself runs on the host (or a sidecar). This image only carries the
# Python CLI and expects OLLAMA_HOST to point at a reachable Ollama server.

FROM python:3.11-slim

WORKDIR /app

# Install Python deps first so the layer caches when source changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code tree.
COPY . .

# Default to pointing at a sidecar named "ollama" on the same docker network.
# Override at run time with -e OLLAMA_HOST=http://host.docker.internal:11434
ENV OLLAMA_HOST=http://ollama:11434
ENV TRIAGE_MODEL=llama3.1:8b

# The CLI reads alert JSON on stdin. Keep the entrypoint minimal so
# `docker run ... < alert.json` works the same as a shell pipe.
ENTRYPOINT ["python", "triage_agent.py"]
