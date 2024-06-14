FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY model_download.py /app
CMD ["python", "/app/model_download.py"]
