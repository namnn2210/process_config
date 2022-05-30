from datetime import datetime
from process import imps_click_process, request_process
import argparse
from loguru import logger
from utils.utils import get_last_hour
from config.imps_config import IMPS_CONFIG
from config.clicks_config import CLICKS_CONFIG
from config.request_config import REQUESTS_CONFIG
from config.general_config import IMPS_CLICK_HEADER, REQUESTS_HEADER

today = datetime.today().strftime('%Y%m%d')

imps_path = 'imps'
clicks_path = 'clicks'
requests_path = 'request'


def create_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--folder_path', required=True,
                    help='Folder path')
    ap.add_argument('-s', '--server_host', required=True, help='Server Host')
    ap.add_argument('-l', '--last_hour', default=False, action='store_true', help='Last hour')
    ap.add_argument('-d', '--day', default=False, action='store_true', help='Beginning of the day')
    ap.add_argument('-i', '--imps', default=False, action='store_true', help='Imps mode')
    ap.add_argument('-c', '--clicks', default=False, action='store_true', help='Clicks mode')
    ap.add_argument('-r', '--requests', default=False, action='store_true', help='Requests mode')

    args = ap.parse_args()
    return args


if __name__ == '__main__':
    args = create_args()
    list_processing_hour = []
    if args.last_hour and args.day:
        logger.info('CHOOSE ONLY ONE PROCESSING BY LAST HOUR OR BEGINNING OF THE DAY')
    else:
        if args.last_hour:
            logger.info('PROCESS COLLECTING LAST HOUR')
            last_hour = f"{get_last_hour():02d}"
            list_processing_hour.append(last_hour)
        elif args.day:
            logger.info('PROCESS COLLECTING FROM BEGINNING OF THE DAY')
            for hour in range(datetime.now().hour):
                formated_hour = f"{hour:02d}"
                list_processing_hour.append(formated_hour)
        else:
            list_processing_hour.append(f"{datetime.now().hour:02d}")
        if (args.imps and args.clicks and args.requests) or (args.imps and args.clicks) or (args.imps and args.requests) or (args.clicks and args.requests):
            logger.info('CHOOSE ONLY ONE MODE: IMPS, CLICKS, REQUESTS')
        else:
            if args.imps:
                imps_click_process.process(args.folder_path, imps_path, today, list_processing_hour, args.server_host,
                                           IMPS_CONFIG,
                                           IMPS_CLICK_HEADER)
            elif args.clicks:
                imps_click_process.process(args.folder_path, clicks_path, today, list_processing_hour, args.server_host,
                                           CLICKS_CONFIG,
                                           IMPS_CLICK_HEADER)
            elif args.requests:
                request_process.process(args.folder_path, requests_path, today, list_processing_hour, args.server_host,
                                        REQUESTS_CONFIG,
                                        REQUESTS_HEADER)
            else:
                logger.info('NO MODE CHOSEN')
