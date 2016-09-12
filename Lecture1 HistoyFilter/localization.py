#Markov Localization UDACITY  Lessin 1 - Localisation
import numpy as np

world = ['g','r','r','g','g']
measurements=['r','r','r','r']
motions = [1,1] #1 = move right
n=5;
p=[];

#measurement probability
pHit = 0.6
pMiss = 0.2

#inexact movement parameter
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

###initialize initial uniform distribution as an initial belief
def initialize(p,n):
	for i in range(n):
		p.append(1./n)
	return p

def sense(p, measurements):
	q = []
	for i in range(len(p)):
		hit = ( measurements == world[i])
		q.append( p[i] *  ( hit * pHit + (1-hit) * pMiss) )
	return q/np.sum(q)

#Move U times to the right (assume a cycle..for an array of size 5, a[5] -> a[0] for U = 1)
#Included uncertainties (Inexact move function)
def move(p, U):
	q = [0]*n
	for i in range(len(p)):
		index = ( i+U ) % len(p)
		indexOver = ( i+U+1 ) % len(p)
		indexUnder = ( i+U-1 ) % len(p)
		q[index] = q[index] + p[i] * 0.8
		q[indexOver] = q[indexOver] + p[i] * 0.1
		q[indexUnder] = q[indexUnder] + p[i] * 0.1 
	return q



p = initialize(p,n)
for i in range(len(motions)):
	p = sense(p,measurements[i])
	p = move(p,motions[i])

print p
