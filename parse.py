import os
import datetime as dt
import re
from datadog import initialize, api
import time

api_path = ''
send_all_total_calls = send_all_response_200 = send_all_response_400 = send_all_response_500 = 0
send_all_response_time_list = []

rss_total_calls = rss_api_response_200 = rss_api_response_400 = rss_api_response_500 = 0
rss_api_response_time_list = []

send_to_segment_total_calls = send_to_segment_response_200 = send_to_segment_response_400 = send_to_segment_response_500 = 0
send_to_segment_resp_time_list = []

send_to_list_total_calls = send_to_list_response_200 = send_to_list_response_400 = send_to_list_response_500 = 0
send_to_list_resp_time_list = []

send_to_individual_total_calls = send_to_individual_response_200 = send_to_individual_response_400 = send_to_individual_response_500 = 0
send_to_individual_resp_time_list = []

segments_api_total_calls = segments_api_response_200 = segments_api_response_400 = segments_api_response_500 = 0
segments_api_resp_time_list = []

get_seg_for_subs_total_calls = get_seg_for_subs_response_200 = get_seg_for_subs_response_400 = get_seg_for_subs_response_500 = 0
get_seg_for_subs_resp_time_list = []

regex_for_200='.*?(200)'
regex_match_for_response_200 = re.compile(regex_for_200,re.IGNORECASE|re.DOTALL)
regex_for_400='.*?(400)'
regex_match_for_response_400 = re.compile(regex_for_400,re.IGNORECASE|re.DOTALL)
regex_for_500='.*?(500)'
regex_match_for_response_500 = re.compile(regex_for_500,re.IGNORECASE|re.DOTALL)
regex_for_response_time = '.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?(\\d+)'
regex_match_for_response_time = re.compile(regex_for_response_time, re.IGNORECASE|re.DOTALL)

### this is the main method ###
def main(cmd_params):
    consider_time_in = cmd_params[0]
    parse_logs_back_untill = int(cmd_params[1])
    now = dt.datetime.utcnow().replace(microsecond=0)

    access_log = os.path.abspath(os.path.expanduser(os.environ.get('access_log', '/var/log/nginx/access.log')))

    regex_for_timestamp='.*?(\\[.*?\\])'
    regex_match_for_timestamp = re.compile(regex_for_timestamp,re.IGNORECASE|re.DOTALL)

    # pulls log entries for this timestamp
    timestamp_to_match_aganist = now - dt.timedelta(seconds = parse_logs_back_untill)

    with open(access_log) as fin:
        for line in fin:
            regex_match = regex_match_for_timestamp.search(line)
            if regex_match:

                timestamp_from_logfile = regex_match.group(1)
                timestamp_from_logfile = str(timestamp_from_logfile.translate(None, '[]'))
                timestamp_from_logfile_formatted = dt.datetime.strptime(timestamp_from_logfile, '%d/%b/%Y:%I:%M:%S +0000')

                if timestamp_to_match_aganist == timestamp_from_logfile_formatted:
                    print 'found it'
                    file_handle = open(timestamp_to_match_aganist+'.log', 'w+')
                    file_handle.write(line)
                else:
                    None
            else :
                print 'error, the date could not be parsed.'
        fin.close()

    regex_for_api_path1='.*?'
    regex_for_api_path2='(?:\\/[\\w\\.\\-]+)+'
    regex_for_api_path3='.*?'
    regex_for_api_path4='((?:\\/[\\w\\.\\-]+)+)'

    regex_match_for_apipath = re.compile(regex_for_api_path1+regex_for_api_path2+regex_for_api_path3+regex_for_api_path4,re.IGNORECASE|re.DOTALL)

    ## remove this
    timestamp_to_match_aganist = '2017-08-23 12:54:47'
    ##

    options = {'api_key': '43edd51e5bec66d97f5c46e838260ede'}
    initialize(**options)

    api_path_dict = {
        '/api/v1/send/all' : send_all,
        '/api/v1/toPush' : rss,
        '/api/v1/send/segment' : send_to_segment,
        '/api/v1/send/list': send_to_list,
        '/api/v1/send/individual' : send_to_indvidual,
        '/api/v1/segments' : segments_api,
        '/api/v1/subscribers' : get_segments_for_subscriber
    }

    with open(str(timestamp_to_match_aganist)+'.log') as read_handle:
        #this loops over every entry in new log file
        for line in read_handle:

           regex_api_result =  regex_match_for_apipath.search(line)
           if regex_api_result:
               global api_path
               api_path = regex_api_result.group(1)
               api_path_dict[api_path](line)
        
        print send_all_response_200
        print send_all_total_calls
        print send_all_response_400
        print send_all_response_500

        send_all_mean_response_time = sum(send_all_response_time_list)/len(send_all_response_time_list)
        rss_api_mean_response_time = sum(rss_api_response_time_list)/len(rss_api_response_time_list)
        rss_api_mean_response_time = sum(rss_api_response_time_list)/len(rss_api_response_time_list)
        send_to_segment_mean_resp_time = sum(send_to_segment_resp_time_list)/len(send_to_segment_resp_time_list)
        send_to_list_mean_resp_time = sum(send_to_list_resp_time_list)/len(send_to_list_resp_time_list)
        send_to_individual_mean_resp_time = sum(send_to_individual_resp_time_list)/len(send_to_individual_resp_time_list)
        segments_api_mean_resp_time = sum(segments_api_resp_time_list)/len(segments_api_resp_time_list)
        get_seg_for_subs_mean_resp_time = sum(get_seg_for_subs_resp_time_list)/len(get_seg_for_subs_resp_time_list)

        print send_all_mean_response_time 
        print rss_api_mean_response_time 
        print rss_api_mean_response_time 
        print send_to_segment_mean_resp_time 
        print send_to_list_mean_resp_time 
        print send_to_individual_mean_resp_time 
        print segments_api_mean_resp_time 
        print get_seg_for_subs_mean_resp_time 
        
        
        api.Metric.send([{'metric':'send_all_total_calls', 'points':send_all_total_calls}, {'metric':'send_all_response_200', 'points':send_all_response_200}, {'metric':'send_all_response_400',
            'points':send_all_response_400}, {'metric':'send_all_response_500', 'points':send_all_response_500}, {'metric':'send_all_mean_response_time', 'points':send_all_mean_response_time}])

