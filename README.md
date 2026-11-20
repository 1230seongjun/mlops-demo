# Hugging Face 텍스트 요약 서비스 (MLOps 실습)

기사 URL을 입력하면 본문을 가져와 요약해 주는 서비스입니다.  
부트캠프 MLOps 과정에서 교안을 참고해 직접 구성한 실습 프로젝트입니다.

## 구조

```
[Streamlit 화면] → [FastAPI /summarize] → [MLflow Model Registry]
     :8501               :8000                 모델 불러오기
```

1. 사용자가 Streamlit 화면에서 기사 URL과 모델을 선택
2. FastAPI 서버가 기사 본문(`<p>` 태그)을 추출
3. MLflow에서 요약 모델을 불러와 요약 (한 번 불러온 모델은 캐시)
4. 요약 결과를 화면에 표시

## 폴더 구성

| 경로 | 내용 |
|---|---|
| `backend/` | FastAPI 요약 API, Dockerfile |
| `frontend/` | Streamlit 화면, Dockerfile |
| `docker-compose.yaml` | backend + frontend 로컬 실행 |
| `Makefile` | 도커 네트워크 생성, 컨테이너 실행/삭제 |
| `k8s/` | Deployment, NFS PV/PVC, 모델 다운로드 Pod |
| `hfcli/` | Hugging Face 모델 다운로드용 이미지 |
| `mlflow-project/` | MLflow Project를 Kubernetes Job으로 실행하는 설정 |

## 기술 스택

- Python, FastAPI, Streamlit
- Hugging Face Transformers (BART, T5)
- MLflow (Model Registry, MLflow Project)
- Docker, Docker Compose
- Kubernetes, NFS

## 실행 방법

```bash
docker compose up --build
```

브라우저에서 `http://localhost:8501` 접속

## 참고

- 실습 환경(사설망) 기준으로 작성되어 MLflow 서버, NFS, 레지스트리 주소가 코드에 들어 있습니다.
- Kubernetes Service 설정은 포함되어 있지 않습니다.
