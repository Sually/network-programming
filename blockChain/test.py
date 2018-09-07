# -*- coding: utf-8 -*-
import random, sys, fns, hashlib, time
from broadcast import Broadcaster

num = 3
cid = []
for i in range(num):
    cid.append(hashlib.sha256(str(random.randint(0,600000)+i*600001)).hexdigest())
print cid

rnd = ''
for i in range(100):
    rnd += str(random.randint(0, 100) % num)
print rnd

Broadcaster().broadcast('deadbeef'*8 + ' ' + str(888888) + ' ' + 'deadbeef'*8)