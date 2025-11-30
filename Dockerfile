FROM python:3.11-slim

WORKDIR /workspace

# Install vim inside the container
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /workspace

CMD ["bash"]
