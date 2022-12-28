# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# 服务层
from Dao.TestCase_Model import TestCaseModel
from Utils.Log_Util import logger


class TestCase:

    def get(self, case_id=None):
        if case_id:
            # 如果不为空，查询操作
            case_data = TestCaseModel.get_by_filter(id=case_id)
            logger.info(f"{case_data}")
            if case_data:
                datas = [{"id": case_data.id,
                          "case_title": case_data.case_title,
                          "remark": case_data.remark}]
            else:
                datas = []
        else:
            # 为空，返回所有记录
            case_datas = TestCaseModel.get_all()
            datas = [{"id": case_data.id,
                      "case_title": case_data.case_title,
                      "remark": case_data.remark} for case_data in case_datas]
        logger.info(f"要返回的数据为<======{datas}")

        # return datas 保证路由有要返回的数据
        return datas

    def create(self,  case_id, case_title, remark):
        case_id = case_id
        # 查询数据库，查看是否有记录
        exists = TestCaseModel.get_by_filter(id=case_id)
        logger.info(f"查询表结果：{exists}")
        if not exists:
            TestCaseModel.create(case_id, case_title, remark)
            return True
        else:
            return False

    def delete(self, case_id):
        """

        :param case_id:
        :return:
        """
        exists = TestCaseModel.get_by_filter(id=case_id)
        if exists:
            TestCaseModel.delete(id=case_id)
            return True
        return False
