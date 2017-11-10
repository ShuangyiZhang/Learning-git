a,b=map(int,raw_input().split())
c=0
d=0
while d*d+d<=b:
    d+=1
while c*c<=a:
    c+=1

if c<=d:
    print "Vladik"
else:
    print "Valera"

