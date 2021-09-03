#!/usr/bin/python
import pytest
import requests
import json

s = requests.Session()

class TestCase:
    def test_cookie_1(self):
        url = "https://www.v2ex.com"
        payload={}
        headers = {} #像header虽然为空，但不能不写。通过关键字驱动可以默认其为None

        print(s.cookies) #打印发送请求前会话中的cookies

        res = s.request("GET", url, headers=headers, params=payload)
        print(res.cookies) #打印这v2ex网站响应的Cookies
        print(s.cookies) #打印接受响应后会话中的Cookies

    def test_cookie_2(self): #没必要传keep_session了，不然session又要初始化了
        #s = keep_session
        url = "https://www.baidu.com"

        print(s.cookies) #打印发送第二个请求前的会话中的Cookies

        res = s.request("GET", url)
        print(res.cookies) #打印baidu返回的响应中的Cookies
        print(s.cookies) #打印目前的会话中的全部Cookies信息，可见会话的Cookies更新了

    def test_cookie_3(self): #没必要传keep_session了，不然session又要初始化了
        print(s.cookies) #打印发送第三个请求前的会话中的Cookies
        url = "https://www.google.com" 
        res = s.request("get", url, headers={}, params={})

        print(res.cookies) #打印google返回的响应中的Cookies
        print(s.cookies) #打印目前的会话中的Cookies信息，可见会话的Cookies又一次更新了