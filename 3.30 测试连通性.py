n,m=map(int,raw_input().split())
graph=[[] for _ in range(n+1)]
def dfs(i):
    for v,num in graph[i]:
        if v not in g and (num<l or num>r):
            g.append(v)
            dfs(v)
for i in range(1,m+1):
    a,b=map(int,raw_input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))
k=int(raw_input())
ans=[0]*(k)
for i in range(1,k+1):
    l,r=map(int,raw_input().split())
    #for j in range(n+1):
    #    visited[j]=-1
    g=[]
    s=0
    for j in range(1,n+1):
        if j not in g:
            dfs(j)
            s+=1
    ans[i-1]=s
for i in range(k):
    print ans[i]
