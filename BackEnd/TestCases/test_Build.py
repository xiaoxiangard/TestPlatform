# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ������¼��Ԫ����
from Service.Build import Build


class TestBuild:

    def setup_class(self):
        self.build = Build()

    def test_get(self):
        self.build.get(1)

    def test_create(self):
        self.build.create(1, "���Ա���")
