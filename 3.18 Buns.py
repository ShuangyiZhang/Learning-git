n,m,c0,d0=map(int,raw_input().split())
a=[0]*(m+1)
b=[0]*(m+1)
c=[0]*(m+1)
d=[0]*(m+1)
f=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    a[i],b[i],c[i],d[i]=map(int,raw_input().split())
for i in range(1,n+1):
    f[0][i]=(i//c0)*d0
for i in range(1,m+1):
    for j in range(1,n+1):
        kmax=min((j//c[i]),(a[i]//b[i]))
        t=0
        for k in range(kmax+1):
           if f[i-1][j-k*c[i]]+k*d[i]>t:
               t=f[i-1][j-k*c[i]]+k*d[i]
        f[i][j]=t
print f[m][n]



