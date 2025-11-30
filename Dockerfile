FROM python:3.11-slim

# Install vim inside the container
RUN apt-get update && apt-get install -y --no-install-recommends vim && rm -rf /var/lib/apt/lists/*

# Workdir inside the container
WORKDIR /workspace

# optional: you can leter pre-install requirements here
# for now, aie_full_setup.sh will handle venv + installs inside the container.
# COPY requirements.txt .
# RUN pip install --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt

# Copy project code into the image (bind mount will override at runtime)
COPY . /workspace

CMD ["bash"]
