n=7
s=raw_input().split()
INF=10**4
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    dp[i][i]=1
    if i<n-1:
       if s[i]==s[i+1]:
           dp[i][i+1]=1
       else:
           dp[i][i+1]=2
for l in range(2,n):
    for i in range(n-l):

        j=i+l
        #if dp[i][j]==1:continue
        a=INF

        #if i==1 and j==2:print a,dp[i+1][j],dp[i+2][j],s[1],s[2]

        for k in range(i,j):

            a=min(a,dp[i][k]+dp[k+1][j])
                #if i == 1 and j == 2: print a
        if s[i]==s[j]:a=min(a,dp[i+1][j-1])
        dp[i][j]=a
print dp