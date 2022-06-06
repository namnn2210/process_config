from utils.utils import start


def process(folder_path, path, list_processing_hour, server_host, list_config, header, is_last_hour, is_day,
            is_yesterday,
            is_crontab, campaign):
    start(folder_path, path, list_processing_hour, server_host, list_config, header, is_last_hour, is_day, is_yesterday,
          is_crontab, campaign)
