#!/usr/bin/python
# encoding=utf-8

"""
Easy to git clone the stars of somebody to local backup.
By @evilcos
"""

import os
import sys
import json
import requests
import multiprocessing as mul

star_urls = []

def get_star_urls(url, page=1):
    url = url%page
    r = requests.get(url)
    c = r.content
    j = json.loads(c)
    for i in j:
        #print(i.get('html_url'))
        star_urls.append(i.get('html_url'))
    if len(j) == 30:
        get_star_urls(entry, page+1)

def clone(url):
    cmd = 'git clone %s'%url
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    try:
        username = sys.argv[1]
    except:
        print('Plz enter the username which you want to git clone his stars. For example:\n\
in this stars url: https://github.com/evilcos?tab=stars, evilcos is the username.')
        sys.exit(0)
    entry = 'https://api.github.com/users/' + username + '/starred?page=%s'
    get_star_urls(entry)
    print('%s stars'%len(star_urls))
    pool = mul.Pool(10)
    pool.map(clone, star_urls)

