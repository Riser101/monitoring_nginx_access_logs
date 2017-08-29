#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=104.37.84.4%20-%20-%20[24/Aug/2017:06:51:47%20%2b0000]%20%20%22POST%20/api/v1/send/all%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20200%20102%20%22-%22%20%22-%22%200.697%200.697%20.&40

import re

txt='104.37.84.4 - - [24/Aug/2017:06:51:47 +0000]  "POST /api/v1/send/all HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 102 "-" "-" 0.23111111 0.8888888888 .'

re1='.*?'    # Non-greedy match on filler
re2='\\d+'    # Uninteresting: int
re3='.*?'    # Non-greedy match on filler
re4='\\d+'    # Uninteresting: int
re5='.*?'    # Non-greedy match on filler
re6='\\d+'    # Uninteresting: int
re7='.*?'    # Non-greedy match on filler
re8='\\d+'    # Uninteresting: int
re9='.*?'    # Non-greedy match on filler
re10='\\d+'    # Uninteresting: int
re11='.*?'    # Non-greedy match on filler
re12='\\d+'    # Uninteresting: int
re13='.*?'    # Non-greedy match on filler
re14='\\d+'    # Uninteresting: int
re15='.*?'    # Non-greedy match on filler
re16='\\d+'    # Uninteresting: int
re17='.*?'    # Non-greedy match on filler
re18='\\d+'    # Uninteresting: int
re19='.*?'    # Non-greedy match on filler
re20='\\d+'    # Uninteresting: int
re21='.*?'    # Non-greedy match on filler
re22='\\d+'    # Uninteresting: int
re23='.*?'    # Non-greedy match on filler
re24='\\d+'    # Uninteresting: int
re25='.*?'    # Non-greedy match on filler
re26='\\d+'    # Uninteresting: int
re27='.*?'    # Non-greedy match on filler
re28='\\d+'    # Uninteresting: int
re29='.*?'    # Non-greedy match on filler
re30='\\d+'    # Uninteresting: int
re31='.*?'    # Non-greedy match on filler
re32='\\d+'    # Uninteresting: int
re33='.*?'    # Non-greedy match on filler
re34='\\d+'    # Uninteresting: int
re35='.*?'    # Non-greedy match on filler
re36='\\d+'    # Uninteresting: int
re37='.*?'    # Non-greedy match on filler
re38='\\d+'    # Uninteresting: int
re39='.*?'    # Non-greedy match on filler
re40='\\d+'    # Uninteresting: int
re41='.*?'    # Non-greedy match on filler
re42='\\d+'    # Uninteresting: int
re43='.*?'    # Non-greedy match on filler
re44='\\d+'    # Uninteresting: int
re45='.*?'    # Non-greedy match on filler
re46='(\\d+)'    # Integer Number 1

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25+re26+re27+re28+re29+re30+re31+re32+re33+re34+re35+re36+re37+re38+re39+re40+re41+re42+re43+re44+re45+re46,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
        int1=m.group(1)
        print "("+int1+")"+"\n"

            #-----
            # Paste the code into a new python file. Then in Unix:'
            # $ python x.py 
            #-----
