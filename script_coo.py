#!/usr/bin/env python3
import sys
import tqdm
# ~ from collections import Counter
try:fn=sys.argv[1]
except:fn=0
class read:
	all = []
	km=10
	KMR={}
	def __init__(self,l):
		c,s = l.split()
		c = int(c)
		self.c = c 
		self.s = s.strip()
		self.l=len(s)
		self.index = len(read.all)
		read.all.append(self)
		self.dkm()
	def amiinclude(me,other):
		return other.s.count(me.s) 
	def amiinter(me):
		mfkm=me.s[:read.km]
		valid=read.KMR[mfkm]
		valid=[r for r in valid if r.l>me.l]
		# ~ return [other for other in read.all[me.index+1:] if me.amiinclude(other)] 
		return [other for other in valid if me.amiinclude(other)] 
	def dkm(me):
		k=read.km
		ckm="_"+me.s[:k-1]
		for c in me.s[k-1:]:
			ckm=ckm[1:]+c
			if ckm in read.KMR:
				read.KMR[ckm].add(me)
			else:
				t=set()
				t.add(me)
				read.KMR[ckm]=t

for l in open(fn):read(l)
# ~ print(len(read.all))
# ~ print(len(read.KMR))
# ~ print(read.KMR.keys())
# ~ print(list(read.KMR.keys())[:10])
# ~ for k in list(read.KMR.keys())[:10]:
	# ~ print(k,len(read.KMR[k]))
read.all.sort(key=lambda t:t.l)
for i,r in enumerate(read.all):r.index=i
CLEAN=[]
merged=unaffected=0
for r in tqdm.tqdm(read.all):
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
print(f"{merged} merged reads, {unaffected} final reads")
ro=[r for r in CLEAN if r.c==1]
print(len(ro),"reads seen atmost once only, that might need correction")
ro=[r for r in CLEAN if r.c<=2]
print(len(ro),"reads seen atmost 2x only, that might need correction")
ro=[r for r in CLEAN if r.c<=3]
print(len(ro),"reads seen atmost 3x only, that might need correction")
ro=[r for r in CLEAN if r.c>=100]
print(len(ro),"reads seen more than 100x")
        
   
