from flask import Flask
from mongoengine import connect
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

connect("flask-db", host="mongo")

from app import views
from app import models