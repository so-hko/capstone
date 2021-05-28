# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import requests


item_name='타이레놀정160밀리그람(아세트아미노펜)'

def pillAPI(item_name):
    url = 'http://apis.data.go.kr/1470000/MdcinGrnIdntfcInfoService/getMdcinGrnIdntfcInfoList'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'q3YoHJj25q60Vbzcmp+u99wHliPWRY+PSgSqZYfTjpBIpg+LTIAR/XBuk56T1BXJC0G9qKOAah4S78mOHm+BJA==', quote_plus('item_name') : item_name})

    payload={'key1':'value1','key2':'value2'}
    res=requests.get(url+queryParams,params=payload)
    print(res.text)
    return res.text


pillAPI(item_name)
