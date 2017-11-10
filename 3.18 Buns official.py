n,m,c0,d0=map(int,raw_input().split())
dp=[0]*(n+1)
for i in range(c0,n+1):
    dp[i]=dp[i-c0]+d0
for k in range(m,0,-1):
    a,b,c,d=map(int, raw_input().split())
    for i in range(a/b):
        for j in range(n,c-1,-1):
            dp[j]=max(dp[j],dp[j-c]+d)
        print dp
