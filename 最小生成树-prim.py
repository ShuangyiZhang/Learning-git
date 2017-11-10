import heapq
m=5
n=6
dist=[-1]*(n+1)
visited=[False]*(n+1)
parent=[0]*(n+1)
edges={i:[] for i in range(1,n+1)}
for i in range(m):
    u,v,s=map(int,raw_input().split())
    edges[u].append((v,s))
    edges[v].append((u,s))
tovisit=[(0,1,0)]
while len(tovisit)>0:
    cost,node,par=heapq.heappop(tovisit)
    if visited[node]:continue
    visited[node]=True
    dist[node]=cost
    parent[node]=par
    if node==n:break
    for adj,extra in edges[node]:
        if not visited[adj]:
            heapq.heappush(tovisit,(extra,adj,node))
