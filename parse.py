import os
import datetime as dt 

def main(parse_logs_back_untill_in_secs):
	 parse_logs_back_untill_in_secs = int(parse_logs_back_untill_in_secs[0])
	 now = dt.datetime.utcnow()
	 logs_date = now - dt.timedelta(seconds = parse_logs_back_untill_in_secs)
	 print logs_date 

if __name__ == '__main__':
	from optparse import OptionParser
	parser = OptionParser()
        (options, args) = parser.parse_args()	
		
	main(args)
