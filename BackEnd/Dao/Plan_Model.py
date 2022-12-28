# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ���Լƻ�
from sqlalchemy import *
from sqlalchemy.orm import relationship
from Dao.TestCase_Plan_Rel import testcase_plan_rel
from Server import db, db_session
from Utils.Log_Util import logger


class PlanModel(db.Model):
    # ����
    __tablename__ = "plan"
    # ����ID ������Ψ һ��ʶ
    id = db.Column(Integer, primary_key=True)
    # ���Լƻ�������
    name = db.Column(String(80), nullable=False, unique=True)
    # ���ò�������������
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

        :param name:  ���Լƻ�������
        :param testcase_objs:  ��������������б�[Testcase1, Testcase2]
        :return:
        """
        instance = cls(name=name)
        db.session.add(instance)
        instance.testcases = case_objs
        db.session.commit()
        # ��commit֮�󣬾ͻ����ɶ�Ӧplanid���Ϳ���ͨ��instanceʵ��ֱ�ӻ�ȡ
        plan_id = instance.id
        logger.debug(f"�����Ĳ��Լƻ���IDΪ->{plan_id}")
        db.session.close()
        return plan_id