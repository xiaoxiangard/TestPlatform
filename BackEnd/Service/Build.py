# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ������¼�����߼�
from Dao.Build_Model import BuildModel
from Utils.Log_Util import logger


class Build:

    def get(self, plan_id=None):
        """
        :param plan_id:
        :return:
        """

        build_objects = self.get_objs_by_plan_id(plan_id)
        build_datas = [
            {"plan_id": build_objects.plan_id,
             "report": build_objects.report,
             # �Ѵ���ʱ��ת��Ϊstring����
             "created_at": str(build_objects.created_at)
             } for build_objects in build_objects]

        logger.info(f"��ȡ���Ĺ�����¼������Ϊ->{build_datas}")
        return build_datas

    def get_objs_by_plan_id(self, plan_id=None):
        # ��ѯ���Լƻ���Ӧ�Ĳ��Լ�¼����һЩ
        if plan_id:
            r = BuildModel.get_filter_by(plan_id=plan_id)
        else:
            r = BuildModel.get_all()
        logger.debug(f"��ȡ���Ĺ�����¼���б�Ϊ{r}")
        return r

    def create(self, plan_id, report):
        """
        :param plan_id:
        :param report:
        :return:
        """
        logger.debug(f"����������¼��Ӧ�ļƻ�idΪ{plan_id}�� ���Ա���Ϊ{report}")
        BuildModel.create(plan_id, report)