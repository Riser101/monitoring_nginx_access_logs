#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=103.17.16.46%20-%20-%20[17/Aug/2017:06:29:05%20%2b0000]%20%20%22GET%20/assets/images/modal-branding.png%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20200%201128%20%22http://ronandlisa.com/2013/10/22/5-sustainable-countertops-granite/%22%20%22Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_12_6)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/60.0.3112.90%20Safari/537.36%22%200.000%20-%20.&12

import re

txt='103.17.16.46 - - [17/Aug/2017:06:29:05 +0000]  "GET /assets/images/modal-branding.png HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 1128 "http://ronandlisa.com/2013/10/22/5-sustainable-countertops-granite/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36" 0.000 - .'

log_list = ['103.17.16.46 - - [17/Aug/2017:06:29:05 +0000]  "GET /assets/images/modal-branding.png HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 1128 "http://ronandlisa.com/2013/10/22/5-sustainable-countertops-granite/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36" 0.000 - .', '103.17.16.46 - - [23/Jun/2012:03:23:05 +0000]  "GET /assets/images/modal-branding.png HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 1128 "http://ronandlisa.com/2013/10/22/5-sustainable-countertops-granite/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36" 0.000 - .']



re1='.*?'    # Non-greedy match on filler
re2='((?:(?:[0-2]?\\d{1})|(?:[3][01]{1}))[-:\\/.](?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[-:\\/.](?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])'    # DDMMMYYYY 1

rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)

for item in log_list:
    m = rg.search(item)
    if m:
        ddmmmyyyy1=m.group(1)
        print "("+ddmmmyyyy1+")"+"\n"

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----
