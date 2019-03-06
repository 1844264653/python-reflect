#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 22:31
# @Author  : 海心
# @Site    : 
# @File    : middleware.py
# @Software: PyCharm
# @descri
import json
import re


# class Strings(object):
#     def __init__(self):
#         super().__init__()
#
#     def __call__(self, *args, **kwargs):
#         pass


def use_admin_step_fun(admin_client_name,org_client_name):
    def change_client(fn):
        def wrapper(self, **kwargs):
            from python_reflect.create import step_create_cloud_host
            admin_client = None
            try:
                # admin_client =getattr(self, admin_client_name)   # 这里相当于 self.admin_client_name
                # org_client = getattr(self, org_client_name)  # 这里相当于  self.org_client_name
                # setattr(self, admin_client_name, org_client) # 相当于 self.admin_client_name = org_client
                new_fn_name = re.sub("step_org", "step", fn.__name__)
                #分析一下这个   fn.__name__  表示取这个函数的名字  = step_org_create_cloud_host
                #  sub  表示  匹配  fn.__name__  中的  step_org  换成  step  ----> step_reate_cloud_host

                setattr(self,new_fn_name, new_fn_name)  #  因为只是小部分代码  自己加的这句 防止报错
                # 实际上 getattr  就是 python的自省机制和反射

                new_fn = getattr(self, new_fn_name)
                new_fn = eval(new_fn)

                print(new_fn,type(new_fn))
                ret = new_fn(**kwargs)
                #  看看这个地方  利用了python的反射机制取调用函数  在大项目里隐藏的好
                #  ret = self.step_create_cloud_host()   !!! 这里开始调用函数
                return ret
            finally:
                if admin_client is not None:
                    setattr(self, admin_client_name, admin_client)


        return wrapper



    return change_client