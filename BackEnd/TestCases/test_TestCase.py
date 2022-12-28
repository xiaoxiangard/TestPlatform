# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# 服务层单元测试
from Service.TestCase import TestCase


class TestTestCase:

    def setup_class(self):
        self.testcase = TestCase()

    def test_get(self):
        r = self.testcase.get()
        assert r != []

    def test_create(self):
        self.testcase.create(2, "test_contact2.py", "企业微信测试用例2")
        # 如果create 方法没有bug，那么使用get(1)，就一定有返回值
        r = self.testcase.get(2)
        # 相当于一个后置动作，只是为了方便单元测试
        assert r != []

    def test_delete(self):
        self.testcase.delete(1)
        r = self.testcase.get(1)
        # 断言获取到的结果为空，表示删除成功
        assert r == []
