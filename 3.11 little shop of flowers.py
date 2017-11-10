f,v=3,5
value=[[0]*(v+1) for _ in range(f+1)]
dp=[[0]*(v+1) for _ in range(f+1)]
for i in range(1,f+1):
    s=raw_input().split(' ')
    for j in range(1,v+1):
        value[i][j]=int(s[j-1])
for i in range(1,f+1):
    for j in range(i,v+i-f+1):
        lmax=0

        for k in range(j):
            if dp[i-1][k]>lmax:lmax=dp[i-1][k]
            #if value[i][k+1]>vmax:vmax=value[i][k+1]
        dp[i][j]=lmax+value[i][j]
vmax=0
for i in range(v+1):
    if vmax<dp[f][i]:vmax=dp[f][i]
print vmax