import numpy as np


class Graph(): 
    def __init__(self, vertices):
        self.V=vertices 
        self.map= [
                    [0 for column in range(vertices)]
                    for row in range(vertices)
                    ]
        self.plate= [ [0 for column in range(3)]
                    for row in range(vertices +1)]
        self.plate[0][0]= "Node"
        self.plate[0][1]= "Dis"
        self.plate[0][2]= "prev"
        ver=['a      ', 'b      ', 'c      ', 'd      ', 'e      ','z      ']
        for i in range(len(ver)):
            self.plate[i+1][0]= ver[i]
    

    def minDistance(self,dist,sptSet):
        shortest_distance =9999
        
        
        for v in range(self.V):
            if dist[v]< shortest_distance and sptSet[v] ==False:
                shortest_distance = dist[v]
                shortest_distance_vertex = v
                ver=['a','b','c','d','e','z']
        return shortest_distance_vertex
    
    def dijkstraAlgo(self, src):
        dist = [9999]*self.V 
        dist[src]=0
        sptSet= [False]*self.V

        
        for cout in range(self.V):
            u= self.minDistance(dist, sptSet)
            sptSet[u] = True

            
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                            dist[v] = dist[u] + self.graph[u][v]
                            self.plate[v+1][1]= dist[v]
                            self.plate[v+1][2] = ver[u]

        print ("SPT: \n" ,np.matrix(self.plate))




map  = Graph(6)
map.graph = [
        [0, 4, 2, 0, 0, 0], 
        [4, 0, 1, 5, 0, 0], 
        [2, 1, 0, 8, 10, 0], 
        [0, 5, 8, 0, 2, 6], 
        [0, 0, 10, 2, 0, 5], 
        [0, 0, 0, 6, 5, 0] 
        ];

ver=['a','b','c','d','e','z']
for i in range(6):
    
    print("root node is ",ver[i])
    map.dijkstraAlgo(i);