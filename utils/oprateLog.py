#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔
import logging
import os
import datetime

def wirte_log(log_content):
	#生成时间戳
	timestamp=datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
	base_path=os.path.dirname(os.path.dirname(__file__))

	filename=(f"{base_path}/log/{timestamp}.log")

	logFile=logging.FileHandler(filename,'a',encoding='utf-8')
	#日志格式
	fmt=logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s',
	                        datefmt='%Y-%m-%d %H:%M:%S')
	logFile.setFormatter(fmt)

	log=logging.Logger('log',level=logging.DEBUG)
	log.addHandler(logFile)
	log.info(log_content)



