n=int(raw_input())
f=[0]*(n+1)
f[1]=1
INF=10**9
for i in range(2,n+1):
    j=int(i**.5)
    minx=INF
    for k in range(1,j+1):
        if f[i-j**2]+1<minx:
            minx=f[i-j**2]+1
    f[i]=minx
print f[n]

