#!/usr/bin/python
# -*- coding: utf-8 -*-

#init score of a day
first_score = 144.8 
#common cookie
c_dict = {}
c_dict['ASP.NET_SessionId'] = 'zf2flvmnjnl4gf3d0gf4cvez'
c_dict['__root_domain_v'] = '.qx8888cp.com'
c_dict['_qdda'] = '2-1.2dgdbg'
c_dict['_qddab'] = '2-6px9ki.jco9olj1'
c_dict['_qddamta_2852153938'] = '2-0'
c_dict['_qddaz'] = 'QD.ozr47t.ladqks.jcmzg2br'

# headers 
headers = {
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
	'Connection':'keep-alive',
	'Content-Length':'276',
	'Content-Type':'application/json; charset=UTF-8'
	}

#common param for gambling
b_guess = "大 "
x_guess = "小 "
times = [1,2,3,5,8,18,30]
extend = 5
init_core = 2
max_win = 50
max_lose = 134
#下注参数
def getData(cid,cno,times,tmoney,guess):
	data = {
		"_FangAn":{
			"Fanprice":tmoney,
			"Fenshu":1,
			"gk":0,
			"baodifenshu":1,
			"RengouFen":1,
			"fenmoney":tmoney,
			"QiHao":cno,
			"QIID":cid,
			"QINum":1,
			"RengGouMoney":tmoney,
			"Gufen":100
		},
		"_list":[{
			"ReQID":cid,
			"ReQno":str(cno),
			"ReWid":105,
			"Wanfan":"组合",
			"TouZhuneiRong":guess,
			"BeiShu":times,
			"TMoney":tmoney
		}]
	}
	return data