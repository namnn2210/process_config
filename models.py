from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, BIGINT, Float
from datetime import datetime

Base = declarative_base()


class StatsAdsDeviceByNodeHour(Base):
    __tablename__ = "stats_ads_device_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsHourByNodeHour(Base):
    __tablename__ = "stats_ads_hour_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsLocationByNodeHour(Base):
    __tablename__ = "stats_ads_location_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    location1 = Column(Integer, default=0)
    location2 = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsPerformanceByNodeHour(Base):
    __tablename__ = "stats_ads_performance_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    domain_id = Column(Integer, default=0)
    campaign_id = Column(Integer, default=0)
    location1 = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    updated_time = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsBrowserByNodeHour(Base):
    __tablename__ = "stats_ads_tags_browser_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    browser = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsCampaignByNodeHour(Base):
    __tablename__ = "stats_ads_tags_campaign_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ad_id = Column(Integer, default=0)
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    campaign_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsDateByNodeHour(Base):

    __tablename__ = "stats_ads_tags_date_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ad_id = Column(Integer, default=0)
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    source_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsDeviceByNodeHour(Base):
    __tablename__ = "stats_ads_tags_device_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    ad_id = Column(Integer, default=0)
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    source_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsLocationByNodeHour(Base):
    __tablename__ = "stats_ads_tags_location_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    location1 = Column(Integer, default=0)
    location2 = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsAdsTagsPositionByNodeHour(Base):
    __tablename__ = "stats_ads_tags_position_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    ad_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    position = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsCampaignByNodeHour(Base):
    __tablename__ = "stats_campaigns_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    campaign_id = Column(Integer, default=0)
    count_ads = Column(Integer, default=0)
    imps = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsCampaignsIndicatorByNodeHour(Base):
    __tablename__ = "stats_campaigns_indicator_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    campaign_id = Column(Integer, default=0)
    imps = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsEventByNodeHour(Base):
    __tablename__ = "stats_event_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    campaign_id = Column(Integer, default=0)
    imps = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsBrowserByNodeHour(Base):
    __tablename__ = "stats_tags_browser_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    tag_id = Column(Integer, default=0)
    browser = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    request = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsChangeByNodeHour(Base):
    __tablename__ = "stats_tags_change_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    tag_id = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    request = Column(Integer, default=0)
    click = Column(Integer, default=0)
    type = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsDateByNodeHour(Base):
    __tablename__ = "stats_tags_date_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    source_id = Column(Integer, default=0)
    tag_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    request = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    ctr = Column(Float, default=0.0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsDeviceByNodeHour(Base):
    __tablename__ = "stats_tags_device_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    tag_id = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    request = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsInventoriesByNodeHour(Base):
    __tablename__ = "stats_tags_inventories_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    tag_id = Column(Integer, default=0)
    did = Column(Integer, default=0)
    location1 = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    request = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    tier = Column(Integer, default=0)
    updated_time = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsTagsLocationByNodeHour(Base):
    __tablename__ = "stats_tags_location_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    tag_id = Column(Integer, default=0)
    location1 = Column(Integer, default=0)
    location2 = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    request = Column(Integer, default=0)
    paid = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    spent_cpm = Column(Integer, default=0)
    click_landing = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent_cpc_landing = Column(Integer, default=0)
    click_raw = Column(Integer, default=0)
    spent_cpc_raw = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    rev_opt = Column(Integer, default=0)
    rev_real = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)


class StatsUsersByNodeHour(Base):
    __tablename__ = "stats_users_by_node_hour"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    user_id = Column(Integer, default=0)
    imp = Column(Integer, default=0)
    click = Column(Integer, default=0)
    spent = Column(Integer, default=0)
    payment = Column(Integer, default=0)
    balance = Column(BIGINT, default=0)
    created_time = Column(Integer, default=0)
    updated_time = Column(Integer, default=0)
    server_host = Column(String, default='')
    hour = Column(Integer, default=0)
