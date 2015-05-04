from ubuntu:14.04
maintainer jesse.miller@adops.com

run apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip

run pip install pymongo

add load.py /app/load.py
workdir /app

cmd ["python", "load.py"]