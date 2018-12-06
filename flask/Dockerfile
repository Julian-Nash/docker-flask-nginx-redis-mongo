FROM python:3.7.1-stretch

# FROM python:3.7.1-alpine3.8  # error

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["uwsgi", "wsgi.ini"]