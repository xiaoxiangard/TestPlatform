# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ����㵥Ԫ����
from Service.TestCase import TestCase


class TestTestCase:

    def setup_class(self):
        self.testcase = TestCase()

    def test_get(self):
        r = self.testcase.get()
        assert r != []

    def test_create(self):
        self.testcase.create(2, "test_contact2.py", "��ҵ΢�Ų�������2")
        # ���create ����û��bug����ôʹ��get(1)����һ���з���ֵ
        r = self.testcase.get(2)
        # �൱��һ�����ö�����ֻ��Ϊ�˷��㵥Ԫ����
        assert r != []

    def test_delete(self):
        self.testcase.delete(1)
        r = self.testcase.get(1)
        # ���Ի�ȡ���Ľ��Ϊ�գ���ʾɾ���ɹ�
        assert r == []
