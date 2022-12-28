# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# dao �㣬ֻ��������ݿ⽻����أ����ϲ�service���á�
from sqlalchemy import *
from Server import db
from Utils.Log_Util import logger


class TestCaseModel(db.Model):
    # ����
    __tablename__ = "testcase"
    # ����ID ������Ψ һ��ʶ
    id = db.Column(Integer, primary_key=True)
    # �����ı��� �����ļ���,�޶� 80���ַ� ����Ϊ�գ�����Ψһ
    case_title = db.Column(String(80),
                           nullable=False, unique=True)
    # ��ע
    remark = db.Column(String(120))

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, case_id, case_title, remark):
        testcase = cls(id=case_id, case_title=case_title, remark=remark)
        logger.info(f"��Ҫ�洢������Ϊ<======{testcase}")
        db.session.add(testcase)
        db.session.commit()
        db.session.close()

    @classmethod
    def delete(cls, **kwargs):
        TestCaseModel.query.filter_by(**kwargs).delete()
        # commit ֮����Ҫ���close
        db.session.commit()
        db.session.close()  # �ӿڵķ�����Ϣ