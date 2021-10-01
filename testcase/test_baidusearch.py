import requests

class TestApiSearch:
    url = "https://www.baidu.com/"

    def test_keyword_length_256(self):
        print("# 执行关键字长度256用例的测试#")
        params = {'wd': '软件测试'*64}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 完成关键字长度256用例的测试#")

    def test_keyword_length_0(self):
        print("# 执行关键字长度0用例的测试#")
        params = {'wd': ''}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 执行关键字长度0用例的测试#")

    def test_keyword_length_1(self):
        print("# 执行关键字长度1用例的测试#")
        params = {'wd': '1'}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 执行关键字长度1用例的测试#")

    def test_keyword_special_char(self):
        print("# 执行关键字为特殊字符用例的测试#")
        params = {'wd': '@'}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200

        params = {'wd': '#'}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200

        params = {'wd': '~'}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 执行关键字为特殊字符用例的测试#")

    def test_keyword_japanese(self):
        print("# 执行关键字为日语用例的测试#")
        params = {'wd': 'テスト'}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 执行关键字为日语用例的测试#")

    def test_keyword_inject(self):
        print("# 执行关键字有sql注入用例的测试#")
        params = {'wd': "' or 1 = 1"}
        resp = requests.get(self.url, params=params)
        assert resp.status_code == 200
        print("# 执行关键字有sql注入用例的测试#")

    def test_keyword_post_instead_get(self):
        print("# 执行get改post用例的测试#")
        params = {'wd': 'test'}
        resp = requests.post(self.url, data=params)
        assert resp.status_code == 302
        print("# 执行get改post用例的测试#")

# pytest -s -v testcase/api/test_api_search.py --html=api_search_report.html