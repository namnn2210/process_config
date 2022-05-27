import vaex
from vaex import agg
import json
import config
import os
from sqlalchemy.orm import sessionmaker
from database import get_connection
from sqlalchemy.sql import and_
from utils import get_table_obj
from json_config.imps_config import IMPS_CONFIG
from loguru import logger

IMPS_CLICK_HEADER = config.IMPS_CLICK_HEADER
REQUESTS_HEADER = config.REQUESTS_HEADER

dict_agg = {
}


def processing_config(json_config):
    dict_config = json_config
    process = dict_config['process']
    table_name = dict_config['table_name']
    process_select = process['select']
    process_group_by = process['group_by']
    process_agg = process['agg']
    for key, value in process_agg.items():
        if key == 'sum':
            for item in value:
                if 'group' not in item.keys():
                    dict_agg[item['alias']] = agg.sum(item['field'][0])
                else:
                    if item['group'] == 'multiple':
                        dict_agg[item['alias']] = agg.sum('*'.join(item['field']))

    return table_name, process_select, process_group_by, table_name


def do_agg(folder_path, imps_path, today, list_processing_hour, server_host):
    try:
        for hour in list_processing_hour:
            logger.info("PROCESSING HOUR %s" % hour)
            for item in IMPS_CONFIG:
                logger.info("PROCESSING TABLE %s" % item)
                table_name, process_select, process_group_by, table_name = processing_config(item)
                imps_file_path = os.path.join(folder_path, imps_path, today,
                                              '{}_{}_{}.csv'.format(imps_path, today, hour))
                try:
                    imps_df = vaex.read_csv(imps_file_path, header=None)
                    imps_df_cols = imps_df.column_names
                    for i in range(len(IMPS_CLICK_HEADER)):
                        imps_df.rename(imps_df_cols[i], IMPS_CLICK_HEADER[i], unique=True)

                    select_imps_df = imps_df[process_select].groupby(
                        by=process_group_by,
                        agg=dict_agg
                    )

                    list_cols = select_imps_df.column_names

                    engine = get_connection()

                    Session = sessionmaker(bind=engine)
                    session = Session()
                    table_obj = get_table_obj(table_name)
                    for index, row in select_imps_df.iterrows():
                        exist_obj = session.query(table_obj)
                        for col in process_group_by:
                            exist_obj = exist_obj.filter(getattr(table_obj, col) == row[col])
                        exist_obj = exist_obj.first()
                        if exist_obj is not None:
                            for col in list_cols:
                                setattr(exist_obj, col, row[col])
                                setattr(exist_obj, 'hour', hour)
                                setattr(exist_obj, 'server_host', server_host)
                            session.commit()
                        else:
                            obj = table_obj()
                            for col in list_cols:
                                setattr(obj, col, row[col])
                            setattr(obj, 'hour', hour)
                            setattr(obj, 'server_host', server_host)
                            session.add(obj)
                            session.commit()
                    session.close()
                except FileNotFoundError as file_not_found:
                    logger.info('ERROR: %s' % str(file_not_found))
                    logger.info("FILE HOUR %s NOT FOUND" % hour)
                    continue
    except Exception as ex:
        logger.info('PROCESSING ERROR: %s' % str(ex))
