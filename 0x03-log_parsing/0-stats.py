#!/usr/bin/python3
'''
esto no anda ni loco jaja suerte
'''


import sys


i = 0
size = 0
status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
input = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        i += 1
        sp = line.split(' ')
        if len(sp) > 2:
            size += int(sp[-1])
            if sp[-2] in status:
                status[sp[-2]] += 1
        if i % 10 == 0:
            print("File size: {}".format(size))
            for tmp in input:
                if status[tmp]:
                    print("{}: {}".format(tmp, status[tmp]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(size))
    for tmp2 in input:
        if status[tmp2]:
            print("{}: {}".format(tmp2, status[tmp2]))
