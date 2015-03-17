__author__ = 'ITRI'
# coding=utf8

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

br.addheaders = [('User-agent', 'Mozilla/5.0')]


br.open('https://tw.yahoo.com/')
br.select_form(nr=0)
print('start')
'''
for field_name in br.form.controls:
    print field_name
'''
br.form['p'] = 'line'
#br.form['passwd'] = 'tpe1234'
#br.form.find_control(id='inputs').__setattr__('value', 'https://www.youtube.com/watch?v=g4FMAgeVV_w')

br.submit()
aaa = br.response().read()
bbb = br.response().get_data()
print(aaa)
for link in br.links():
    print(link)

