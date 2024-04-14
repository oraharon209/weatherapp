FROM python:alpine3.19
WORKDIR /weatherapp
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:9090 wsgi:app
