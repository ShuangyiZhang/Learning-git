n=8
prev=[0]*(n+1)
graph=[[] for _ in range(n+1)]
rank=[0]*(n+1)
for i in range(1,n):
    c,b=map(int,raw_input().split())
    graph[c].append(b)
    graph[b].append(c)
def dfs(k,s):
    for v in graph[k]:
        if v==s:continue
        if rank[v]==-1:
            rank[v]=rank[k]+1
            prev[v]=k
            #print v,rank[v]
            dfs(v,k)
times=int(raw_input())
for i in range(1,times+1):
    for j in range(1,n+1):
        rank[j]=-1
        prev[j]=j

    r,x,y=map(int,raw_input().split())
    rank[r] = 1
    dfs(r, r)
    print rank
    print prev
    if rank[x]>rank[y]:
        x,y=y,x
    while rank[y]>rank[x]:
        y=prev[y]
    if x==y:
        print x
    else:
        while prev[x]!=prev[y]:
            x=prev[x]
            y=prev[y]
        print prev[x]
