parent=dict()
rank=dict()
def make_set(vertice):
    parent[vertice]=vertice
    rank[vertice]=0
def find(vertice):
    if parent[vertice]!=vertice:
        parent[vertice]=find(parent[vertice])
    return parent[vertice]
def union(vertice1,vertice2):
    root1=find(vertice1)
    root2=find(vertice2)
    if root1!=root2:
        if rank[root1]>rank[root2]:
            parent[root2]=root1
        else:
            parent[root2]=root2
            if rank[root1]==rank[root2]:rank[root2]+=1
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    MTS=set()
    edges=list(graph['edges'])
    edges.sort()
    for edge in edges:
        w,v1,v2=edge
        if find(v1)!=find(v2):
            union(v1,v2)
            MTS.add(edge)
    return MTS
