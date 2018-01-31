#!/usr/bin/env python
#-*- coding=utf-8 -*-

from urllib import request

# 防止中文报错
CaptchaUrl = "http://http://qx8888cp.com/Vcode.aspx"
# 将cookies绑定到一个opener cookie由cookielib自动管理
# 用户名和密码
picture = request.urlretrieve(CaptchaUrl) 
local = open('test.jpg', 'wb')
local.write(picture)
local.close()