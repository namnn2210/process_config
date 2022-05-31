from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, BIGINT, Float, Text
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


class Ads(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    origin_id = Column(Integer, default=0)
    campaign_id = Column(Integer, default=0)
    name = Column(String, default='')
    kind = Column(Integer, default=0)
    size_id = Column(Integer, default=0)
    url = Column(String, default='')
    title = Column(String, default='')
    other_text = Column(Text, default='')
    image = Column(String, default='')
    image_brand_logo = Column(String, default='')
    brand_data = Column(String, default='')
    des_link = Column(String, default='')
    run_type = Column(Integer, default=0)
    cpm = Column(Float, default=0.0)
    click_price = Column(Float, default=0.0)
    usd_cpm = Column(Float, default=0.0)
    usd_click_price = Column(Float, default=0.0)
    reject_reason = Column(String, default='')
    opt_store = Column(Integer, default=0)
    status = Column(Integer, default=0)
    status_media = Column(Integer, default=0)
    status_adv = Column(Integer, default=0)
    status_adv_old = Column(Integer, default=0)
    archived_is = Column(Integer, default=0)
    created_time = Column(Integer, default=0)
    updated_time = Column(Integer, default=0)


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    domain_id = Column(Integer, default=0)
    size_id = Column(Integer, default=0)
    type = Column(Integer, default=0)
    tag_column = Column(Integer, default=0)
    tag_row = Column(Integer, default=0)
    name = Column(String, default='')
    item_number = Column(Integer, default=0)
    css = Column(Text, default='')
    passback = Column(Text, default='')
    pb_adx = Column(Text, default='')
    source_type = Column(Integer, default=0)
    source_id = Column(Integer, default=0)
    source_pb = Column(Text, default='')
    rmkt_is = Column(Integer, default=0)
    cpm = Column(Float, default=0.0)
    data = Column(Text, default='')
    volume_type = Column(Integer, default=0)
    status = Column(Integer, default=0)
    status_sys = Column(Integer, default=0)
    created_time = Column(Integer, default=0)
    updated_time = Column(Integer, default=0)


class ConversionsClick(Base):
    __tablename__ = "conversions_click"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    click_id = Column(String, default='')
    tag_id = Column(Integer, default=0)
    campaign_id = Column(Integer, default=0)
    ad_id = Column(Integer, default=0)
    date = Column(String, default=datetime.today().strftime('%Y%m%d'))
    location1 = Column(Integer, default=0)
    location2 = Column(Integer, default=0)
    device1 = Column(Integer, default=0)
    device2 = Column(Integer, default=0)
    browser = Column(Integer, default=0)
    position = Column(Integer, default=0)
    missing = Column(Integer, default=0)
    payout = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
