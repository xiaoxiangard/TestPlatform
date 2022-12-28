# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# dao 层，只负责和数据库交互相关，供上层service调用。
from sqlalchemy import *
from Server import db
from Utils.Log_Util import logger


class TestCaseModel(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    case_title = db.Column(String(80),
                           nullable=False, unique=True)
    # 备注
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
        logger.info(f"将要存储的内容为<======{testcase}")
        db.session.add(testcase)
        db.session.commit()
        db.session.close()

    @classmethod
    def delete(cls, **kwargs):
        TestCaseModel.query.filter_by(**kwargs).delete()
        # commit 之后需要添加close
        db.session.commit()
        db.session.close()  # 接口的返回信息