m=6
n=5
#dist=[-1]*(n+1)
visited=[False]*(n+1)
edges=[[] for i in range(1,m+1)]
for i in range(m):
    u,v=map(int,raw_input().split())
    edges[u].append(v)
def dfs(i):
    for j in edges[i]:
        if visited[j]==False:
            visited[j]=True
            print j
            dfs(j)
visited[1]=True
dfs(1)
