n=3
t=[0]*(n+1)
c=[0]*(n+1)
#MAXN=10**4
INF=10**4
dp=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    x,y=map(int,raw_input().split())
    t[i]=x+1
    c[i]=y
    dp[i][0]=0
#print c
dp[1][t[1]]=c[1]
for i in range(2,n+1):
    for j in range(1,n+1):
        if j-t[i]>=0:
            s=j-t[i]
        else:s=0
        dp[i][j]=min(dp[i-1][j],dp[i-1][s]+c[i])
            #print '1',dp[i][j]
        #else:
        #    dp[i][j]=dp[i-1][j]
print dp[n][n]
#print dp[1][1],dp[2][1],dp[2][2],dp[3][1],dp[3][2],dp[3][3]