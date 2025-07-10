class graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range(vno)]

    def addedge(self,u,v,weight=1):
        if self.vertex_count>u>=0 and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight

        else:
            print("invalid vertex")

    def removeedge(self,u,v):
        if self.vertex_count>u>=0 and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0

        else:
            print("invalid vertex")

    def hasedge(self,u,v):
        if self.vertex_count>u>=0 and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        
    def print_adjmatix(self):
        for rowlist in self.adj_matrix:
            print(" ".join(map(str,rowlist)))

f1=graph(5)
f1.addedge(0,1,1)

f1.print_adjmatix()