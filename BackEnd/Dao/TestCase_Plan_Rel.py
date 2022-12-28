# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
from sqlalchemy import *
from Server import db

testcase_plan_rel = db.Table(
    # 中间表的名称
    'testcase_plan_rel',
    # Column('id', Integer, primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('testcase_id', Integer,
           ForeignKey('testcase.id'),
           primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('plan_id', Integer,
           ForeignKey('plan.id'),
           primary_key=True)
)