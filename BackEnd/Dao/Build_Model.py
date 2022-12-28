# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ������¼
import datetime
from sqlalchemy import *
from Server import db, db_session


class BuildModel(db.Model):
    # ����
    __tablename__ = "build"
    # ����id������
    id = db.Column(Integer, primary_key=True)
    # ���ָ����Լƻ���id
    plan_id = db.Column(Integer, ForeignKey("plan.id"))
    # ���Ա��������
    report = db.Column(String(120), nullable=False, unique=True)
    # ����ʱ�䣬����Ҫ��ֵ���Զ�����
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def create(cls, plan_id, report):
        instance = cls(plan_id=plan_id, report=report)
        db.session.add(instance)
        db.session.commit()
        db.session.close()

    @classmethod
    def get_all(cls):
        return db_session.query(cls).all()

    @classmethod
    def get_filter_by(cls, **kwargs):
        return db_session.query(cls).filter_by(**kwargs).all()