import vaex
from vaex import agg
import json
import config
from sqlalchemy.orm import sessionmaker
from database import get_connection
from sqlalchemy.sql import and_
from utils import get_table_obj
from json_config.imps_config import IMPS_CONFIG

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


def do_agg(imps_file_path, clicks_file_path, action_name, hour):
    for item in IMPS_CONFIG:

        table_name, process_select, process_group_by, table_name = processing_config(item)
        imps_df = vaex.read_csv('imps_20220523_04.csv', header=None)

        imps_df_cols = imps_df.column_names
        for i in range(len(IMPS_CLICK_HEADER)):
            imps_df.rename(imps_df_cols[i], IMPS_CLICK_HEADER[i], unique=True)

        select_imps_df = imps_df[process_select].groupby(
            by=process_group_by,
            agg=dict_agg
        )

        list_select_cols = select_imps_df.column_names

        engine = get_connection()

        Session = sessionmaker(bind=engine)
        session = Session()
        table_obj = get_table_obj(table_name)
        print("=====================", table_obj.__getattribute__('ad_id'))
        for index, row in select_imps_df.iterrows():
            exist_obj = session.query(table_obj).filter(
                and_(table_obj.ad_id == row['ad_id'], table_obj.tag_id == row['tag_id'])).first()
            if exist_obj is not None:
                pass
            else:
                obj = table_obj(ad_id=row['ad_id'], tag_id=row['tag_id'], imp=row['imp'],
                                spent_cpm=row['spent_cpm'], hour=hour)
                print(obj)
                # session.add(obj)
                # session.commit()
