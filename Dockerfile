FROM python:3.8-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]