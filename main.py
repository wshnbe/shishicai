#!/usr/bin/env python
#-*-coding=utf-8-*-

'main python file'

#import code
#import login
import proCai as pc
import config
import decimal



#初始化 当前个人分数 和 当前期号
score = float(pc.getperson())
pc.per_score = score
pc_dic = pc.getreq()[0]
pc.reqNo = pc_dic['Qino']
#下注 
pc.doit(pc_dic['ID'],pc_dic['Qino'],1,2,config.x_guess)
#监听
pc.circle()

#get code
#_list = code.getCode()
#userlogin profile
#uname = 'test01'
#upwd = 'test01'
#execute login
#login.userlogin(uname,upwd,_list[1],_list[0])