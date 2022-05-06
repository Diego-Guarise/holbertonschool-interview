#!/usr/bin/python3
'''
Log parsing
'''


import re
import sys


lines = 1
size = 0
status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
          '404': 0, '405': 0, '500': 0}
input = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}.+')

for line in sys.stdin:
    if input.match(line.strip()) is None:
        break
    array = line.split(' ')
    size += int(array[-1])

    for key in status.keys():
        if key == array[-2] and isinstance(status[key], int):
            status[key] += 1

    if lines % 10 == 0:
        print('File size: {}'.format(size))
        for key, value in status.items():
            if value:
                print('{}: {}'.format(key, value))
    lines += 1
