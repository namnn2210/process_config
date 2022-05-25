from sqlalchemy import create_engine
import config


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            config.DBUSERNAME, config.DBPASSWORD, config.DBHOST, config.DBPORT, config.DBNAME
        )
    )


