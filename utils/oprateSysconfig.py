#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
from utils.ReadYaml import ReadYaml
from utils.oprateLog import wirte_log

obj=ReadYaml()

class oprateSysconfig:
	def getHost(self):
		data=obj.readYaml('config','sysConfig.yaml')
		host=data[0]['host']
		wirte_log(f'读取host配置：{host}')
		return host



	def getToken(self):
		data = obj.readYaml('config', 'sysConfig.yaml')
		token=data[0]['token']
		wirte_log(f'读取token配置：{token}')
		return token

	def getPlatform(self):
		data = obj.readYaml('config', 'sysConfig.yaml')
		platform = data[0]['platform']
		wirte_log(f'读取platform配置：{platform}')
		return platform

	def getChannel(self):
		data = obj.readYaml('config', 'sysConfig.yaml')
		channel = data[0]['channel']
		wirte_log(f'读取channel配置：{channel}')
		return channel


	def getConnection(self):
		data = obj.readYaml('config', 'sysConfig.yaml')
		Connection = data[0]['Connection']
		wirte_log(f'读取Connection配置：{Connection}')
		return Connection

	def getContent_type(self):
		data = obj.readYaml('config', 'sysConfig.yaml')
		content_type = data[0]['content_type']
		wirte_log(f'读取content_type配置：{content_type}')
		return content_type

# if __name__=='__main__':
# 	oprateSysconfig=oprateSysconfig()
# 	print(oprateSysconfig.getHost())
# 	print(oprateSysconfig.getToken())