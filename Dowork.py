import os

import requests
import json
import urllib.parse


#http://api.zhuishushenqi.com/ranking/54d42d92321052167dfb75e3
from spidderbooktool import spidderUtils
from spidderbooktool import sqlliteconnect
#追书完结版url
r=requests.get("http://api.zhuishushenqi.com/ranking/564eea0b731ade4d6c509493")
responsetxt=r.text
jsonobj=json.loads(responsetxt)
books=jsonobj['ranking']['books']
i=0
for book  in books:
 if(i>20):
  spidderUtils.saveBookfromResouRank(book)
 i=i+1;

