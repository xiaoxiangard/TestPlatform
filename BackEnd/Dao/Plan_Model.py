# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# 测试计划
from sqlalchemy import *
from sqlalchemy.orm import relationship
from Dao.TestCase_Plan_Rel import testcase_plan_rel
from Server import db, db_session
from Utils.Log_Util import logger


class PlanModel(db.Model):
    # 表名
    __tablename__ = "plan"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 测试计划的名称
    name = db.Column(String(80), nullable=False, unique=True)
    # 引用测试用例的属性
    testcases = relationship("TestCaseModel",
                             secondary=testcase_plan_rel,
                             backref="plancase")

    @classmethod
    def get_all(cls):
        return db_session.query(cls).all()

    @classmethod
    def get_filter_by(cls, **kwargs):
        return db_session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def create(cls, name, case_objs):
        """

        :param name:  测试计划的名称
        :param testcase_objs:  测试用例对象的列表[Testcase1, Testcase2]
        :return:
        """
        instance = cls(name=name)
        db.session.add(instance)
        instance.testcases = case_objs
        db.session.commit()
        # 在commit之后，就会生成对应planid，就可以通过instance实例直接获取
        plan_id = instance.id
        logger.debug(f"创建的测试计划的ID为->{plan_id}")
        db.session.close()
        return plan_id