def send_all(line):
    global send_all_total_calls
    send_all_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        send_all_with_response_200 = http_status_code['regex_200_result'].group(1)
        if int(send_all_with_response_200) == 200:
            global send_all_response_200
            send_all_response_200 += 1

    if http_status_code['regex_400_result']:
        send_all_with_response_400 = http_status_code['regex_400_result'].group(1)
        if int(send_all_with_response_400) == 400:
            global send_all_response_400
            send_all_response_400 += 1

    if http_status_code['regex_500_result']:
        send_all_with_response_500 = http_status_code['regex_500_result'].group(1)
        if int(send_all_with_response_500) == 500:
            global send_all_response_500
            send_all_response_500 += 1

    if http_status_code['regex_response_time_result']:
        send_all_with_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global send_all_response_time_list
        send_all_response_time_list.append(send_all_with_response_time)

def rss(line):
    global rss_total_calls
    rss_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        rss_with_response_200 = http_status_code['regex_200_result'].group(1)
        if int(rss_with_response_200) == 200:
            global rss_api_response_200
            rss_api_response_200 += 1

    if http_status_code['regex_400_result']:
        rss_with_response_400 = http_status_code['regex_400_result'].group(1)
        if int(rss_with_response_400) == 400:
            global rss_api_response_400
            rss_api_response_400 += 1

    if http_status_code['regex_500_result']:
        rss_with_response_500 = http_status_code['regex_500_result'].group(1)
        if int(rss_with_response_500) == 500:
            global rss_api_response_500
            rss_api_response_500 += 1

    if http_status_code['regex_response_time_result']:
        rss_with_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global rss_api_response_time_list
        rss_api_response_time_list.append(rss_with_response_time)

def send_to_segment(line):
    global send_to_segment_total_calls
    send_to_segment_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        status_200_from_log = http_status_code['regex_200_result'].group(1)
        if int(status_200_from_log) == 200:
            global send_to_segment_response_200
            send_to_segment_response_200 += 1

    if http_status_code['regex_400_result']:
        status_400_from_log = http_status_code['regex_400_result'].group(1)
        if int(status_400_from_log) == 400:
            global send_to_segment_response_400
            send_to_segment_response_400 += 1

    if http_status_code['regex_500_result']:
        status_500_from_log = http_status_code['regex_500_result'].group(1)
        if int(status_500_from_log) == 500:
            global send_to_segment_response_500
            send_to_segment_response_500 += 1

    if http_status_code['regex_response_time_result']:
        api_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global send_to_segment_resp_time_list
        send_to_segment_resp_time_list.append(api_response_time)     

