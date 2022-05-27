from datetime import datetime
import adsapp, campaignapp, requestapp
import argparse
from loguru import logger
from utils import get_last_hour
from json_config.imps_config import IMPS_CONFIG
from json_config.clicks_config import CLICKS_CONFIG
from config import IMPS_CLICK_HEADER, REQUESTS_HEADER

today = datetime.today().strftime('%Y%m%d')

imps_path = 'imps'
clicks_path = 'clicks'
requests_path = 'request'


def create_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--folder_path', required=True,
                    help='Folder path')
    ap.add_argument('-s', '--server_host', required=True, help='Server Host')
    ap.add_argument('-lh', '--last_hour', default=False, action='store_true', help='Last hour')
    ap.add_argument('-d', '--day', default=False, action='store_true', help='Beginning of the day')

    args = ap.parse_args()
    return args


if __name__ == '__main__':
    args = create_args()
    list_processing_hour = []
    if args.last_hour and args.day:
        logger.info('CHOOSE ONLY PROCESSING BY LAST HOUR OR BEGINNING OF THE DAY')
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
        # Read file by hour
        # requests_file_path = os.path.join(requests_path, '{}_{}_{}'.format(requests_path, today, hour))

        adsapp.process(args.folder_path, imps_path, today, list_processing_hour, args.server_host, IMPS_CONFIG,
                       IMPS_CLICK_HEADER)
        adsapp.process(args.folder_path, clicks_path, today, list_processing_hour, args.server_host, CLICKS_CONFIG,
                       IMPS_CLICK_HEADER)
