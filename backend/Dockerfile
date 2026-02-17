FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask flask-cors flask-sqlalchemy psycopg2-binary

EXPOSE 5000

CMD ["python", "app.py"]
