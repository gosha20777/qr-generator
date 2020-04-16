FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn server:app --host 0.0.0.0 --port 5000 --log-config log-config.yaml