__author__ = 'ITRI'
# coding=utf-8

import urllib2
import mechanize
import time

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# Turn on debugging messages
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")]


br.open('https://login.yahoo.com/')
#br.open('http://auderio.com/')
#print(openpage.read())
br.select_form(nr=0)
print('start')
for field_name in br.form.controls:
    print field_name
#br.form['username'] = 'lalalala'
#br.form['passwd'] = 'llla2'
#br.form.find_control(id='inputs').__setattr__('value', 'https://www.youtube.com/watch?v=g4FMAgeVV_w')

#br.submit()
aaa = br.response().read()
bbb = br.response().get_data()
print(bbb)
for link in br.links():
    print(link)

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

'''
url = "http://auderio.com/download?url=https://www.youtube.com/watch?v=g4FMAgeVV_w"
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
'''