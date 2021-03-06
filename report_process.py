from sqlalchemy.orm import sessionmaker
from database.database import get_connection
from config.report_config import REPORT_CONFIG
from utils.utils import get_table_obj, get_current_date_hour
from loguru import logger
import pandas as pd
import time
import argparse
from datetime import timedelta


def create_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-y', '--yesterday', default=False, action='store_true', help='Yesterday')
    ap.add_argument('-cd', '--custom_date', help='Custom date', type=str)

    args = ap.parse_args()
    return args


def do_report(date):
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    session = Session()

    for config in REPORT_CONFIG:
        sql = config['sql'].format(date=date)
        indexes = config['index']
        table_obj = get_table_obj(config['table_name'])
        logger.info('PROCESSING TABLE %s ' % config['table_name'].replace("_by_node_hour", ""))
        raw_table_obj = get_table_obj(config['table_name'].replace("_by_node_hour", ""))
        df = pd.read_sql(sql, session.bind)
        # df = df.fillna(0)
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
                    session.commit()
            else:
                obj = raw_table_obj()
                for key in row.keys():
                    setattr(obj, key, str(row[key]))
                session.add(obj)
                session.commit()
    session.close()


if __name__ == '__main__':
    try:
        args = create_args()
        date = None
        if args.yesterday:
            ct = get_current_date_hour()
            logger.info('YESTERDAY MODE')
            date = "'{}'".format((ct - timedelta(days=1)).date().strftime('%Y-%m-%d'))
            logger.info(date)
        elif args.custom_date is not None:
            logger.info('CUSTOM DATE MODE')
            date = args.custom_date
            logger.info(date)
        # else:
        #     logger.info('NORMAL MODE')
        #     ct = get_current_date_hour()
        #     date = "'{}'".format(ct.date().strftime('%Y-%m-%d'))
        #     logger.info(date)
        if args.yesterday or args.custom_date is not None:
            do_report(date)
        else:
            while True:
                ct = get_current_date_hour()
                date = "'{}'".format(ct.date().strftime('%Y-%m-%d'))
                do_report(date)
                time.sleep(60)
    except Exception as ex:
        logger.info(str(ex))
