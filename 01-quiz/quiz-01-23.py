#!/usr/bin/env python

#Write code that makes the robot move twice and then prints 
#out the resulting distribution, starting with the initial 
#distribution p = [0, 1, 0, 0, 0]

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        qExact = p[(i-U) % len(p)] * pExact
        qOvershoot = p[(i-(U+1)) % len(p)] * pOvershoot
        qUndershoot = p[(i-(U-1)) % len(p)] * pUndershoot
        q.append(qExact + qOvershoot + qUndershoot)
    return q
    
p = move(p, 1)

print move(p,1)
