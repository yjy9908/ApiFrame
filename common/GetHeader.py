#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
import json
from utils.oprateSysconfig import oprateSysconfig


obj=oprateSysconfig()

def getHeaders():
	data_dict= {}
	dictchannel={'channel':obj.getChannel()}
	dictContype={'content-type':obj.getContent_type()}
	dictConn={'Connection':obj.getConnection()}
	dictToken={'eic-token':obj.getToken()}
	dictPlat={'platform':obj.getPlatform()}
	data_dict.update(dictchannel)
	data_dict.update(dictContype)
	data_dict.update(dictPlat)
	data_dict.update(dictConn)
	data_dict.update(dictToken)
	return data_dict

# print(getHeaders())