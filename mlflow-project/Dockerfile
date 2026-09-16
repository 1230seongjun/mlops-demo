FROM python:3.11-slim

RUN pip install mlflow
WORKDIR /app
COPY test.py .

CMD python3 test.py
