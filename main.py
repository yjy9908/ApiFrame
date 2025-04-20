import pytest
import subprocess
import datetime
from utils.oprateLog import wirte_log




'''
执行所有测试用例入口
使用allure生成测试报告
'''
if __name__ == '__main__':
    # 生成时间戳
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    pytest.main(["-s","-v","tests/","--alluredir",f"./report/{timestamp}_report/result"])
    subprocess.call(f'allure generate report/{timestamp}_report/result/ -o report/{timestamp}_report/html --clean',shell=True)
    wirte_log('生成测试报告')

