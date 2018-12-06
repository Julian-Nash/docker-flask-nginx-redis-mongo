class Config(object):
    SECRET_KEY = "kueghfo734yfo8g387"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True