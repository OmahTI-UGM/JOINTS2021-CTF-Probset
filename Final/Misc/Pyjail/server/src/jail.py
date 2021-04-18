#!/usr/bin/env python
import os
import sys
import enum

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas + '\n')
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

class A(enum.Enum):
    attr = None

banned = list('"!#$&\'()*+-/:<=>?@\^`{|}~')
banned += ['import', 'enum', 'banned', 'eval', 'fork']
banned += ['exec', 'open', 'locals', 'globals', 'dir']
banned += ['__file__', '__builtins__', '__doc__']

stdout = Unbuffered(sys.stdout)
stdout.write('>>> ')
msg = raw_input()

for b in banned:
    if b in msg:
        stdout.writelines('Illegal character!')
        sys.exit()

try:
    exec(msg)
except:
    pass
