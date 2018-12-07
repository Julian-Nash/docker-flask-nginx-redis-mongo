# Simple dockerised Flask application

*Note - Early work in progress. Day 1 of Docker*

#### Flask app comprised of 4 containers

```
flask: Contains the Flask application and uWSGI application server
nginx: Contains the Nginx web server
redis: Contains the Redis cache
mongo: Contains the MongoDB database
```

#### Some info on the stack

```
Python version: 3.7.1
Web framework:  Flask
Database:       MongoDB (Using the Mongoengine driver)
Cache:          Redis
App server:     uWSGI
Web server:     Nginx
Front end:      Bootsrap4
```

#### Give it a spin

1. Pull this repo
2. Update the username & password for mongo in `docker-compose.yml`
3. Update the password for redis in `docker-compose.yml`
4. Update the mongo & redis username & passwords in `flask/app/__init__.py`
5. `docker-compose up --build`
6. Go to `127.0.0.1/` in your browser

Consider installing MongoDB compass and connect to the mongo container for a helpful debugging & data exploring tool

Remove the following lines from `docker-compose.yml` to remove the exposed mongo ports for production

```
ports:
  - "27017:27017"
```

#### TODO

1. Write a solid nginx.conf
2. Automate SSL certs
3. Better handling/automation of usernames, passwords & environment variables. Look into `.env` file
4. Integrate a celery container & setup background tasks
5. Learn more about Docker

#### Notes

Mongo auth has been a bit buggy

Feedback welcome!




