#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

Dirs=[]
src=os.getenv("HOME")
print(src)
src+="/data/prod"
dest = os.getenv("HOME")
dest+="/data/prod_backup"

Dirs = next(os.walk(src))[1]


def rsync_dir(name_dir):
    subprocess.call(["rsync", "-arq", src+"/"+name_dir, dest])

p = Pool(len(Dirs))
p.map(rsync_dir,Dirs)

