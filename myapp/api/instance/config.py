"""Configuration file"""

class Config(object):
    DEBUG = False

class Development(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True
    DEBUG = True

class Production(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': Development,
    'debug': Development,
    'testing': Testing,
    }
