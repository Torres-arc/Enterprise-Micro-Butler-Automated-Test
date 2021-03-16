# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 9:30
# @Author  : Torres
# @File    : APIRequest.py
from imp import reload

import requests, os, json
from common.base_page import *
from common.statics import get_config

tokenUrl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'  # 企微token接口
userInfoListUrl = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'  # 企微获取员工uid接口
adict = {}
toke = get_config('control')


# 调用接口，获取token
def get_token():
    r = requests.get(url=tokenUrl, params={'corpid': toke['corpid'], 'corpsecret': toke['corpsecret']})
    result = r.json()
    return result.get('access_token')


# 通过token，获取员工uid
def get_user_list(token):
    r = requests.get(url=userInfoListUrl, params={
        'access_token': token, 'department_id': '1', 'fetch_child': '1'})
    result = r.json()
    return result


# 将uid写入文件，方便读取
def refreshInfo():
    a = get_token()
    list = get_user_list(a)
    dicl = list.get('userlist')
    for i in dicl:
        adict[i['userid']] = i['name']
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\idInfo.json'
    f = open(path, 'w', encoding='utf-8')
    js = json.dumps(adict)
    f.write(js)
    f.close()


if __name__ == '__main__':
    refreshInfo()