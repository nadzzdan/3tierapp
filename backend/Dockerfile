FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# uvicorn on 0.0.0.0 for k8s
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
