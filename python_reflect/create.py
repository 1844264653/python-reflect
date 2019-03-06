#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 22:22
# @Author  : 海心
# @Site    : 
# @File    : create.py
# @Software: PyCharm
# @descri  : 继承父类创建

from python_reflect.meta_create import Step_org_create_cloud_host
from python_reflect.middleware import use_admin_step_fun


class Stepcareate(Step_org_create_cloud_host):

    """模拟定义一个创建云主机的方法  继承父类就ok"""
    @use_admin_step_fun("admin_client_name", "org_client_name")
    def step_org_create_cloud_host(self):
        pass


def step_create_cloud_host():
        print('我被调用了')