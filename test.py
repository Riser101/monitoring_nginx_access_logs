#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=104.37.84.4%20-%20-%20[24/Aug/2017:06:51:47%20%2b0000]%20%20%22POST%20/api/v1/segments/23434/subscribers?page=1%26per_page=2%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20500%20102%20%22-%22%20%22-%22%200.697%200.697%20.&31

import re

txt='104.37.84.4 - - [24/Aug/2017:06:51:47 +0000]  "DELETE /api/v1/segments/23434/subscribers HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 500 102 "-" "-" 0.697 0.697 .'

re1='.*?(?:[a-z][a-z]+).*?((?:[a-z][a-z]+))'

#rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
#m = rg.search(txt)
m = re.search(re1, txt)
if m:
    word1=m.group(1)
    print "("+word1+")"+"\n"

            #-----
            # Paste the code into a new python file. Then in Unix:'
            # $ python x.py 
            #-----
