n=int(raw_input())
def f(i):
    if i==1:return 1
    if i==2:return 2
    a=1
    b=2
    for k in range(i-2):
        t=a+b
        a=b
        b=t
    return b
x=f(n-2)
y=f(n-1)
z=x+y
s=str(x*x*z*z*2+x*y*y*z*12+y*y*y*y*2+2)
l=len(s)
if l<=3:
    print s
else:
    p=l/3
    q=l%3
    #print p,q
    if q==0:
        print s[0]+s[1]+s[2],
        for i in range(1,p):
            print ','+s[3*i:3*i+3],
    elif q==1:
        print s[0],
        for i in range(0,p):
            print ','+s[(3*i+1):(3*i+4)],
    elif q==2:
        print s[0]+s[1],
        for i in range(0,p):
            print ','+s[(3*i+2):(3*i+5)],