FROM python:3.11-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /workspace

CMD ["bash"]
