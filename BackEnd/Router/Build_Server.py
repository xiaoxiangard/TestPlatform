# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
from flask import request
from flask_restx import Namespace, Resource
from Server import api
from Service.Build import Build
from Utils.Log_Util import logger

build_ns = Namespace("build", description="构建记录管理")


@build_ns.route("")
class BuildServer(Resource):
    # 通过 parser 对象解析参数
    get_parser = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_parser.add_argument("plan_id", type=int, location="args")

    @build_ns.expect(get_parser)
    # 定义测试用例，查找
    def get(self):
        """
        构建记录的查找
        :return:
        """
        # 接口的请求数据信息
        plan_id = request.args.get("plan_id")
        logger.info(f"测试计划获取接口接收到的参数 <===== {plan_id}")
        # =====调用service层的具体的业务逻辑
        build = Build()
        datas = build.get(plan_id)
        # ====
        # 给接口的响应内容
        return {"code": 0, "msg": {"status": "success", "data": datas}}