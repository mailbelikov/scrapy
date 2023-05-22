import requests
from bs4 import BeautifulSoup as bs

sess = requests.Session()
site = sess.post('http://192.168.0.1/goform/goform_set_cmd_process', data = {'goformId':'LOGIN', 'password':'YWRtaW4='})  # , auth = ('admin', 'admin')
print(site)
site = sess.post('http://192.168.0.1/goform/goform_set_cmd_process', data = {'goformId':'SET_WIFI_INFO', 'wifiEnabled':'0'})
print(site)
site.close
