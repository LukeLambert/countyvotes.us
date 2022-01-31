FROM python:3.7-slim

EXPOSE 8080

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
