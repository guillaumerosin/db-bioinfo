#!/usr/bin/env python3
import sys
# ~ from collections import Counter
try:fn=sys.argv[1]
except fn=0
class read:
    all = []
    def __init__(self,l):
        c,s = l.split()
        c = int(c)
        self.c = c 
        self.s = s
        self.index = len(read.all)
        read.all.append(self)

    def amiinclude(me,other):
        return other.s.count(me.s) 

    def amiinter(me):
        return [other for other in read.all if me.amiinclude(other) and me != other] 
    

for l in open(fn):read(l)
print(len(read.all))

for fr in read.all:
    resultat = fr.test()
    if resultat:print(fr.index,[x.index for x in resultat])


        
   

# for seq in fr.test():
#     fr in read.all < 1


        
   
