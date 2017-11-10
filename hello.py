def insert(alist):
    for i in range(len(alist)):
        p=i
        c=alist[i]
        while p>0 and alist[p-1]>c:
            alist[p]=alist[p-1]
            p-=1
        alist[p]=c
alist=[1,6,3,5,4,2,9,7,8,10]
insert(alist)
print alist