#!/usr/bin/env python
from pyquery import PyQuery as pq
import requests as r
import sys
import os

url = 'http://dict.youdao.com/fsearch?q=%s'

try:
    html = r.get(url % os.sys.argv[1]).content
    d = pq(html)
    if not len([sys.stdout.write(v.text + '\n') for v in d('phonetic-symbol,content')]):
        print("can't find word")
except:
    print("you need input word")
