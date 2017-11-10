s=raw_input()
l=len(s)
if l==1:
    print 1
else:
    s=s[1::]
    print 10**(l-1)-int(s)