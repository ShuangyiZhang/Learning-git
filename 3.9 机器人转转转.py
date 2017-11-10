w,h=4,4
s=[]
for i in range(w):
    s.append(raw_input())
    for j,c in enumerate(s[-1]):
        if c not in '.*':
            pos=(i,j,c)
dx={'U':0,'D':0,'L':-1,'R':1}
dy={'U':1,'D':-1,'L':0,'R':0}
rt={'U':'R','D':'L','L':'U','R':'D'}
states=[]
path=[]
ans=0
while pos not in states:
    states.append(pos)
    if (pos[0],pos[1]) not in path:
        path.append((pos[0],pos[1]))
        ans+=1
    new=(pos[0]+dx[pos[2]],pos[1]+dy[pos[2]],pos[2])
    if 0<=new[0]<w and 0<=new[1]<h and s[new[0]][new[1]]!='*':
        pos=new
    else:
        pos=(pos[0],pos[1],rt[pos[2]])
print path,ans