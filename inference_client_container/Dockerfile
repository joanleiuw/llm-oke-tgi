FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY llama3_gradio.py /app
EXPOSE 7860
CMD ["python", "/app/llama3_gradio.py"]
