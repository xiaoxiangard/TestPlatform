# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
from flask import request
from flask_restx import Namespace, Resource
from Dao.TestCase_Model import TestCaseModel
from Server import api, db
from Service.TestCase import TestCase
from Utils.Log_Util import logger

case_ns = Namespace("case", description="��������")


@case_ns.route("")
class TestCaseServer(Resource):
    get_parser = api.parser()
    # ��ѯ�ӿڣ� ���Դ�id ��Ҳ���Բ���id��
    # ����id�����Ƿ��� ȫ����¼
    # ��id�����ز�ѯ���Ķ�Ӧ�ļ�¼�����δ�鵽�򷵻� ���б�
    get_parser.add_argument("id", type=int, location="args")

    @case_ns.expect(get_parser)
    def get(self):
        """
        ���������Ĳ���
        :return:
        """
        # �ӿڵ�����������Ϣ
        case_id = request.args.get("id")
        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"���յ��Ĳ��� <===== {case_id}")
        # =====����service��ľ����ҵ���߼�
        testcase = TestCase()
        datas = testcase.get(case_id)
        # ====
        # ���ӿڵ���Ӧ����
        return {"code": 0, "msg": {"status": "success", "data": datas}}

    post_parser = api.parser()
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("case_title", type=str, required=True, location="json")
    post_parser.add_argument("remark", type=str, location="json")

    @case_ns.expect(post_parser)
    def post(self):
        """
        ��������������
        :return:
        """
        # ��ȡ��������
        case_data = request.json
        logger.info(f"���յ��Ĳ���<====== {case_data}")
        case_id = case_data.get("id")
        case_title = case_data.get("case_title")
        remark = case_data.get("remark")
        # case_id
        # ��������ڣ������������¼������
        # ������ڣ���ִ������������ ���� 40001������
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
        �����������޸�
        :return:
        """
        case_data = request.json
        logger.info(f"���յ��Ĳ���<====== {case_data}")
        case_id = case_data.get("id")
        # ��ѯ���ݿ⣬�鿴�Ƿ��м�¼
        exists = TestCaseModel.query.filter_by(id=case_id).first()
        logger.info(f"��ѯ������{exists}")
        # ��������ڣ��� ��ִ���޸Ĳ��� ������ 40002
        # ������ڣ�ִ���޸Ĳ���
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
        ����������ɾ��
        :return:
        """
        # �ӿ���Ӧ��Ϣ
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"���յ��Ĳ���id <====={case_id}")

        testcase = TestCase()
        r = testcase.delete(case_id)
        if r:
            # �ӿڵķ�����Ϣ
            return {"code": 0, "msg": f"case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"case is not exists"}