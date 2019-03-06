#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 22:16
# @Author  : 海心
# @Site    : 
# @File    : meta_create.py
# @Software: PyCharm
# @descri


class Step_org_create_cloud_host(object):

    def __init__(self, host=None):
        '''初始化'''
        self.host = host

    def step_org_create_cloud_host(self):
        print('这里不是创建云主机的')
        return self.host

    # def step_create_cloud_host(self):
    #     print('这里创建的')
    #     return self.host