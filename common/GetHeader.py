#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
import json
from utils.oprateSysconfig import oprateSysconfig


obj=oprateSysconfig()

def getHeaders():
	key_list={'Connection','eic-token','platform','channel','content-type'}
	value_list={
		obj.getConnection(),
		obj.getToken(),
		obj.getPlatform(),
		obj.getChannel(),
		obj.getContent_type()}
	return dict(zip(key_list,value_list))

print(getHeaders())