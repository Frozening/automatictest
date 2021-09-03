#!/usr/bin/python
import sys
sys.path.append("/home/ubuntu/autotest")
from commom.excel_util import excel
import pytest

print(excel())

@pytest.fixture(params = excel())
def a(request):
    return request.param

def test_case2(a):
    print(a)

@pytest.mark.parametrize('data', excel())
def test_case1(data):
    print(data)