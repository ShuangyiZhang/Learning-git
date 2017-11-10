def f(a,b):
    if not b:
        return (a,1,0)
    r,x,y=f(b,a%b)
    return (r,y,x-(a/b)*y)
print f(123,60)
