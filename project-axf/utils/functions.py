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
