#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
import yaml
from common.OprateFile import filePath

class ReadYaml:
	def readYaml(self,fileDir,fileName):
		with open(filePath(fileDir=fileDir,fileName=fileName)) as f:
			return list(yaml.safe_load_all(f))

# if __name__=='__main__':
# 	reyaml=ReadYaml()
# 	print(reyaml.readYaml(fileDir='config',fileName='sysConfig.yaml'))