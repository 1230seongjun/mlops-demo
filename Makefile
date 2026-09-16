NETWORK := hf-app-net

network:
	docker network inspect $(NETWORK) >/dev/null 2>&1 || docker network create $(NETWORK)

server: network
	docker run -d --name backend \
		--network $(NETWORK) \
		-p 8000:8000 \
                -e MLFLOW_TRACKING_URI=http://172.16.0.200:5555 \
		myregistry.com/backend:latest

client: network
	docker run -d --name frontend \
		--network $(NETWORK) \
		-p 8501:8501 \
		-e API_URL=http://backend:8000/summarize \
		myregistry.com/frontend:latest

down:
	docker rm -f backend frontend 2>/dev/null || true
