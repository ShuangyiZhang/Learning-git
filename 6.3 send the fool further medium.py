from heapq import heapify,heappop,heappush,nlargest
n,k=map(int,raw_input().split())
graph=[[] for _ in range(n+1)]
for i in range(1,n):
    u,v,c=map(int,raw_input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))
def dfs(i):
    size=max(len(graph[i]),k)
    a=[]
    for j,c in graph[i]:
        a.append((dfs(j),c))
    b=nlargest(size,a)
    sum=0
    for l in range(size):
        sum+=b[l][1]
