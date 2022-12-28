# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
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
username = data['mysqlinfo']['username']  # mysql数据库用户名
password = data['mysqlinfo']['password']  # mysql数据库密码
server = data['mysqlinfo']['server']  # mysql数据库的host地址
db = data['mysqlinfo']['db']  # 数据库名

# 链接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)
# 为了查询的时候IDE可以有对应的提示
db_session: Session = db.session


# 导包
def get_router():
    from Router.Build_Server import build_ns
    from Router.Plan_Server import plan_ns
    from Router.TestCase_Server import case_ns
    #添加api的命名空间，解决swagger不展示内容的问题
    api.add_namespace(build_ns, "/build")
    api.add_namespace(plan_ns, "/plan")
    api.add_namespace(case_ns, "/testcase")


if __name__ == '__main__':
    # 调用getrouter方法，完成testcase 路由的注册
    get_router()
    app.run(debug=True)