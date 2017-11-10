n,k=map(int,raw_input().split())
res=1
if k>=2:
    res+=n*(n-1)/2
if k>=3:
    res+=n*(n-1)*(n-2)/3
if k>=4:
    res+=n*(n-1)/2*(n-2)*(n-3)/4*3
print res