#!/usr/bin/env python3
import sys
import tqdm
# ~ from collections import Counter
try:fn=sys.argv[1]
except:fn=0
class read:
	all = []
	def __init__(self,l):
		c,s = l.split()
		c = int(c)
		self.c = c 
		self.s = s
		self.l=len(s)
		self.index = len(read.all)
		read.all.append(self)
	
	def amiinclude(me,other):
		return other.s.count(me.s) 
	
	def amiinter(me):
		return [other for other in read.all if me.amiinclude(other) and me != other] 
	

for l in open(fn):read(l)
print(len(read.all))
AR=list(read.all)
AR.sort(key=lambda t:t.l)
CLEAN=[]
merged=unaffected=0
# ~ while AR:
for r in tqdm.tqdm(AR):
	# ~ r=AR.pop(0)
	resultat = r.amiinter()
	if resultat:
		# ~ print(f"todo : {len(AR)} | merging {r.index} seen {r.c} times  to {len(resultat)} reads")
		tt=sum([other.c for other in resultat])
		for other in resultat:
			other.c+=r.c*other.c/tt
		merged+=1
	else:
		# ~ print(f"todo : {len(AR)} | leaving {r.index} seen {r.c} times unmerged")
		CLEAN.append(r)
		unaffected+=1
print("final read count",len(CLEAN))
print(f"{merged} merged reads, {unaffected} untouched reads")


        
   
