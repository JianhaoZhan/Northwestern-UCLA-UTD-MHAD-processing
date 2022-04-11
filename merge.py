# -*- coding: utf-8 -*-
import os

d = os.listdir()
l = []
for i in d :
    if i != 'merge.py':
        l.append(i)
l.sort()
with open('Northwestern-UCLA.tar.gz', 'ab') as f:
    for i in l:
        with open(i, 'rb') as j:
            f.write(j.read())
