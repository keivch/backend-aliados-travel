import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    JSON_AS_ASCII = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

class TestingConfig:
    TESTING = True
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
