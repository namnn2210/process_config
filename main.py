from datetime import datetime
import os
import adsapp, campaignapp, requestapp

today = datetime.today().strftime('%Y%m%d')
hour = datetime.now().hour

imps_path = 'imps'
clicks_path = 'clicks'
requests_path = 'request'

if __name__ == '__main__':

    action_name = 'ad-tag-device'

    # Read file by hour
    imps_file_path = os.path.join(imps_path, '{}_{}_{}'.format(imps_path, today, hour))
    clicks_file_path = os.path.join(clicks_path, '{}_{}_{}'.format(clicks_path, today, hour))
    requests_file_path = os.path.join(requests_path, '{}_{}_{}'.format(requests_path, today, hour))

    adsapp.do_agg(imps_file_path, clicks_file_path, action_name, hour)
