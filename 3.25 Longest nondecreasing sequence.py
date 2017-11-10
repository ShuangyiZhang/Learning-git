n=6
a=[0]*(n+1)
f=[0]*(n+1)
prev=[0]*(n+1)
for i in range(1,n+1):
    a[i]=int(raw_input())
    maxf=0
    for j in range(1,i):
        if a[i]>=a[j] and f[j]>maxf:
            maxf=f[j]
            prev[i]=j
    f[i]=maxf+1
maxf=max([f[i] for i in range(1,n+1)])
print maxf
for i in range(1,n+1):
    if f[i]==maxf:
        j=i
        s=[]
        while j>0:
           s.append(a[j])
           j=prev[j]
        print s[::-1]