from models import models
import vaex
import os
import time

from datetime import datetime, timedelta
from loguru import logger
from vaex import agg
from sqlalchemy.orm import sessionmaker
from database.database import get_connection
import pytz

dict_agg = {
}


def get_current_date_hour():
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    ct = datetime.now(tz=tz)
    return ct


def get_last_hour():
    _, current_hour = get_current_date_hour()
    return current_hour - 1


def get_table_obj(table_name):
    if table_name == 'stats_ads_device':
        return models.StatsAdsDeviceByNodeHour
    elif table_name == 'stats_ads_hour':
        return models.StatsAdsHourByNodeHour
    elif table_name == 'stats_ads_location':
        return models.StatsAdsLocationByNodeHour
    elif table_name == 'stats_ads_performance':
        return models.StatsAdsPerformanceByNodeHour
    elif table_name == 'stats_ads_tags_browser':
        return models.StatsAdsTagsBrowserByNodeHour
    elif table_name == 'stats_ads_tags_campaign':
        return models.StatsAdsTagsCampaignByNodeHour
    elif table_name == 'stats_ads_tags_date':
        return models.StatsAdsTagsDateByNodeHour
    elif table_name == 'stats_ads_tags_device':
        return models.StatsAdsTagsDeviceByNodeHour
    elif table_name == 'stats_ads_tags_location':
        return models.StatsAdsTagsLocationByNodeHour
    elif table_name == 'stats_ads_tags_position':
        return models.StatsAdsTagsPositionByNodeHour
    elif table_name == 'stats_campaigns':
        return models.StatsCampaignByNodeHour
    elif table_name == 'stats_campaigns_indicator':
        return models.StatsCampaignsIndicatorByNodeHour
    elif table_name == 'stats_event':
        return models.StatsEventByNodeHour
    elif table_name == 'stats_tags_browser':
        return models.StatsTagsBrowserByNodeHour
    elif table_name == 'stats_tags_change':
        return models.StatsTagsChangeByNodeHour
    elif table_name == 'stats_tags_date':
        return models.StatsTagsDateByNodeHour
    elif table_name == 'stats_tags_device':
        return models.StatsTagsDeviceByNodeHour
    elif table_name == 'stats_tags_inventories':
        return models.StatsTagsInventoriesByNodeHour
    elif table_name == 'stats_tags_location':
        return models.StatsTagsLocationByNodeHour
    elif table_name == 'stats_users':
        return models.StatsUsersByNodeHour
    else:
        return None


def processing_config(json_config):
    process = json_config['process']
    table_name = json_config['table_name']
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


def do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header):
    try:
        raw_today = today.strftime('%Y%m%d')
        filter_today = today.strftime('%Y-%m-%d')
        for hour in list_processing_hour:
            logger.info("PROCESSING HOUR %s" % hour)
            for item in list_config:
                logger.info("PROCESSING TABLE %s" % item)
                table_name, process_select, process_group_by, table_name = processing_config(item)

                file_path = os.path.join(folder_path, path, raw_today,
                                         '{}_{}_{}.csv'.format(path, raw_today, hour))
                # file_path = 'imps_20220531_00.csv'
                try:
                    imps_df = vaex.read_csv(file_path, header=None)
                    imps_df_cols = imps_df.column_names
                    for i in range(len(header)):
                        imps_df.rename(imps_df_cols[i], header[i], unique=True)

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
                        exist_obj = exist_obj.filter(
                            getattr(table_obj, 'date') == filter_today).filter(
                            getattr(table_obj, 'hour') == hour)
                        exist_obj = exist_obj.first()
                        if exist_obj is not None:
                            for col in list_cols:
                                setattr(exist_obj, col, row[col])
                            setattr(exist_obj, 'server_host', server_host)
                            if table_name == 'stats_tags_inventories':
                                pass
                            session.commit()
                        else:
                            obj = table_obj()
                            for col in list_cols:
                                setattr(obj, col, row[col])
                            setattr(obj, 'hour', hour)
                            setattr(obj, 'server_host', server_host)
                            setattr(obj, 'date', filter_today)
                            session.add(obj)
                            session.commit()
                    session.close()
                except FileNotFoundError as file_not_found:
                    logger.info('ERROR: %s' % str(file_not_found))
                    logger.info("FILE HOUR %s NOT FOUND" % hour)
                    continue
    except Exception as ex:
        logger.info('PROCESSING ERROR: %s' % str(ex))


def start(folder_path, path, list_processing_hour, server_host, list_config, header, is_last_hour, is_day, is_yesterday,
          is_crontab):
    today = None
    if is_last_hour:
        logger.info('PROCESS COLLECTING LAST HOUR')
        last_hour = f"{get_last_hour():02d}"
        list_processing_hour.append(last_hour)
    elif is_day:
        logger.info('PROCESS COLLECTING FROM BEGINNING OF THE DAY')
        today = get_current_date_hour()
        for hour in range(today.hour):
            formated_hour = f"{hour:02d}"
            list_processing_hour.append(formated_hour)
    elif is_yesterday:
        logger.info('PROCESS COLLECTING YESTERDAY MODE')
        ct = get_current_date_hour()
        today = (ct - timedelta(days=1))
        for hour in range(0, 24):
            formated_hour = f"{hour:02d}"
            list_processing_hour.append(formated_hour)
    elif is_crontab:
        logger.info('PROCESS COLLECTING CRONTAB MODE')
        ct = get_current_date_hour()
        processing_datetime = ct - timedelta(hours=1)
        list_processing_hour.append(processing_datetime.hour)
        today = processing_datetime.today()
    else:
        today = get_current_date_hour()
        list_processing_hour.append(f"{today.hour:02d}")
    if is_crontab:
        do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header)
    else:
        while True:
            do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header)
            time.sleep(120)
