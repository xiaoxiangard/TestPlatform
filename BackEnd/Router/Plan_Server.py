# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
import json
from flask import request
from flask_restx import Namespace, Resource
from Server import api
from Service.Plan import Plan
from Utils.Log_Util import logger

plan_ns = Namespace("plan", description="测试计划管理")


@plan_ns.route("")
class PlanServer(Resource):
    get_parser = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_parser.add_argument("id", type=int, location="args")

    @plan_ns.expect(get_parser)
    def get(self):
        """
        测试计划的查找
        :return:
        """
        # 接口的请求数据信息
        plan_id = request.args.get("id")
        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"测试计划获取接口接收到的参数 <===== {plan_id}")
        # =====调用service层的具体的业务逻辑
        plan = Plan()
        datas = plan.get(plan_id)
        # ====
        # 给接口的响应内容
        return {"code": 0, "msg": {"status": "success", "data": datas}}

    post_parser = api.parser()
    post_parser.add_argument("name", type=str, required=True, location="json")
    post_parser.add_argument("testcases", location="json")

    @plan_ns.expect(post_parser)
    def post(self):
        """
        测试计划的新增
        :return:
        """
        # 获取请求数据
        plan_data = request.json
        logger.info(f"测试计划新增接口接收到的参数<====== {plan_data}")
        name = plan_data.get("name")
        testcases = plan_data.get("testcases")
        testcases = json.loads(testcases) if isinstance(testcases, str) else testcases
        # ===============调用的service逻辑
        plan = Plan()
        plan.create(name, testcases)
        return {"code": 0, "msg": f"plan success add."}