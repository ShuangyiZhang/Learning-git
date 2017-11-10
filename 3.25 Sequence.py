n=5
a=[0]*(n+1)
maxn=5000
INF=100
b=[]
f=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n):
    x=int(raw_input())
    a[i]=x
    b.append(x)
b.sort()
#还可以去重
#还可以用一维数组刷
f[1][1]=abs(a[1]-b[0])
for i in range(2,n+1):
    f[1][i]=min(f[1][i-1],abs(a[1]-b[i-1]))
for i in range(2,n+1):
    for j in range(1,n+1):
        f[i][j]=min(f[i][j-1],f[i-1][j]+abs(a[i]-b[i-1]))
print f[n][n]

