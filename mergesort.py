def mergesort(alist):
    if len(alist)>1:
        left=alist[:len(alist)//2]
        right=alist[len(alist)//2:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                alist[k]=left[i]
                i=i+1
            else:
                alist[k]=right[j]
                j=j+1
            k=k+1
        if i<len(left):
            while i<len(left):
                alist[k]=left[i]
                i=i+1
                k=k+1
        if j<len(right):
            while j<len(right):
                alist[k]=right[j]
                j=j+1
                k=k+1
array=[1,5,3,7,9,8,2,6,90]
mergesort(array)
print array