#!/usr/bin/env python
# _*_ coding=utf-8 _*_

'this is a script for shishicai'

import requests,json,config,decimal
from time import sleep

#记录上一期 积分和期号
per_score = 0.0
reqNo = '' # Qino
#1.获取个人的基本信息
def getperson():
	per_url = 'http://qx8888cp.com/Servers/UserInfo.ashx'
	per = requests.get(per_url,cookies=config.c_dict)
	per_dict = json.loads(per.text)
	per_score = per_dict['Score']
	return per_score

#2.获取期号和期id	
def getreq():
	req_url = 'http://qx8888cp.com/Servers/Game/qinhaocurrent.ashx?ReCID=15'
	req = requests.get(req_url,cookies=config.c_dict)
	req_dict = json.loads(req.text)
	return req_dict

#3.post-->下注
def doit(reqid,reqno,times,score,guess):
	post_url = 'http://qx8888cp.com/Servers/Game/pcdd/pcddsubmit.ashx?CaiID=15'
	params = config.getData(reqid,reqno,times,score,guess)
	print('期号：%s , 下注倍数：%d,下注钱数：%d' % (reqno,times,score) )
	post = requests.post(post_url,data=json.dumps(params),cookies=config.c_dict,headers=config.headers)
	print(post.text)

#4.设置亏盈标准
def balance(start,cur,full):
	if cur - start >= full :
		print('赚钱达到今天的目标')
		return True
	elif start - cur >= full :
		print('亏损达到今天的目标')
		return True
	return False

#4. 逻辑组装
def circle():
	global per_score
	global reqNo
	
	#计数
	count = 0
	while(True):
		#期号
		tmp_req_dict = getreq()
		if len(tmp_req_dict) != 0:
			cno = tmp_req_dict[0]['Qino']
			cid = tmp_req_dict[0]['ID']
			#当前个人score
			tmp_score = float(getperson())
			#下一期到来了
			if reqNo != cno:
				print('收到新的期号.....')
				if tmp_score > per_score:
					print('赚:%f,当前余额是：%f' % (tmp_score-per_score, tmp_score))
					#缓存变量替换
					per_score = tmp_score
					reqNo = cno
					flag = balance(config.first_score,tmp_score,config.max_win)
					#如果赚到了今天的目标，则结束今天
					if flag :
						break
					#count清零
					count = 0
					t = config.times[count]
					#下注
					doit(cid,cno,t,config.init_core,config.b_guess)
				elif tmp_score < per_score:
					print('赔:%f,当前余额是：%f' % ( per_score-tmp_score, tmp_score ))
					#缓存变量替换
					per_score = tmp_score
					reqNo = cno
					#如果亏损达到标准，则结束今天
					flag = balance(config.first_score,tmp_score,config.max_lose)
					if flag :
						break
					#count++ 启动下一期倍数
					count = count + 1
					t = config.times[count]
					#下注
					doit(cid,cno,t,config.init_core*t,config.b_guess)

				elif tmp_score == per_score:
					print('持平,当前余额是：%f' % tmp_score )
		#暂停5秒
		print('休息5s。。。。。')
		sleep(5)


