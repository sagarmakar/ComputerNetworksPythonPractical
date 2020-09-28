def BellmanFord(graph, V, E, src): 

    dis = [9999] * (V+1)
    prev= [src] * (V+1)
    dis[src] = 0

    for i in range(V-1): 
        for j in range(E): 
            if dis[graph[j][0]]!=9999 and dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]: 
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2] 
                prev[graph[j][1]] = graph[j][0]


    for i in range(E): 
        x = graph[i][0] 
        y = graph[i][1] 
        weight = graph[i][2] 
        if dis[x] != 9999 and dis[x] + weight < dis[y]: 
            print("Graph contains negative weight cycle") 

    print("Vertex Distance from Source: "+ str(src)) 
    for i in range(1, V+1): 
        print("%d\t\t%d\t%d" % (i, dis[i], prev[i])) 

if __name__ == "__main__": 
    V = 7
    E = 10  
    graph = [[1, 2, 6], 
            [1, 3, 5], 
            [1, 4, 5], 
            [2, 5, -1], 
            [3, 5, 1],
            [3, 2, -2], 
            [4, 6, -1],
            [4, 3, -2], 
            [5, 7, 3], 
            [6, 7, 3]] 

    for i in range( 1, V+1):
        BellmanFord(graph, V, E, i) 
