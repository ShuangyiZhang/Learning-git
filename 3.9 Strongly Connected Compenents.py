n,m=5,4
g=[[] for _ in range(n+1)]
gr=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    g[a]+=[b]
    gr[b]+=[a]
color=[-1]*(n+1)
f=[0]*(n+1)
d=[0]*(n+1)
a=list()


def dfs(i):
    color[i]=0
    a.append(' ')
    d[i]=len(a)
    for j in gr[i]:
        if color[j]==-1:dfs[j]
    color[i]=1
    a.append(' ')
    f[i]=len(a)
dfs(1)
print f
