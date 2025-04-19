#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔


'''
对文件目录获取
'''
import os.path
import pytest

'''
对文件目录获取
'''
def filePath(fileDir='data',fileName=None):
	base_path=os.path.dirname(os.path.dirname(__file__))
	return os.path.join(base_path,fileDir,fileName)


