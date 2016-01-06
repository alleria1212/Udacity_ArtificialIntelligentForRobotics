import numpy as np

p=[]
n=5
for i in range(n):
	p.append(1./n)

world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','red']
motions = [1,1]


pHit = 0.6
pMiss = 0.2
pUndershoot = 0.1
pOvershoot = 0.1
pExact = 0.8

def move(p, U):
	q =[]
	for i in range(len(p)):
		s = pOvershoot * p[(i-U-1)%len(p)]
		s = s+ pUndershoot * p[(i-U+1)%len(p)]
		s = s+ pExact * p[(i-U)%len(p)]
		q.append(s)
	return q

def sense(p, Z):
	q=[]
	for i in range(len(p)):
		hit = ( Z == world[i])
		q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
		s = sum(q)
	for i in range(len(p)):
		q[i] = q[i]/s
	return q

for k in range(len(measurements)):
	p = sense(p, measurements[k])
	p = move(p, motions[k])

print (move(p,1))