n,m=map(int,raw_input().split())
a=[[0]*101 for _ in range(n+1)]
b=[0]*(n+1)
dp=[0]*(m+1)
for i in range(1,n+1):
    s=raw_input().split()
    k=int(s[0])
    b[i]=k
    for j in range(1,k+1):
        maxk = 0

        for p in range(0,j+1):
           su = 0
           for q in range(1,p+1):
               su+=int(s[q])
           for q in range(k,k-j+p,-1):
               su+=int(s[q])
           if su>maxk:maxk=su
        a[i][j]=maxk
if m>b[1]:
    for i in range(1,b[1]+1):
        dp[i]=a[1][i]
    for i in range(b[1]+1,m+1):
        dp[i]=dp[b[1]]
else:
    for i in range(1,m+1):
        dp[i]=a[1][i]
for i in range(2,n+1):
    for j in range(m,0,-1):
        maxf=0
        for k in range(b[i]+1):
            if j<k:break
            if dp[j-k]+a[i][k]>maxf:
                maxf=dp[j-k]+a[i][k]
        dp[j]=maxf
print dp[m]



