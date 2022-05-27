from utils import do_agg


def process(folder_path, path, today, list_processing_hour, server_host, list_config, header):
    do_agg(folder_path, path, today, list_processing_hour, server_host, list_config, header)
