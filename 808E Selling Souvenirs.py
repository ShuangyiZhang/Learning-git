n,m=map(int,raw_input().split())
a,b,c=[],[],[]
dp=[-1]*(m+1)
pointera=[-1]*(m+1)
pointerb=[-1]*(m+1)
pointerc=[-1]*(m+1)
for i in range(n):
    w,p=map(int,raw_input().split())
    if w==1:
        a.append(p)
    elif w==2:
        b.append(p)
    else:
        c.append(p)
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
dp[0]=0
#for i in range(len(a)):
#    if i+1<=m:
 #      dp[i+1]=dp[i]+a[i]
#print dp
#for i in range(2,m+1):
#    if pointer[i-2]<len(b)-1 and dp[i-2]!=-1:
#       if dp[i]<dp[i-2]+b[pointer[i-2]+1]:
#           dp[i] =dp[i - 2] + b[pointer[i - 2] + 1]
#           pointer[i]=pointer[i-2]+1
#       else:
#           pointer[i]=pointer[i-2]
#    else:
#        pointer[i]=pointer[i-2]
#print dp,pointer
#for i in range(m+1):
#    pointer[i]=-1
for i in range(1,m+1):
    #if i==1 and len(a)!=0:
    #    dp[1]=a[0]
     #   pointera[1]==0
    #elif i==2:
     #   if dp[1]+a[1]>b[0]:
     #       dp[2]=dp[1]+a[1]
     #       pointera[2]=1
     #   else:
     #       dp[2]=b[0]
    #        pointerb[2]=0
    #else:
        if i>=3 and pointerc[i-3]+1<=len(c)-1:
            x=dp[i-3]+c[pointerc[i-3]+1]
        else:
            x=0
        if i>=2 and pointerb[i - 2] + 1 <=len(b) - 1:
            y=dp[i-2]+b[pointerb[i-2]+1]
        else:
            y=0
        if pointera[i - 1] + 1 <=len(a) - 1:
            z=dp[i-1]+a[pointera[i-1]+1]
        else:
            z=0
        if x>y and x>z:
            dp[i]=x
            pointerc[i]=pointerc[i-3]+1
            pointerb[i]=pointerb[i-3]
            pointera[i]=pointera[i-3]
        elif y>z:
            dp[i]=y
            pointerb[i]=pointerb[i-2]+1
            pointerc[i]=pointerc[i-2]
            pointera[i]=pointera[i-2]
        else:
            dp[i]=z
            pointera[i]=pointera[i-1]+1
            pointerc[i]=pointerc[i-1]
            pointerb[i]=pointerb[i-1]
#    if pointer[i-3]<len(c)-1 and dp[i-3]!=-1:
#       if dp[i]<dp[i-3]+c[pointer[i-3]+1]:
#           dp[i] =dp[i - 3] + c[pointer[i - 3] + 1]
#           pointer[i]=pointer[i-3]+1
#       else:
#           pointer[i]=pointer[i-3]
#    else:
#        pointer[i]=pointer[i-3]
res=0
for i in range(m+1):
   if res<dp[i]:
       res=dp[i]
print res