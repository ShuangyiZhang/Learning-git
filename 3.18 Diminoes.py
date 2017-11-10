n=int(raw_input())
bar=5000
maxn=2*bar+1
INF=10**5
c=[0]*(n+1)
dp=[[INF]*maxn for _ in range(n+1)]
s=0
for i in range(1,n+1):
    a,b=map(int,raw_input().split())
    c[i]=a-b
    s+=abs(c[i])
dp[1][bar+c[1]]=0
dp[1][bar-c[1]]=1
for i in range(2,n+1):
    for j in range(bar-s,bar+s+1):
        dp[i][j]=min(dp[i-1][j-c[i]],dp[i-1][j+c[i]]+1)
for i in range(bar,maxn):
    if dp[n][i]!=INF or dp[n][2*bar-i]!=INF:
       print min(dp[n][i],dp[n][2*bar-i]),abs(i-bar)
       break
