#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:肥仔

import pytest
import allure
from base.requestMethod import Requests
from utils.oprateExcel import oprateExcel
from common.GetHeader import getHeaders
from utils.replaceParam import replaceHost

requests=Requests()
objExcel=oprateExcel()

@allure.feature('测试用户信息接口调用是否正常')
@pytest.mark.parametrize('data',objExcel.isRun(fileName='basedata.xls'))
def test_UserInfo(data):
	base_url=data['请求地址']
	r=requests.requests(
		url=replaceHost(base_url),
		method='get',
		headers=getHeaders()
	)
	assert r.json()['code']==data['期望结果']


if __name__=='__main__':
	pytest.main("-v","-s","test_UserInfo.py")