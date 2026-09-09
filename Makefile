client:
	streamlit run frontend/client.py --server.address=0.0.0.0 --server.port=8501 &
server:
	uvicorn backend.server:app --host 0.0.0.0 --port 8000
