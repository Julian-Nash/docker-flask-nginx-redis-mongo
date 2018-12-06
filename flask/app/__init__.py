from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

from app import views
from app import models