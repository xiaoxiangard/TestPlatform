# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
import logging
import os

from logging.handlers import RotatingFileHandler

# �󶨰󶨾����logger����
logger = logging.getLogger(__name__)
# ��ȡ��ǰ�����ļ����ڵ�·��
root_path = os.path.dirname(os.path.abspath(__file__))
# ƴ�ӵ�ǰҪ�����־��·��
log_dir_path = os.sep.join([root_path, f'/logs'])
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)
# ������־��¼����ָ����־����·��,ÿ����־�Ĵ�С��������־������
file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path, 'log.log']), maxBytes=1024 * 1024, backupCount=10)
# ������־�ĸ�ʽ
date_string = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(filename)s]/[line: %(lineno)d]/[%(funcName)s] %(message)s ', date_string)
# ��־���������̨�ľ��
stream_handler = logging.StreamHandler()
# ����־��¼��ָ����־�ĸ�ʽ
file_log_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
# Ϊȫ�ֵ���־���߶��������־��¼��
# �󶨰󶨾����logger����
logger.addHandler(stream_handler)
logger.addHandler(file_log_handler)
# ������־�������
logger.setLevel(level=logging.DEBUG)