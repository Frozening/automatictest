#!/usr/bin/python
import pytest
import requests
import json

#keep_session = requests.Session()

base_url = "https://api.weixin.qq.com"

@pytest.fixture()
def keep_session():
    return requests.Session()

class TestCase:
    def test_get_access_token(self):
        #s = keep_session
        url = base_url + "/cgi-bin/token"

        payload={'grant_type':'client_credential','appid':'wx289af799a499ac72','secret':'b54589067023f6afcfea82f35e6f67fa'}
        headers = {} #像header虽然为空，但不能不写。通过关键字驱动可以默认其为None

        res = requests.request("GET", url, headers=headers, params=payload)
        global access_token #在函数体内必须通过global声明变量为全局变量，在函数外就没必要了
        access_token = res.json()["access_token"]
        assert access_token != ""

    def test_get_api_ipaddress(self):
        #s = keep_session
        url = base_url + "/cgi-bin/get_api_domain_ip"

        payload={'access_token':access_token} #引用(全局)变量的值无需global
        headers = {}
       
        res = requests.request("GET", url, headers=headers, params=payload)
        assert res.json()["ip_list"] != []