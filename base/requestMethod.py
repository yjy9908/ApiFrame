#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
import requests
'''
对request请求的封装
'''

class Requests:

	def requests(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request('get',url,**kwargs)
		if method=='post':
			return requests.request('post',url,**kwargs)
		if method=='delete':
			return requests.request('delete',url,**kwargs)
		if method=='put':
			return requests.request('put',url,**kwargs)


	def get(self,url,**kwargs):
		return requests.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return requests.request(url=url,method='post',**kwargs)

	def delete(self,url,**kwargs):
		return requests.request(url=url,method='delete',**kwargs)

	def put(self,url,**kwargs):
		return requests.request(url=url,method='put',**kwargs)