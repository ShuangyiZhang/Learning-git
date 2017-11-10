n,m=10,6
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    g[a]+=[b]
def d(i):
    if i in v:return
    v.append(i)
    for j in g[i]:
        d(j)
v=[]
for i in range(1,n+1):
    if i not in v:
        d(i)
        print v
