#!/usr/bin/env python
#-*- coding=utf-8 -*-

from PIL import Image
from aip import AipOcr
from selenium import webdriver
import config
import pytesseract
import random
import requests
import json

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)

def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read() 
options = {  
  'detect_direction': 'true',  
  'language_type': 'CHN_ENG',  
} 

def getCode():
	# r_login = requests.get('http://qx8888cp.com/login.aspx',cookie)
	# _cookie = r_login.
	# print(_cookie)
	dict_cookie = {}
	for key,value in config.c_dict.items():
		dict_cookie['name'] = 'ASP.NET_SessionId'
		dict_cookie['value'] = 'e4xj33hanf3pm4ghmjeqsrpx'
	# #打开浏览器截图
	flo = round(random.random(),15)
	url = 'http://qx8888cp.com/Vcode.aspx'
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get(url)
	driver.add_cookie(dict_cookie)
	driver.save_screenshot("test.png")
	#使用百度云进行图片识别
	filePath = config.IMAGE_PAGE 
	result = client.basicGeneral(get_file_content(filePath), options)  
	words = result['words_result']
	#获取到验证码
	strNum = words[0]['words']
	l = [dict_cookie,strNum]
	print(l)
	return l


