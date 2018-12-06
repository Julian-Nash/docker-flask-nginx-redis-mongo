from app import app
from mongoengine import connect

app.config.from_object('config.ProductionConfig')

connect(
    db=app.config["DB_NAME"],
    username=app.config["DB_USERNAME"],
    password=app.config["DB_PASSWORD"],
    authentication_source=app.config["DB_AUTH_SOURCE"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")