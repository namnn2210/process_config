from datetime import datetime
import os
import adsapp, campaignapp, requestapp
import argparse

today = datetime.today().strftime('%Y%m%d')
hour = datetime.now().hour

imps_path = 'imps'
clicks_path = 'clicks'
requests_path = 'request'


def create_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--folderpath', required=True,
                    help='Folder path')
    args = vars(ap.parse_args())
    return args


if __name__ == '__main__':
    args = create_args()
    # Read file by hour
    imps_file_path = os.path.join(args['folderpath'], imps_path, '{}_{}_{}'.format(imps_path, today, hour))
    # clicks_file_path = os.path.join(clicks_path, '{}_{}_{}'.format(clicks_path, today, hour))
    # requests_file_path = os.path.join(requests_path, '{}_{}_{}'.format(requests_path, today, hour))

    adsapp.do_agg(imps_file_path, hour)
