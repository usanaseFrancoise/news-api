import os

class Config:
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY ='7898c1e92e3f4963b15bf09d8dcb0c15'

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
   DEBUG =   True  

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}

