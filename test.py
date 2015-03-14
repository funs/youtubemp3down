__author__ = 'ITRI'
# coding=utf-8

import urllib2
import mechanize
import time

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_debug_http(True)
br.set_debug_responses(True)
br.set_debug_redirects(True)
br.addheaders = [('User-agent', 'Mozilla/5.0')]
'''
br.open('https://www.google.com.tw/')


for f in br.forms():
    print f

br.select_form('f')
br.form['q'] = 'line app'

br.submit()

aaa = br.response().read()
hhtml = br.response().get_data()
print(aaa)

for link in br.links():
    print(link)
'''

br.open('https://savedeo.com/en')
#br.open('http://auderio.com/')
br.select_form(nr=0)
br.form['url'] = 'https://www.youtube.com/watch?v=g4FMAgeVV_w'
print("")
#br.form.find_control(id='youtube-url').__setattr__('value', 'https://www.youtube.com/watch?v=g4FMAgeVV_w')

br.submit()
aaa = br.response().read()
bbb = br.response().get_data()
print(bbb)
for link in br.links():
    print(link)

'''
url = "http://auderio.com/download?url=https://www.youtube.com/watch?v=g4FMAgeVV_w"
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
'''