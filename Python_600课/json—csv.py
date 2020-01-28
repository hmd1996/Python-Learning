
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

# 获取ｊｓｏｎ数据
import json

with open('json.txt', 'r') as f:
    rows = json.load(f)

# 创建文件对象
f = open('data.csv', 'w')

# 通过文件创建csv对象
csv_write = csv.writer(f)

# 关闭打开的文件
f.close()
