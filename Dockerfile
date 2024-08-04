FROM python:3.10-slim

WORKDIR /takewords

COPY . /takewords

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
