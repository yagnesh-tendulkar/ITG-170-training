FROM python:3.11-slim

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Run the app with Gunicorn + Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "backend.main:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
