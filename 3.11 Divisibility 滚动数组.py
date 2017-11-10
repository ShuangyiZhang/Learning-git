n,k=map(int,raw_input().split())
s=raw_input().split(' ')
a=[0]*(n+1)
f=[[0]*k for _ in range(2)]
for i in range(n):
    a[i]=int(s[i])%k
f[0][a[0]]=1
z=0
for i in range(1,n):
    zz=1 and (not z)
    for j in range(k):
        if f[z][j]==1:
            j1=(j+a[i])%k
            j2=(j-a[i]+k)%k
            f[zz][j1]=1
            f[zz][j2]=1
        f[z][j]=0
    z=zz
if f[zz][0]==1:
    print 'Divisible'
else:
    print 'Not divisible'