#!/usr/bin/env python
#-*-coding=utf-8-*-

'user login'

import requests,json
import config

def userlogin(uname,upwd,code,cookie):
	url = 'http://qx8888cp.com/Servers/UserLogin.ashx'
	headers = {'Content-Type':'text/html; charset=utf-8'}
	data = {
		'LoginName': uname,
		'Pass': upwd,
		'UserNumber': code
	}
	print(cookie)
	print(code)
	_post = requests.post(url,data=json.dumps(data),cookies=config.c_dict,headers=headers)
	print(_post.cookies.get_dict())
	print(_post.text)