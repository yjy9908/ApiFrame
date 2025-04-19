#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
from utils.oprateSysconfig import oprateSysconfig

obj=oprateSysconfig()


def replaceHost(url):
	if '{host}' in url:
		finalUrl = str(url).replace('{host}', obj.getHost())
		return finalUrl





