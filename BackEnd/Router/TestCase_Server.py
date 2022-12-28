# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
from flask import request
from flask_restx import Namespace, Resource
from Dao.TestCase_Model import TestCaseModel
from Server import api, db
from Service.TestCase import TestCase
from Utils.Log_Util import logger

case_ns = Namespace("case", description="用例管理")


@case_ns.route("")
class TestCaseServer(Resource):
    get_parser = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_parser.add_argument("id", type=int, location="args")

    @case_ns.expect(get_parser)
    def get(self):
        """
        测试用例的查找
        :return:
        """
        # 接口的请求数据信息
        case_id = request.args.get("id")
        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"接收到的参数 <===== {case_id}")
        # =====调用service层的具体的业务逻辑
        testcase = TestCase()
        datas = testcase.get(case_id)
        # ====
        # 给接口的响应内容
        return {"code": 0, "msg": {"status": "success", "data": datas}}

    post_parser = api.parser()
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("case_title", type=str, required=True, location="json")
    post_parser.add_argument("remark", type=str, location="json")

    @case_ns.expect(post_parser)
    def post(self):
        """
        测试用例的新增
        :return:
        """
        # 获取请求数据
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        case_id = case_data.get("id")
        case_title = case_data.get("case_title")
        remark = case_data.get("remark")
        # case_id
        # 如果不存在，则添加这条记录到库中
        # 如果存在，不执行新增操作， 返回 40001错误码
        testcaes = TestCase()
        r = testcaes.create(case_id, case_title, remark)
        if r:
            return {"code": 0, "msg": f"case id {case_id} success add."}
        else:
            return {"code": 40001, "msg": "case is exists"}

    put_parser = api.parser()
    put_parser.add_argument("id", type=int, required=True, location="json")
    put_parser.add_argument("case_title", type=str, required=True, location="json")
    put_parser.add_argument("remark", type=str, location="json")

    @case_ns.expect(put_parser)
    def put(self):
        """
        测试用例的修改
        :return:
        """
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        case_id = case_data.get("id")
        # 查询数据库，查看是否有记录
        exists = TestCaseModel.query.filter_by(id=case_id).first()
        logger.info(f"查询表结果：{exists}")
        # 如果不存在，则 不执行修改操作 并返回 40002
        # 如果存在，执行修改操作
        if exists:
            case_data1 = {}
            case_data1["case_title"] = case_data.get("case_title")
            case_data1["remark"] = case_data.get("remark")
            TestCaseModel.query.filter_by(id=case_id).update(case_data1)
            db.session.commit()
            db.session.close()
            return {"code": 0, "msg": f"case id {case_id} success change to {case_data1}"}
        else:
            return {"code": 40002, "msg": "case is not exists"}

    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, location="json", required=True)

    @case_ns.expect(delete_parser)
    def delete(self):
        """
        测试用例的删除
        :return:
        """
        # 接口响应信息
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"接收到的参数id <====={case_id}")

        testcase = TestCase()
        r = testcase.delete(case_id)
        if r:
            # 接口的返回信息
            return {"code": 0, "msg": f"case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"case is not exists"}