FROM python:3.11-slim-buster 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/app 

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt 

CMD ["gunicorn", "tutorial.wsgi:application", "-w", "2", "-b", "0.0.0.0:8000"]
