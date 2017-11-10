n,m=map(int,raw_input().split())
edges=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    edges[a]+=[b]
    edges[b]+=[a]
dist=[-1]*(n+1)
for i in range(1,n+1):
    if dist[i]==-1:
        dist[i]=True
        q=[i]
        while q:
            x=q.pop(-1)
            for v in edges[x]:
                if dist[v]==-1:
                    dist[v]=not(dist[x])
                    q.append(v)
print dist
flag=1
for i in range(1,n+1):
    for v in edges[i]:
        if dist[v]==dist[i]:
            flag=0
if flag:
    a=''
    b=''
    for i in range(1,n+1):
        if dist[i]==1:
            a+=str(i)+' '
        else:
            b+=str(i)+' '
    print a
    print b