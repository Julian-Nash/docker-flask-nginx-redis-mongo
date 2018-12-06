from flask import Flask
import redis
from mongoengine import connect

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

connect(db="flask-db", host="mongo", port=27017)

from app import views
from app import models