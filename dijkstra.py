from queue import PriorityQueue

class Graph:            ## classe grafo [rappresenta la rete]
    def __init__(self, num_of_vertices):        ## costruttore della classe
        self.v = num_of_vertices           ## [v] rappresenta il numero di nodi del grafo
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]     ## [endges] rappresenta la lista di percorsi tra i nodi sotto forma di matrice inizialmente creata con elementi tutti a '-1'
        self.visited = []       ## lista dei nodi visitati

    def add_edge(self, u, v, weight):           ## metodo per l'aggiunta del percoso tra due nodi
        self.edges[u][v] = weight           ## [u] [v] sono i nodi tra cui vi è il collegamento
        self.edges[v][u] = weight



def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}      ## lista di lunghezza [v] nodi inizializata tutta a infinito
    D[start_vertex] = 0         ## nodi iniziale impostato a 0

    pq = PriorityQueue()        ## coda prioritaria con solo il nodi di partenza alla locazione 0
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()       ## prendiamo le informazioni dal nodo [distanza e nodo]
        graph.visited.append(current_vertex)    ## segnamo il nodo come visitato

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:     ## se tra il nodo corrente e il suo vicino c'è un collegamento allora distanza = costo del percorso
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:       ## se il nodo NON è stato visitato
                    old_cost = D[neighbor]                      ## prendiamo il costo precedente e quello del nuovo percorso
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:             ## se il percorso nuovo è migliore inseriamo il costo per raggiungere il vicino e cambiamo il costo del nodo nel grafo
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D
    

g = Graph(8)            ## creamo il grafo con 8 vertici/nodi
g.add_edge(0, 1, 6)         ## aggiungiamo i collegamenti tra i nodi con relativo costo
g.add_edge(0, 3, 3)
g.add_edge(0, 4, 5)
g.add_edge(1, 2, 7)
g.add_edge(2, 4, 7)
g.add_edge(2, 6, 4)
g.add_edge(3, 7, 6)
g.add_edge(4, 5, 9)
g.add_edge(4, 7, 2)
g.add_edge(5, 6, 3)
g.add_edge(5, 7, 1)

D = dijkstra(g, 0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])