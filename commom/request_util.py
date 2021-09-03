import requests
import json

'''参考www.cnblogs.com/wintest/p/13423231.html编写'''
class REQUEST:

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.sess = requests.session()

    def do_get(self, url, headers = None, params = None, **kwargs):
        return self.do_request("get", url, headers, **kwargs)

    def do_post(self, url, headers = None, data = None, json = None, **kwargs):
        return self.do_request("post", url, headers, data, json, **kwargs)

    def do_put(self, url, headers = None, data = None, **kwargs):
        return self.do_request("put", url, headers, data, **kwargs)

    def do_delete(self, url, headers = None, params = None, **kwargs):
        return self.do_request("delete", url, headers, **kwargs)

    '''do_patch的括号里是do_patch要接收的参数，self.do_request的括号里是要传给do_request接收的参数，本就没什么关联；传参与接收参数的地方要位置对应'''
    def do_patch(self, url, headers = None, data = None, **kwargs):
        return self.do_request("patch", url, headers, data, **kwargs)
    
    '''这个地方是位置传参'''
    def do_request(self, method, url, headers, data = None, json = None, **kwargs):
        url = self.api_root_url + url
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        if method == "get":
            return self.sess.get(url = url, params = params, **kwargs)
        elif method == "post":
            return self.sess.post(url = url, data = data, json = json, cookies = cookies, files = files, **kwargs)
        elif method == "put":
            if json:
                data = json.dumps(json)  # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
            return self.sess.put(url = url, data = data, **kwargs)
        elif method == "delete":
            return self.sess.delete(url = url, params = params,**kwargs)
        elif method == "patch":
            if json:
                data = json.dumps(json)
            return self.sess.patch(url, data, **kwargs)
        else:
            print("请求方式不正确")

'''参考www.cnblogs.com/Bdmn-Lg/p/13755607.html'''
class ApiRequest:
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.sess = requests.Session()

    def do_request(self, method, url, data = None, params = None, headers = None, cookies = None, json = None, files = None, auth = None, timeout = None, proxies = None, verify = None, cert = None):
        url = self.api_root_url + url
        return self.sess.request(method = method, url = url, data = data, params = params, headers = headers, cookies = cookies, json = json, files = files, auth = auth, timeout = timeout, proxies = proxies, verify = verify, cert = cert)
        


'''
#以下代码可以验证请求封装的功能
a = ApiRequest("https://api.weixin.qq.com")
payload = {'grant_type':'client_credential','appid':'wx289af799a499ac72','secret':'b54589067023f6afcfea82f35e6f67fa'}
r = a.do_request(method = "get", url = "/cgi-bin/token", params = payload)
print(r.json())
'''
