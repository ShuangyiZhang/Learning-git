n=int(raw_input())
s=[]
for i in range(n):
   s.append(raw_input())
s.sort()
ok=False
for i in range(1,n):
    if s[i].find(s[i-1])!=-1:
        ok=True
        break
print ok