def send_to_list(line):
    global send_to_list_total_calls
    send_to_list_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        status_200_from_log = http_status_code['regex_200_result'].group(1)
        if int(status_200_from_log) == 200:
            global send_to_list_response_200
            send_to_list_response_200 += 1

    if http_status_code['regex_400_result']:
        status_400_from_log = http_status_code['regex_400_result'].group(1)
        if int(status_400_from_log) == 400:
            global send_to_list_response_400
            send_to_list_response_400 += 1

    if http_status_code['regex_500_result']:
        status_500_from_log = http_status_code['regex_500_result'].group(1)
        if int(status_500_from_log) == 500:
            global send_to_list_response_500
            send_to_list_response_500 += 1

    if http_status_code['regex_response_time_result']:
        api_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global send_to_list_resp_time_list
        send_to_list_resp_time_list.append(api_response_time)    

def send_to_individual(line):
    global send_to_individual_total_calls
    send_to_individual_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        status_200_from_log = http_status_code['regex_200_result'].group(1)
        if int(status_200_from_log) == 200:
            global send_to_individual_response_200
            send_to_individual_response_200 += 1

    if http_status_code['regex_400_result']:
        status_400_from_log = http_status_code['regex_400_result'].group(1)
        if int(status_400_from_log) == 400:
            global send_to_individual_response_400
            send_to_individual_response_400 += 1

    if http_status_code['regex_500_result']:
        status_500_from_log = http_status_code['regex_500_result'].group(1)
        if int(status_500_from_log) == 500:
            global send_to_individual_response_500
            send_to_individual_response_500 += 1

    if http_status_code['regex_response_time_result']:
        api_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global send_to_individual_resp_time_list
        send_to_individual_resp_time_list.append(api_response_time)

def segments_api(line):
    global segments_api_total_calls
    segments_api_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        status_200_from_log = http_status_code['regex_200_result'].group(1)
        if int(status_200_from_log) == 200:
            global segments_api_response_200
            segments_api_response_200 += 1

    if http_status_code['regex_400_result']:
        status_400_from_log = http_status_code['regex_400_result'].group(1)
        if int(status_400_from_log) == 400:
            global segments_api_response_400
            segments_api_response_400 += 1

    if http_status_code['regex_500_result']:
        status_500_from_log = http_status_code['regex_500_result'].group(1)
        if int(status_500_from_log) == 500:
            global segments_api_response_500
            segments_api_response_500 += 1

    if http_status_code['regex_response_time_result']:
        api_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global segments_api_resp_time_list
        segments_api_resp_time_list.append(api_response_time)                                         

def get_segments_for_subscriber(line):
    global get_seg_for_subs_total_calls
    get_seg_for_subs_total_calls += 1
    http_status_code = parse_status_code(line)

    if http_status_code['regex_200_result']:
        status_200_from_log = http_status_code['regex_200_result'].group(1)
        if int(status_200_from_log) == 200:
            global get_seg_for_subs_response_200
            get_seg_for_subs_response_200 += 1

    if http_status_code['regex_400_result']:
        status_400_from_log = http_status_code['regex_400_result'].group(1)
        if int(status_400_from_log) == 400:
            global get_seg_for_subs_response_400
            get_seg_for_subs_response_400 += 1

    if http_status_code['regex_500_result']:
        status_500_from_log = http_status_code['regex_500_result'].group(1)
        if int(status_500_from_log) == 500:
            global get_seg_for_subs_response_500
            get_seg_for_subs_response_500 += 1

    if http_status_code['regex_response_time_result']:
        api_response_time = int(http_status_code['regex_response_time_result'].group(1))
        global get_seg_for_subs_resp_time_list
        get_seg_for_subs_resp_time_list.append(api_response_time)                                                     


def parse_status_code(line):
    return {
           'regex_200_result' : regex_match_for_response_200.search(line),
           'regex_400_result' : regex_match_for_response_400.search(line),
           'regex_500_result' : regex_match_for_response_500.search(line),
           'regex_response_time_result': regex_match_for_response_time.search(line)
    }

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()

    main(args)
