years=[0]*100
for i in range(1,10):
    years[i]=i
for i in range(2,11):
    for j in range(1,10):
        years[9*(i-1)+j]=years[9*(i-2)+j]*10
s=int(raw_input())
head=1
tail=90
while head<tail:
    mid=(head+tail)/2

    if s>=years[mid]:
        head=mid+1
    else:
        tail=mid-1
print years[head]-s