#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=104.37.84.4%20-%20-%20[24/Aug/2017:06:51:47%20%2b0000]%20%20%22POST%20/api/v1/send/all%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20200%20102%20%22-%22%20%22-%22%200.697%200.697%20.&40

import re

txt='104.37.84.4 - - [24/Aug/2017:06:51:47 +0000]  "POST /api/v1/send/all HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 102 "-" "-" 0.23111111 0.899988998988 .'

re1='.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?\\d+.*?(\\d+)'    

rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
            int1=m.group(1)
            print "("+int1+")"+"\n"

                                #-----
                                            # Paste the code into a new python file. Then in Unix:'
                                                        # $ python x.py
                                                                    #-----

