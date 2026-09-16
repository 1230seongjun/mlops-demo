FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV API_URL=http://backend:8000/summarize
COPY client.py .
EXPOSE 8501
CMD ["streamlit", "run", "client.py", "--server.address=0.0.0.0", "--server.port=8501"]
