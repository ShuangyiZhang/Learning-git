n,m=map(int,raw_input().split())
r=[]
a=[0]*n
for i in range(m):
    r.append(raw_input())
for i in range(n):
    a[i]=i+1
    j=i
    #print str(a[j])+' '+str(a[j-1])
    while (str(a[j-1])+' '+str(a[j])) in r and j>0:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
print a