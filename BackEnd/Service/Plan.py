# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__��wangxiaoxiang
"""
# ���Լƻ������߼�
from Dao.Plan_Model import PlanModel
from Dao.TestCase_Model import TestCaseModel
from Service.Build import Build
from Utils.Jenkins_Util import JenkinsUtils
from Utils.Log_Util import logger


class Plan:

    def execute(self, plan_id, case_titles):
        """
        ִ�в��������� ��Ҫ����ƻ���id���Լ���Ӧ�ľ����������Ϣ
        :return:
        """

        # ['testcase1.py', 'testcase2.py']  -> pytest testcase1.py testcase2.py
        # ��ɸ�ʽת����jenkins����ֱ�ӵ���
        case_titles = " ".join(case_titles)
        logger.debug(f"���Լƻ�{plan_id}��"
                     f"Ҫִ�еĵĲ�����������{case_titles}")
        # ����ִ����ִ�в�������
        report = JenkinsUtils.invoke(task=case_titles)
        # д�빹����¼
        build = Build()
        build.create(plan_id, report)

    def create(self, name, case_id_lists):
        """
        1. ��ù����Ĳ���������������Ӧ�Ĳ��Լƻ�
        2. ִ�в��Լƻ�������һ��������¼
        :return:
        """
        # case_id_lists -> case_objs
        case_objects = [TestCaseModel.get_by_filter(id=case_id)
                        for case_id in case_id_lists]
        logger.debug(f"�����б�{case_id_lists}��"
                     f"��ȡ���Ĳ��������Ķ���Ϊ{case_objects}")
        # �ڴ����Ĺ����У���Ҫ������Լƻ������ƣ�����ָ��������Щ��������
        plan_id = PlanModel.create(name, case_objects)
        # ֱ�ӵ���get��������ȡת����Ĳ������ݵĸ�ʽ
        case_titles = self.get(plan_id)[0]["testcase_info"]
        self.execute(plan_id, case_titles)

    def get(self, plan_id=None):
        """

        :param plan_id:
        :return:
        """
        plan_objects = self.get_objs(plan_id)
        plan_datas = [{"id": plan_object.id,
                       "name": plan_object.name,
                       # ��ȡ���Ĳ������ݴӶ���ת����ʵ�ʵ�������Ϣ�������Ķ�
                       "testcase_info": [
                           testcase.case_title for testcase in plan_object.testcases]}
                      for plan_object in plan_objects]
        logger.info(f"��ȡ���Ĳ��Լƻ�������Ϊ->{plan_datas}")
        return plan_datas

    def get_objs(self, plan_id=None):
        if plan_id:
            r = PlanModel.get_filter_by(id=plan_id)
        else:
            r = PlanModel.get_all()
        logger.debug(f"��ȡ���Ĳ��Լƻ����б�Ϊ{r}")
        return r
