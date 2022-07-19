from models import models
import vaex
import os
import time

from datetime import datetime, timedelta
from loguru import logger
from vaex import agg
from sqlalchemy.orm import sessionmaker
from database.database import get_connection
from config.campaign_config import CAMPAIGN_CONFIG

import pytz

dict_agg = {
}


def get_current_date_hour():
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    ct = datetime.now(tz=tz)
    return ct


def get_last_hour():
    ct = get_current_date_hour()
    return ct.hour - 1


def get_table_obj(table_name):
    if table_name == 'stats_ads_device_by_node_hour':
        return models.StatsAdsDeviceByNodeHour
    elif table_name == 'stats_ads_hour_by_node_hour':
        return models.StatsAdsHourByNodeHour
    elif table_name == 'stats_ads_location_by_node_hour':
        return models.StatsAdsLocationByNodeHour
    elif table_name == 'stats_ads_performance_by_node_hour':
        return models.StatsAdsPerformanceByNodeHour
    elif table_name == 'stats_ads_performance':
        return models.StatsAdsPerformance
    elif table_name == 'stats_ads_performance_swap':
        return models.StatsAdsPerformanceSwap
    elif table_name == 'stats_ads_tags_browser_by_node_hour':
        return models.StatsAdsTagsBrowserByNodeHour
    elif table_name == 'stats_ads_tags_browser':
        return models.StatsAdsTagsBrowser
    elif table_name == 'stats_ads_tags_browser_swap':
        return models.StatsAdsTagsBrowserSwap
    elif table_name == 'stats_ads_tags_campaign_by_node_hour':
        return models.StatsAdsTagsCampaignByNodeHour
    elif table_name == 'stats_ads_tags_campaign':
        return models.StatsAdsTagsCampaign
    elif table_name == 'stats_ads_tags_campaign_swap':
        return models.StatsAdsTagsCampaignSwap
    elif table_name == 'stats_ads_tags_date_by_node_hour':
        return models.StatsAdsTagsDateByNodeHour
    elif table_name == 'stats_ads_tags_date':
        return models.StatsAdsTagsDate
    elif table_name == 'stats_ads_tags_date_swap':
        return models.StatsAdsTagsDateSwap
    elif table_name == 'stats_ads_tags_device_by_node_hour':
        return models.StatsAdsTagsDeviceByNodeHour
    elif table_name == 'stats_ads_tags_device':
        return models.StatsAdsTagsDevice
    elif table_name == 'stats_ads_tags_device_swap':
        return models.StatsAdsTagsDeviceSwap
    elif table_name == 'stats_ads_tags_location_by_node_hour':
        return models.StatsAdsTagsLocationByNodeHour
    elif table_name == 'stats_ads_tags_location':
        return models.StatsAdsTagsLocation
    elif table_name == 'stats_ads_tags_location_swap':
        return models.StatsAdsTagsLocationSwap
    elif table_name == 'stats_ads_tags_position_by_node_hour':
        return models.StatsAdsTagsPositionByNodeHour
    elif table_name == 'stats_campaigns_by_node_hour':
        return models.StatsCampaignByNodeHour
    elif table_name == 'stats_campaigns_indicator_by_node_hour':
        return models.StatsCampaignsIndicatorByNodeHour
    elif table_name == 'stats_event_by_node_hour':
        return models.StatsEventByNodeHour
    elif table_name == 'stats_tags_browser_by_node_hour':
        return models.StatsTagsBrowserByNodeHour
    elif table_name == 'stats_tags_browser':
        return models.StatsTagsBrowser
    elif table_name == 'stats_tags_browser_swap':
        return models.StatsTagsBrowserSwap
    elif table_name == 'stats_tags_change_by_node_hour':
        return models.StatsTagsChangeByNodeHour
    elif table_name == 'stats_tags_date_by_node_hour':
        return models.StatsTagsDateByNodeHour
    elif table_name == 'stats_tags_date':
        return models.StatsTagsDate
    elif table_name == 'stats_tags_date_swap':
        return models.StatsTagsDateSwap
    elif table_name == 'stats_tags_device_by_node_hour':
        return models.StatsTagsDeviceByNodeHour
    elif table_name == 'stats_tags_device':
        return models.StatsTagsDevice
    elif table_name == 'stats_tags_device_swap':
        return models.StatsTagsDeviceSwap
    elif table_name == 'stats_tags_inventories_by_node_hour':
        return models.StatsTagsInventoriesByNodeHour
    elif table_name == 'stats_tags_inventories':
        return models.StatsTagsInventories
    elif table_name == 'stats_tags_inventories_swap':
        return models.StatsTagsInventoriesSwap
    elif table_name == 'stats_tags_location_by_node_hour':
        return models.StatsTagsLocationByNodeHour
    elif table_name == 'stats_tags_location':
        return models.StatsTagsLocation
    elif table_name == 'stats_tags_location_swap':
        return models.StatsTagsLocationSwap
    elif table_name == 'stats_users_by_node_hour':
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

    return table_name, process_select, process_group_by


