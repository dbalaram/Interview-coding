# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

S = "23:59"

import itertools
l = []
for i in S:
    if i != ":":
        l.append(i)
        
value1 = int(l[0]+l[1])
value2 = int(l[2]+l[3])        
p = list(itertools.permutations(l))  
g = [] 
f = []
las = []
for count,i in enumerate(p):
    lis = list(i)
    first = int(lis[0]+ lis[1])
    last = int(lis[2]+ lis[3])
    
    if first < 24 and last <= 59:
        g.append(lis)
        f.append(first)
        las.append(last)
        
diff1 = []
diff2 = []       
for i in f:
    d = i - value1
    diff1.append(d)
    

for i in las:
    d = i - value2
    diff2.append(d) 
   
            
for count in range(len(diff1)):
    if diff2[count] < 0:
        diff2[count] += 60
        diff1[count] -=1
        if diff1[count] <= 0 :
            diff1[count] += 24
    if diff1[count] < 0:
        diff1[count] += 24
    if diff1[count]==0 and diff2[count]==0:
        diff1[count] = 24
dummy = []        

for i in range(len(diff1)):
        dummy.append(str(diff1[i])+ str(diff2[i]))  

m = dummy.index(min(dummy)) 
li = p[m]     
final = ''
for i in range(4):
    
    final = final+ li[i]
    if i==1:
        final = final +':'
        