#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=105.235.111.251%20-%20-%20[24/Aug/2017:10:27:44%20%2b0000]%20%20%22GET%20/http-v4/css/httpFront-v4.css%20HTTP/1.1%22%20TLSv1.2%20%22ECDHE-RSA-AES256-GCM-SHA384%22%20200%202933%20%22https://www.leptidigital.fr/reseaux-sociaux/telecharger-video-facebook-6847/%22%20%22Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/60.0.3112.101%20Safari/537.36%22%200.000%20-%20.&-84

import re

txt='105.235.111.251 - - [24/Aug/2017:10:27:44 +0000]  "GET /http-v4/css/httpFront-v4.css HTTP/1.1" TLSv1.2 "ECDHE-RSA-AES256-GCM-SHA384" 200 2933 "https://www.leptidigital.fr/reseaux-sociaux/telecharger-video-facebook-6847/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36" 0.000 - .'

re1='.*?(200)'    # Integer Number 1

rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
        int1=m.group(1)
        print "("+int1+")"+"\n"
