# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
from Service.Plan import Plan


class TestPlan:
    def setup_class(self):
        self.plan = Plan()

    def test_create(self):
        self.plan.create("���Լƻ�", [1])
        r = self.plan.get(4)
        assert r != []

    def test_get(self):
        r = self.plan.get(1)
        assert r != []
