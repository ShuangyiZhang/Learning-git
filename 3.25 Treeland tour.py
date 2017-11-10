n=5
a=[0]*(n+1)
graph=[[] for _ in range(n+1)]
s=raw_input().split()
rank=[0]*(n+1)
for i in range(1,n+1):
    a[i]=int(s[i-1])
for i in range(1,n):
    c,b=map(int,raw_input().split())
    graph[c].append(b)
    graph[b].append(c)
def dfs(k,s):
    for v in graph[k]:
        if v==s:continue
        if rank[v]<rank[k]+1 and a[v]>a[k]:
            rank[v]=rank[k]+1
            #print v,rank[v]
            dfs(v,k)
ans=0
for i in range(1,3):
    for j in range(1,n+1):
        rank[j]=-1
    rank[i]=1
    dfs(i,i)
    #print rank
    for j in range(n,0,-1):
        if rank[j]!=-1:
            res=rank[j]
            break
    if res>ans:ans=res
print ans
