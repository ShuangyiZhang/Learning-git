n=int(raw_input())
t=[0]*(n+1)
c=[0]*(n+1)
INF=10**9
dp=[INF]*(n+1)
for i in range(1,n+1):
    x,y=map(int,raw_input().split())
    t[i]=x+1
    c[i]=y
dp[0]=0
for i in range(1,n+1):
    for j in range(n,-1,-1):
        tn=min(n,j+t[i])
        dp[tn]=min(dp[tn],dp[j]+c[i])
        print tn,dp[tn],
    print