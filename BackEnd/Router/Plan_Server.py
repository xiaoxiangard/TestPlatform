# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
import json
from flask import request
from flask_restx import Namespace, Resource
from Server import api
from Service.Plan import Plan
from Utils.Log_Util import logger

plan_ns = Namespace("plan", description="���Լƻ�����")


@plan_ns.route("")
class PlanServer(Resource):
    get_parser = api.parser()
    # ��ѯ�ӿڣ� ���Դ�id ��Ҳ���Բ���id��
    # ����id�����Ƿ��� ȫ����¼
    # ��id�����ز�ѯ���Ķ�Ӧ�ļ�¼�����δ�鵽�򷵻� ���б�
    get_parser.add_argument("id", type=int, location="args")

    @plan_ns.expect(get_parser)
    def get(self):
        """
        ���Լƻ��Ĳ���
        :return:
        """
        # �ӿڵ�����������Ϣ
        plan_id = request.args.get("id")
        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"���Լƻ���ȡ�ӿڽ��յ��Ĳ��� <===== {plan_id}")
        # =====����service��ľ����ҵ���߼�
        plan = Plan()
        datas = plan.get(plan_id)
        # ====
        # ���ӿڵ���Ӧ����
        return {"code": 0, "msg": {"status": "success", "data": datas}}

    post_parser = api.parser()
    post_parser.add_argument("name", type=str, required=True, location="json")
    post_parser.add_argument("testcases", location="json")

    @plan_ns.expect(post_parser)
    def post(self):
        """
        ���Լƻ�������
        :return:
        """
        # ��ȡ��������
        plan_data = request.json
        logger.info(f"���Լƻ������ӿڽ��յ��Ĳ���<====== {plan_data}")
        name = plan_data.get("name")
        testcases = plan_data.get("testcases")
        testcases = json.loads(testcases) if isinstance(testcases, str) else testcases
        # ===============���õ�service�߼�
        plan = Plan()
        plan.create(name, testcases)
        return {"code": 0, "msg": f"plan success add."}