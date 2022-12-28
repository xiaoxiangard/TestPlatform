# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
from sqlalchemy import *
from Server import db

testcase_plan_rel = db.Table(
    # �м�������
    'testcase_plan_rel',
    # Column('id', Integer, primary_key=True),
    # ����һ�ű����������Ϊһ�����ָ������������id
    Column('testcase_id', Integer,
           ForeignKey('testcase.id'),
           primary_key=True),
    # ����һ�ű����������Ϊһ�����ָ������������id
    Column('plan_id', Integer,
           ForeignKey('plan.id'),
           primary_key=True)
)