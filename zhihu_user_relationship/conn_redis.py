#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:12
# @Author  : Sa.Song
# @Desc    : 
# @File    : conn_redis.py
# @Software: PyCharm
from redis import Redis

import redis

def get_link(ip='127.0.0.1', port=6379):
    redis_pool = redis.ConnectionPool(host=ip, port=port, max_connections=20)  # 创建一个连接池
    conn = redis.Redis(connection_pool=redis_pool,decode_responses=True)  # 从池子里边起一个链接
    return conn
    # print(conn.get('myKey').decode('utf-8'))
