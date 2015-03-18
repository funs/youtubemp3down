__author__ = 'ITRI'
# coding=utf-8

import urllib
import urllib2
import requests
from pprint import pprint

uri = 'https://tw.yahoo.com/'
# Prepare the data
values = {'p':'柯文哲'}
data = urllib.urlencode(values)
headers = {'User-agent':'Mozilla/11.0'}

request = urllib2.Request(uri, data=data, headers=headers)
response = urllib2.urlopen(request)

html = response.read()
'''

response = requests.post(uri,data=data,headers=headers)
html = response.content
'''
print(html)