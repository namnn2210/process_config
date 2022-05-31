from utils.utils import do_agg
import time


def process(folder_path, path, today, list_processing_hour, server_host, list_config, header):
    while True:
        do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header)
        time.sleep(120)
