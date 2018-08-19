# -*- coding: utf-8 -*-
__author__ = 'QB'
from celery import task
import time


def tasktest():
    print("good")
    time.sleep(5)  # 模拟耗时操作
    print("nice")
