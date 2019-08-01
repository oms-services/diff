FROM        python:3.7-alpine

ADD         requirements.txt app.py gdiff.py /app
RUN         pip install -r /app/requirements.txt

ENTRYPOINT  ["python", "/app/app.py"]
