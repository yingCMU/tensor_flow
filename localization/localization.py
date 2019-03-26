# uniform distribution
p = []
n = 5
for _ in range(n):
    p.append(1./n)

print sum(p)


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

# move (exact motion)
def move(p,U):
    q = []
    # another way
    # U = U % len(p)
    # q = p[-U:] + p[:-U]
    for i in range(len(p)):
        q.append(p[(i-U)%len(p)])
    return q

# move (inexact motion)
def move(p,U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)]
        s = s + pOvershoot * p[(i-U-1)%len(p)]
        s = s + pUndershoot * p[(i-U+1)%len(p)]
        q.append(s)
