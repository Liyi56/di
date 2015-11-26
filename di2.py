#!/usr/bin/env python
from pyquery import PyQuery as pq
from pprint import pprint
import requests as r
import uniout
import os

url = 'http://dict.youdao.com/fsearch?q=%s'

try:
    html = r.get(url % os.sys.argv[1]).content
    d = pq(html)
    if not len([pprint(v.text) for v in d('content')]):
        print("can't find word")
except:
    print("you need input word")
