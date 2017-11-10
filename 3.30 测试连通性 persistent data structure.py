n,m=map(int,raw_input().split())
graph=[[[] for _ in range(n+2)] for __ in range(m+1)]
rgraph=[[[] for _ in range(n+2)] for __ in range(m+1)]
edges=[0]*(2*m+1)
for i in range(1,m+1):
    edges[i],edges[m+i]=map(int,raw_input().split())
for i in range(1,m+1):
    for j in range(1,i+1):
        graph[i][edges[i]].append((edges[m+i],i)) #不是append啊。。。
        graph[i][edges[m+i]].append((edges[i],i))
        rgraph[i][edges[m+1-i]].append((edges[2*m+1-i],i))
        rgraph[i][edges[m+1-i]].append((edges[2*m+1-i],i))
k=int(raw_input())
ans=[0]*(k)
for i in range(1,k+1):
    l,r=map(int,raw_input().split())
    g=graph[l-1]
    rg=rgraph[r+1]



for i in range(k):
    print ans[i]
