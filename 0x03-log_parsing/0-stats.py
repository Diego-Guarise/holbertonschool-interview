#!/usr/bin/python3
'''
Log parsing
'''


import sys


lines = 1
size = 0
status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
          '404': 0, '405': 0, '500': 0}
input = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for line in sys.stdin:
        lines += 1
        if len(line.split(' ')) > 2:
            size += int(line.split(' ')[-1])
            if line.split(' ')[-2] in status:
                status[line.split(' ')[-2]] += 1
        if lines % 10 == 0:
            print('File size: {}'.format(lines))
            for tmp in input:
                if status[tmp] != 0:
                    print('{}: {}'.format(tmp, status[tmp]))
except KeyboardInterrupt:
    pass
finally:
    print('File size: {}'.format(size))
    for tmp in input:
        if status[tmp] != 0:
            print('{}: {}'.format(tmp, status[tmp]))
