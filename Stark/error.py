import os
import numpy as np

#s_root = "/home/ryan/Stark/data/got10k/cir21/groundtruth.txt"
s_root = "/home/ryan/cir/test/cir22/groundtruth.txt"
p_root = "/home/ryan/Stark/test/tracking_results/stark_s/baseline_got10k_only/ep50/cir22.txt"


e = 0
N = 0
r = 5

with open(s_root) as count, open(s_root) as label_s, open(p_root) as label_p:
    for l1 in count:
    	l2 = label_s.readline()
    	l2_list = l2.split(',')
    	l3 = label_p.readline()
    	l3_list = l3.split('	')
    	#print(l2_list)
    	#print(l3_list)
    	x2,y2,w2,h2=l2_list[:] 
    	x2 = int(x2)+int(w2)/2
    	y2 = int(y2)+int(h2)/2
    	x3,y3,w3,h3=l3_list[:] 
    	x3 = int(x3)+int(w3)/2
    	y3 = int(y3)+int(h3)/2
    	e = e + np.sqrt(np.square(x2-x3)+np.square(y2-y3))
    	N = N +1
    	#print(N)
    	
    	

error = e/(N)
print(error)
em = error/r
print(em)
