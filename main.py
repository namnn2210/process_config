from process import imps_click_process, request_process
import argparse
from loguru import logger
from config.imps_config import IMPS_CONFIG
from config.clicks_config import CLICKS_CONFIG
from config.request_config import REQUESTS_CONFIG
from config.general_config import IMPS_CLICK_HEADER, REQUESTS_HEADER

imps_path = 'imps'
clicks_path = 'clicks'
requests_path = 'requests'


def create_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--folder_path', required=True,
                    help='Folder path')
    ap.add_argument('-s', '--server_host', required=True, help='Server Host')
    ap.add_argument('-l', '--last_hour', default=False, action='store_true', help='Last hour')
    ap.add_argument('-d', '--day', default=False, action='store_true', help='Beginning of the day')
    ap.add_argument('-y', '--yesterday', default=False, action='store_true', help='Yesterday')
    ap.add_argument('-cr', '--crontab', default=False, action='store_true', help='Crontab mode')
    ap.add_argument('-i', '--imps', default=False, action='store_true', help='Imps mode')
    ap.add_argument('-c', '--clicks', default=False, action='store_true', help='Clicks mode')
    ap.add_argument('-r', '--requests', default=False, action='store_true', help='Requests mode')

    args = ap.parse_args()
    return args


if __name__ == '__main__':
    args = create_args()
    list_processing_hour = []
    if args.last_hour and args.day and args.yesterday and args.crontab:
        logger.info('CHOOSE ONLY ONE PROCESSING')
    else:
        if (args.imps and args.clicks and args.requests) or (args.imps and args.clicks) or (
                args.imps and args.requests) or (args.clicks and args.requests):
            logger.info('CHOOSE ONLY ONE MODE: IMPS, CLICKS, REQUESTS')
        else:
            if args.imps:
                imps_click_process.process(args.folder_path, imps_path, list_processing_hour, args.server_host,
                                           IMPS_CONFIG,
                                           IMPS_CLICK_HEADER, args.last_hour, args.day, args.yesterday, args.crontab,
                                           campaign=True)
            elif args.clicks:
                imps_click_process.process(args.folder_path, clicks_path, list_processing_hour, args.server_host,
                                           CLICKS_CONFIG,
                                           IMPS_CLICK_HEADER, args.last_hour, args.day, args.yesterday, args.crontab)
            elif args.requests:
                request_process.process(args.folder_path, requests_path, list_processing_hour, args.server_host,
                                        REQUESTS_CONFIG,
                                        REQUESTS_HEADER, args.last_hour, args.day, args.yesterday, args.crontab)
            else:
                logger.info('NO MODE CHOSEN')
