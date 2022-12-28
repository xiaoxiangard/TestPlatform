# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
# 调用Jenkins中的job，并生成报告
import yaml
from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:

    with open('./Data/jenkins_info.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    BASE_URL = data['jenkinsinfo']['BASE_URL']  # Jenkins服务地址
    USERNAME = data['jenkinsinfo']['USERNAME']  # Jenkins的用户名
    PASSWORD = data['jenkinsinfo']['PASSWORD']  # Jenkins用户的token
    JOB = data['jenkinsinfo']['JOB']  # Jenkins中job的名称

    @classmethod
    def invoke(cls, **kwargs):
        jenkins_task = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取jenkins的job对象
        ck_job = jenkins_task.get_job(cls.JOB)
        # 构建job
        ck_job.invoke(build_params=kwargs)
        # 获取当前job最后一次完成构建的编号
        first_build_number = ck_job.get_last_buildnumber()
        # 获取测试报告
        report = f"{cls.BASE_URL}job/{cls.JOB}/{first_build_number+1}/allure"
        return report


if __name__ == '__main__':
    JenkinsUtils.invoke(task="test_contact.py")