FROM python:3.7.1-stretch

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["uwsgi", "wsgi.ini"]