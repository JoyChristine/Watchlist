class Config:
   pass

class ProdConfig(Config):
    pass


class DevConfig:
    DEBUG = True
    