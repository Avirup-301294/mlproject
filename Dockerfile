FROM python:3.9-slim-bullseye
WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends awscli ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
CMD ["python3", "app.py"]