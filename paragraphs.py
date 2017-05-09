#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('N', type=int)
args = parser.parse_args()

pp = sys.stdin.read().split('\n\n')
p = pp[args.N-1].strip()
for l in p.split('\n'):
    #if l[0] == '#':
    #    continue
    print(l)
