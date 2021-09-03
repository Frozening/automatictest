#! /usr/bin/python
import yaml

class YamlUtil:
    def read_yaml(self, yamlfile):
        '''把yaml流转化为python字典'''
        with open(yamlfile, 'r', encoding = 'utf-8') as f:
            value = yaml.load(f, Loader = yaml.FullLoader)
            print(value) #return value

    def read_test_yaml(self, yamlfile):
        '''因为mark.parametrize()装饰器要求参数是列表，每组测试数据对应一个字典，
        测试用例的yaml数据应该写为字典列表，这样parametrize()每次就能传一组测试数据'''
        with open(yamlfile, 'r', encoding = 'utf-8') as f:
            value = yaml.load(f, Loader = yaml.FullLoader)
            return value

    def write_extract_yaml(self, data):
        '''提取python对象，以键值对的形式写入yaml文档'''
        with open('./extract.yaml', 'a', encoding = 'utf-8') as f:
            yaml.dump(data, f)

    def clear_extract_yaml(self):
        with open('./extract.yaml', 'w') as f:
            f.truncate()

    '''参考https://www.cnblogs.com/yoyoketang/p/14116839.html'''
    def assert_response(self, response, validate):
        import jsonpath
        for i in validate:
            if "eq" in i.keys():
                yaml_result = i.get("eq")[0]
                actual_result = jsonpath.jsonpath(response.json(), yaml_result)
                expect_result = i.get("eq")[1]
                print("实际结果：%s" % actual_result)
                print("期望结果：%s" % expect_result)
                assert actual_result[0] == expect_result

token = '909089'#设置一个python对象
if __name__ == '__main__':
    YamlUtil().write_extract_yaml({'token':token})
    YamlUtil().read_yaml('./extract.yaml')
    YamlUtil().write_extract_yaml({'token':'159357'})
    YamlUtil().read_yaml('./extract.yaml') #对于同名键，yaml读取的总是此键的最新的值
    YamlUtil().write_extract_yaml({'曰':'天苍苍不可得久视，地颤颤不可得久履，道此绝矣！'})
    YamlUtil().read_yaml('./extract.yaml') #返回的是整体为字典的、包含各字段的yaml数据