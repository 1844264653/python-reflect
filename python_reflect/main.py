#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 22:54
# @Author  : 海心
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @descri

from python_reflect.create import Stepcareate



if __name__ == '__main__':
    stepcareate = Stepcareate('cloud')
    stepcareate.step_org_create_cloud_host()
   '''最终结果  ： <function step_create_cloud_host at 0x0000029B2B2A1F28> <class 'function'>
我被调用了'''