from sqlalchemy.orm import sessionmaker
from database.database import get_connection
from config.report_config import REPORT_CONFIG
from utils.utils import get_table_obj, get_current_date_hour
from loguru import logger
import pandas as pd
import time

if __name__ == '__main__':
    try:
        while True:
            engine = get_connection()
            Session = sessionmaker(bind=engine)
            session = Session()

            for config in REPORT_CONFIG:
                ct = get_current_date_hour()
                date = "'{}'".format(ct.date().strftime('%Y-%m-%d'))
                # date = "'{}'".format('2022-05-31')
                sql = config['sql'].format(date=date)
                indexes = config['index']
                table_obj = get_table_obj(config['table_name'])
                logger.info('PROCESSING TABLE %s ' % config['table_name'].replace("_by_node_hour", "_swap"))
                raw_table_obj = get_table_obj(config['table_name'].replace("_by_node_hour", "_swap"))
                df = pd.read_sql(sql, session.bind)
                df = df.fillna(0)
                list_cols = list(df.columns.values)
                for _, row in df.iterrows():
                    exist_obj = session.query(raw_table_obj)
                    for index in indexes:
                        exist_obj = exist_obj.filter(getattr(raw_table_obj, index) == row[index])
                    exist_obj = exist_obj.first()
                    if exist_obj is not None:
                        for key in row.keys():
                            if key in indexes:
                                continue
                            setattr(exist_obj, key, str(row[key]))
                    else:
                        obj = raw_table_obj()
                        for key in row.keys():
                            setattr(obj, key, str(row[key]))
                        session.add(obj)
                        session.commit()
                session.close()
                time.sleep(120)
    except Exception as ex:
        logger.info(str(ex))
