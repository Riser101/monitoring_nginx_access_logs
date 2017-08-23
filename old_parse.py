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
        required_log_timestamp = now - dt.timedelta(seconds = parse_logs_back_untill)
    else:	
        required_log_timestamp = now - dt.timedelta(minutes = parse_logs_back_untill)
    
    with open(access_log) as fin:
        for line in fin:
            m = rg.search(line)
            if m:
                logged_datetime = m.group(1)
                logged_datetime = str(logged_datetime.translate(None, '[]'))
	       # print '######## ' + logged_datetime 
		if consider_time_in == 'secs':
                    formatted_logged_time = dt.datetime.strptime(logged_datetime, '%d/%b/%Y:%I:%M:%S +0000')
                    print '######' + str(logged_datetime)
		else : 
		    formatted_logged_time = dt.datetime.strptime(logged_datetime, '%d/%b/%Y:%I:%M +0000')
	  
               	
               # print type(formatted_logged_time) + 'calculated tie: ' + required_log_timestamp

            else :
	        print 'error, the date could not be parsed.'   

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()

    main(args)
