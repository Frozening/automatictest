#!/usr/bin/python
#!coding = utf-8
import sys
sys.path.append("/home/ubuntu/autotest")
from commom.request_util import REQUEST
import pytest
import json
from commom.yaml_util import YamlUtil

s = REQUEST("https://api.weixin.qq.com")
def assert_result(actual_result, expect_result): #actual_result传response.json(),expect_result传yaml用例中的validate字段
    for i in expect_result:
        if "eq" in i.keys():
            expect_result = i.get("eq")
            expect_result = set(expect_result.items()) 
            actual_result =  set(actual_result.items())
            assert expect_result.issubset(actual_result) #set的issubset方法,a.issubset(b):判断集合a的所有元素是否都包含在集合b中
        if "less_than" in i.keys():
            pass



class TestOne:
    @pytest.mark.parametrize("data", YamlUtil().read_test_yaml("./data/test_getaccess_token.yaml")) #yaml用例是一个列表，这样parametrize就能一个一个自动执行
    def test_getaccess_token(self, data):
            #请求数据和接口
            url = data["url"]
            #模拟请求下发
            response = s.do_get(url)

            #断言
            assert_result(response.json(), data["validate"])



            #assert response.json()["access_token"] != None, '请求发送成功'
