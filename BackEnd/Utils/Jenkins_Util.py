# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
# ����Jenkins�е�job�������ɱ���
import yaml
from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:

    with open('./Data/jenkins_info.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    BASE_URL = data['jenkinsinfo']['BASE_URL']  # Jenkins�����ַ
    USERNAME = data['jenkinsinfo']['USERNAME']  # Jenkins���û���
    PASSWORD = data['jenkinsinfo']['PASSWORD']  # Jenkins�û���token
    JOB = data['jenkinsinfo']['JOB']  # Jenkins��job������

    @classmethod
    def invoke(cls, **kwargs):
        jenkins_task = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # ��ȡjenkins��job����
        ck_job = jenkins_task.get_job(cls.JOB)
        # ����job
        ck_job.invoke(build_params=kwargs)
        # ��ȡ��ǰjob���һ����ɹ����ı��
        first_build_number = ck_job.get_last_buildnumber()
        # ��ȡ���Ա���
        report = f"{cls.BASE_URL}job/{cls.JOB}/{first_build_number+1}/allure"
        return report


if __name__ == '__main__':
    JenkinsUtils.invoke(task="test_contact.py")