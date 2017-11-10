n,m=map(int,raw_input().split())
INF=5001
a=[0]*(n+1)
f=[INF]*(n+1)
for i in xrange(1,n+1):
    a[i],b=map(int,raw_input().split())
    start=1
    end=i
    while start<=end:
        middle=(start+end)/2
        if f[middle]>a[i]:
            end=middle-1
        else:
            start=middle+1
    f[start]=a[i]
for i in range(n,0,-1):
    if f[i]!=INF:
        print n-i
        break