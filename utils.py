import models
from datetime import datetime


def get_last_hour():
    return datetime.now().hour - 1


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
