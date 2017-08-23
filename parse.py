import os
import datetime as dt
import re

def main(cmd_params):
    print cmd_params
    consider_time_in = cmd_params[0]
    parse_logs_back_untill = int(cmd_params[1])
    now = dt.datetime.utcnow()
    access_log = os.path.abspath(os.path.expanduser(os.environ.get('access_log', '/var/log/nginx/access.log')))

    re1='.*?'
    re2='(\\[.*?\\])'
    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)

    if consider_time_in == 'secs':
        timestamp_to_match_aganist = now - dt.timedelta(seconds = parse_logs_back_untill)
    else:
        timestamp_to_match_aganist = now - dt.timedelta(minutes = parse_logs_back_untill)

    with open(access_log) as fin:
        for line in fin:
            regex_match = rg.search(line)
            if regex_match:
                timestamp_from_logfile = regex_match.group(1)
                timestamp_from_logfile = str(timestamp_from_logfile.translate(None, '[]'))
                if consider_time_in == 'secs':
                    timestamp_from_logfile_formatted = dt.datetime.strptime(timestamp_from_logfile, '%d/%b/%Y:%I:%M:%S +0000')
                    print timestamp_from_logfile_formatted
                else :
                    timestamp_from_logfile_formatted = dt.datetime.strptime(timestamp_from_logfile, '%d/%b/%Y:%I:%M +0000')
            else :
                print 'error, the date could not be parsed.'

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()

    main(args)
