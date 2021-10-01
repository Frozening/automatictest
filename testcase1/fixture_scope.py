import pytest

class TestCase:
    @pytest.fixture(scope="function")
    def ff(self):
        print("前置动作")

    data_90 = [
            {'sql': '', 'data': {"p":1}, 'checkList': [2], 'title': "查看全部建筑信息接口"},
            {'sql': '', 'data': {"p":2}, 'checkList': [2], 'title': "更改数据库信息，再次查看全部建筑信息接口"}
        ]
    @pytest.mark.parametrize("cdb", data_90)
    def test_exper(self, ff, cdb):
        print(cdb["data"])

    def test_009(self, ff):
        print("sss")