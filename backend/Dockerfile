FROM huggingface/transformers-torch-light
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
        build-essential \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server.py .
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
