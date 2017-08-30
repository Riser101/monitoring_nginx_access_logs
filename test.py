#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=127.0.0.1%20-%20-%20[30/Aug/2017:11:59:16%20%2b0000]%20%20%22POST%20/api/v1/segments/148130/subscribers%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20200%2020%20%22-%22%20%22-%22%200.095%200.095%20.&2

import re

txt='127.0.0.1 - - [30/Aug/2017:11:59:16 +0000]  "POST /api/v1/segments/148130/subscribers HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 20 "-" "-" 0.095 0.095 .'

re1='.*?'    # Non-greedy match on filler
re2='(?:\\/[\\w\\.\\-]+)+'    # Uninteresting: unixpath
re3='.*?'    # Non-greedy match on filler
re4='((?:\\/[\\w\\.\\-]+)+)'    # Unix Path 1

rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    unixpath1=m.group(1)
    print "("+unixpath1+")"+"\n"

            #-----
            # Paste the code into a new python file. Then in Unix:'
            # $ python x.py 
            #-----

