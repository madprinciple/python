#!/usr/bin/env python

#Python wrapper for the ls command


import subprocess

for x in range(0, 3):
    print "hi"
    subprocess.call(["ls","-l"])
