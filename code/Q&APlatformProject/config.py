class Config(object):
    HOSTNAME = "127.0.0.1"
    PORT = 3306
    USERNAME = "root"
    PASSWORD = "dd19991207"
    DATABASE = "database_flask"
    DB_URL = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}"
                                             f":{PORT}/{DATABASE}?charset=utf8mb4")
    SQLALCHEMY_DATABASE_URI = DB_URL

    # mail配置
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = "tguo7@ucsc.edu"
    MAIL_PASSWORD = "woockaavzljzcnzx"
    MAIL_DEFAULT_SENDER = "tguo7@ucsc.edu"

    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "127.0.0.1"
    CACHE_REDIS_PORT = 6379