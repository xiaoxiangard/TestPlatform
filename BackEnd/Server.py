# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
import yaml
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True)

with open('./Data/mysql_info.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
username = data['mysqlinfo']['username']  # mysql���ݿ��û���
password = data['mysqlinfo']['password']  # mysql���ݿ�����
server = data['mysqlinfo']['server']  # mysql���ݿ��host��ַ
db = data['mysqlinfo']['db']  # ���ݿ���

# �������ݿ�
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy �� app
db = SQLAlchemy(app)
# Ϊ�˲�ѯ��ʱ��IDE�����ж�Ӧ����ʾ
db_session: Session = db.session


# ����
def get_router():
    from Router.Build_Server import build_ns
    from Router.Plan_Server import plan_ns
    from Router.TestCase_Server import case_ns
    #���api�������ռ䣬���swagger��չʾ���ݵ�����
    api.add_namespace(build_ns, "/build")
    api.add_namespace(plan_ns, "/plan")
    api.add_namespace(case_ns, "/testcase")


if __name__ == '__main__':
    # ����getrouter���������testcase ·�ɵ�ע��
    get_router()
    app.run(debug=True)