def do_agg_campaign(folder_path, path, server_host, header, raw_today, filter_today, hour):
    temp_df = None
    logger.info("PROCESSING CAMPAIGN")
    for cp_item in CAMPAIGN_CONFIG:
        cp_dict_agg = {}
        table_name = cp_item['table_name']
        process = cp_item['process']
        process_select = process['select']
        process_group_by = process['group_by']
        process_agg = process['agg']
        for key, value in process_agg.items():
            if key == 'sum':
                for cp_item in value:
                    if 'group' not in cp_item.keys():
                        cp_dict_agg[cp_item['alias']] = agg.sum(cp_item['field'][0])
                    else:
                        if cp_item['group'] == 'multiple':
                            cp_dict_agg[cp_item['alias']] = agg.sum('*'.join(cp_item['field']))
            elif key == 'count':
                for cp_item in value:
                    if 'group' not in cp_item.keys():
                        cp_dict_agg[cp_item['alias']] = agg.count(cp_item['field'][0])
        file_path = os.path.join(folder_path, path, raw_today,
                                 '{}_{}_{}.csv'.format(path, raw_today, hour))
        if temp_df is None:
            imps_df = vaex.read_csv(file_path, header=None)
            imps_df_cols = imps_df.column_names
            for i in range(len(header)):
                imps_df.rename(imps_df_cols[i], header[i], unique=True)
            select_imps_df = imps_df[process_select].groupby(
                by=process_group_by,
                agg=cp_dict_agg
            )
            temp_df = select_imps_df
        else:
            imps_df = temp_df

            select_imps_df = imps_df[process_select].groupby(
                by=process_group_by,
                agg=cp_dict_agg
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


def do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header, campaign=False):
    try:
        raw_today = today.strftime('%Y%m%d')
        filter_today = today.strftime('%Y-%m-%d')
        for hour in list_processing_hour:
            logger.info("PROCESSING HOUR %s" % hour)
            if campaign:
                do_agg_campaign(folder_path, path, server_host, header, raw_today, filter_today, hour)
            for item in list_config:
                logger.info("PROCESSING TABLE %s" % item)
                table_name, process_select, process_group_by = processing_config(item)

                file_path = os.path.join(folder_path, path, raw_today,
                                         '{}_{}_{}.csv'.format(path, raw_today, hour))
                logger.info(file_path)
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


def thisstart(folder_path, path, list_processing_hour, server_host, list_config, header, is_last_hour, is_day, is_yesterday,
          is_crontab, custom_date, campaign=False):
    today = None
    if is_last_hour:
        logger.info('PROCESS COLLECTING LAST HOUR')
        today = get_current_date_hour()
        logger.info("==================== %s" % today)
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
        logger.info("YESTERDAY DATE %s" % today)
        for hour in range(0, 24):
            formated_hour = f"{hour:02d}"
            list_processing_hour.append(formated_hour)
    elif is_crontab:
        logger.info('PROCESS COLLECTING CRONTAB MODE')
        ct = get_current_date_hour()
        processing_datetime = ct - timedelta(hours=1)
        list_processing_hour.append(processing_datetime.hour)
        today = processing_datetime.today()
    elif custom_date is not None:
        today = datetime.strptime(custom_date, '%Y-%m-%d')
        logger.info("CUSTOM DATE %s" % today)
        for hour in range(0, 24):
            formated_hour = f"{hour:02d}"
            list_processing_hour.append(formated_hour)
    if is_crontab or is_last_hour or is_day or is_yesterday or custom_date is not None:
        do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header, campaign)
    else:
        while True:
            list_processing_hour = []
            today = get_current_date_hour()
            list_processing_hour.append(f"{today.hour:02d}")
            do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header, campaign)
            time.sleep(60)
