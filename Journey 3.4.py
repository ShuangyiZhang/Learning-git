n,m,t=map(int,raw_input().split())
graph=[[] for _ in xrange(m+2)]
#edges=[[] for _ in xrange(m+2)]
INF=10**9+1
dp=[[INF]*5000 for _ in range(5001)]
prev=[[0]*5000 for _ in range(5001)]
#deg=[0]*(n+2)
for i in xrange(1,m+1):
    a,b,c=map(int,raw_input().split())
    graph[a].append((b,c))
    #deg[b]+=1
#print graph,deg

#quene=[]
#for i in range(1,n+1):
#    for j in range(1,n+1):
#        if deg[j]==0:
#            break
#    deg[j]=-1
#    quene.append(j)
#    for k,l in graph[j]:
#        deg[k]-=1
#print quene
dp[1][1]=0
for i in range(2,n+1):
    for j in range(1,n):
        if dp[j][i-1]!=INF:
            for v,cost in graph[j]:
               if dp[v][i]>dp[j][i-1]+cost:
                   dp[v][i]=dp[j][i-1]+cost
                   prev[v][i]=j
for i in range(n,1,-1):
    if dp[n][i]<=t:
        print i
        ans=str(n)
        k=n
        for j in range(i,1,-1):
            ans+=str(prev[k][j])
            k=prev[k][j]
        print ans[::-1]
        break



