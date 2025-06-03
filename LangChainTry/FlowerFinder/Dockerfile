FROM python:3.11-alpine

WORKDIR /app
# Установка обновлённого pip
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir --retries 10 --timeout 30 -r requirements.txt

COPY . .

CMD ["python", "main.py"]
