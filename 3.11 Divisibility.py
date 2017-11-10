n,k=map(int,raw_input().split())
s=raw_input().split(' ')
a=[0]*(n+1)
f=[[0]*k for _ in range(n+1)]
for i in range(n):
    a[i]=int(s[i])%k
f[0][a[0]]=1
for i in range(1,n):
    for j in range(k):
        if f[i-1][j]==1:
            j1=(j+a[i])%k
            j2=(j-a[i]+k)%k
            f[i][j1]=1
            f[i][j2]=1
if f[n-1][0]==1:
    print 'Divisible'
else:
    print 'Not divisible'


