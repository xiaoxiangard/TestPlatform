# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# 构建记录处理逻辑
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
             # 把创建时间转换为string类型
             "created_at": str(build_objects.created_at)
             } for build_objects in build_objects]

        logger.info(f"获取到的构建记录的数据为->{build_datas}")
        return build_datas

    def get_objs_by_plan_id(self, plan_id=None):
        # 查询测试计划对应的测试记录有哪一些
        if plan_id:
            r = BuildModel.get_filter_by(plan_id=plan_id)
        else:
            r = BuildModel.get_all()
        logger.debug(f"获取到的构建记录的列表为{r}")
        return r

    def create(self, plan_id, report):
        """
        :param plan_id:
        :param report:
        :return:
        """
        logger.debug(f"创建构建记录对应的计划id为{plan_id}， 测试报告为{report}")
        BuildModel.create(plan_id, report)