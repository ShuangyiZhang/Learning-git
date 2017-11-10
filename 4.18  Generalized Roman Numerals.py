s=raw_input()
l=len(s)
def number(x):
    if x=='I':return 1
    if x=='V':return 5
    if x=='X':return 10
    if x=='L':return 50
    if x=='C':return 100
def union(x,y):
    q=[]
    for v in x:
        for w in y:
            if v>=w:
                ab=v+w
                q.append(ab)
            else:
                ab=w-v
                q.append(ab)
    return q
ss=[]
f=[[[] for _1 in range(l+1)] for _2 in range(l+1)]
for i in range(l):
    t=number(s[i])
    ss.append(t)
    f[i][i].append(t)
for i in range(1,l):
    for j in range(l-i):
        k=i+j
        sets=[]
        for m in range(j,k):
            for n in union(f[j][m],f[m+1][k]):
                if n not in sets:
                    sets.append(n)
        f[j][k]=sets
print f[0][l-1]

