#!/usr/bin/env python
import requests as r
from pyquery import PyQuery as pq
import os

url = 'http://dict.youdao.com/fsearch?q=%s'

try:
    html = r.get(url % os.sys.argv[1]).content
    d = pq(html)
    if not len([print(v.text) for v in d('content')]):
        print("can't find word")
except:
    print("you need input word")
