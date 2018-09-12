# -*- coding: utf-8 -*-
__author__ = 'QB'
import random


def get_ticket():
    s = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    ticket = ''
    for i in range(30):
        # 获取随机的字符串
        ticket += random.choice(s)
    ticket = 'TK_' + ticket
    return ticket


def get_order_random_id():
    s = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    order_num = ''
    for i in range(30):
        order_num += random.choice(s)
    return order_num
