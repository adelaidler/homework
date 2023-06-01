#!/usr/bin/python
# Example Python script

import sys

argc = len(sys.argv)

if argc > 1:
    print('too many args')

else:
    where = 'world'
    print("hello", where)

print('goodby from' + sys.argv[0])




