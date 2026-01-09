FROM python:3.11-alpine

WORKDIR /app

# Kopeeri AINULT requirements ENNE source koodi
COPY requirements.txt .

# Install dependencies - see layer cache'itakse
RUN pip install --no-cache-dir -r requirements.txt

# Nüüd kopeeri rakenduse kood
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
