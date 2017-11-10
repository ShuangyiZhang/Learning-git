n=3
s=raw_input().split()
#print s
INF=10**4
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    dp[i][i]=1
for l in range(1,n):
    for i in range(n-l):
        j=i+l
        a=INF
        if s[i]==s[i+1]:
            #if i == 1 and j == 2: print a, dp[i + 1][j], dp[i + 2][j], s[1], s[2]

            a=dp[i+2][j]+1
            #if i == 1 and j == 2: print a, dp[i + 1][j], dp[i + 2][j], s[1], s[2]

        else:
            a=dp[i+1][j]+1
        #if i==1 and j==2:print a,dp[i+1][j],dp[i+2][j],s[1],s[2]
        if l>1:
            for k in range(i+2,j+1):
                if s[i]==s[k]:
                    a=min(a,dp[i+1][k-1]+dp[k+1][j])
                #if i == 1 and j == 2: print a

        dp[i][j]=a
        #print i,j
print dp[0][n-1]