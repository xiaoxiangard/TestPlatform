# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# �����
from Dao.TestCase_Model import TestCaseModel
from Utils.Log_Util import logger


class TestCase:

    def get(self, case_id=None):
        if case_id:
            # �����Ϊ�գ���ѯ����
            case_data = TestCaseModel.get_by_filter(id=case_id)
            logger.info(f"{case_data}")
            if case_data:
                datas = [{"id": case_data.id,
                          "case_title": case_data.case_title,
                          "remark": case_data.remark}]
            else:
                datas = []
        else:
            # Ϊ�գ��������м�¼
            case_datas = TestCaseModel.get_all()
            datas = [{"id": case_data.id,
                      "case_title": case_data.case_title,
                      "remark": case_data.remark} for case_data in case_datas]
        logger.info(f"Ҫ���ص�����Ϊ<======{datas}")

        # return datas ��֤·����Ҫ���ص�����
        return datas

    def create(self,  case_id, case_title, remark):
        case_id = case_id
        # ��ѯ���ݿ⣬�鿴�Ƿ��м�¼
        exists = TestCaseModel.get_by_filter(id=case_id)
        logger.info(f"��ѯ������{exists}")
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
