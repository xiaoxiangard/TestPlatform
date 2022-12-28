# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
from flask import request
from flask_restx import Namespace, Resource
from Server import api
from Service.Build import Build
from Utils.Log_Util import logger

build_ns = Namespace("build", description="������¼����")


@build_ns.route("")
class BuildServer(Resource):
    # ͨ�� parser �����������
    get_parser = api.parser()
    # ��ѯ�ӿڣ� ���Դ�id ��Ҳ���Բ���id��
    # ����id�����Ƿ��� ȫ����¼
    # ��id�����ز�ѯ���Ķ�Ӧ�ļ�¼�����δ�鵽�򷵻� ���б�
    get_parser.add_argument("plan_id", type=int, location="args")

    @build_ns.expect(get_parser)
    # �����������������
    def get(self):
        """
        ������¼�Ĳ���
        :return:
        """
        # �ӿڵ�����������Ϣ
        plan_id = request.args.get("plan_id")
        logger.info(f"���Լƻ���ȡ�ӿڽ��յ��Ĳ��� <===== {plan_id}")
        # =====����service��ľ����ҵ���߼�
        build = Build()
        datas = build.get(plan_id)
        # ====
        # ���ӿڵ���Ӧ����
        return {"code": 0, "msg": {"status": "success", "data": datas}}