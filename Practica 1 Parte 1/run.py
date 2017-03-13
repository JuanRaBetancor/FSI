# Search methods
import search
ab = search.GPSProblem('A', 'B', search.romania)

"""
1) Este va por el camino mas corto, es decir el que menos nodos usa para llegar al destino
"""
print "***GRAPH SEARCH***"
print "El camino mas corto. Busqueda en anchura (graph search)"
print search.breadth_first_graph_search(ab).path() 

"""
2)Este va por el camino mas largo, es decir el que mas nodos usa para llegar al destino
"""
print "\nEl camino mas largo. Busqueda en profundidad (graph search)"
print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
#print search.astar_search(ab).path()

'''
3)Este va por el camino mas barato,es decir el que menos coste almacena al llegar al destino
'''
print "\nEl mas barato. Busqueda en ramificacion y acotacion (graph search)"
print search.ramum_et_vinctum_graph_search(ab).path()

'''
print "\n***TREE SEARCH***"
print "El mas barato. Busqueda en ramificacion y acotacion (tree search)"
print search.ramum_et_vinctum_tree_search(ab).path()
'''

'''
EJEMPLOS
 1) El mas corto(anchura). 2) EL mas barato(ram-aco)
 Resultado de A->B:
 [<Node B>, <Node F>, <Node S>, <Node A>]: 211 + 99 + 140 = 450
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]: 101 + 97 + 80 + 140 = 418

 Resultado de O->B:
 [<Node B>, <Node F>, <Node S>, <Node O>]: 151 + 99 + 211 = 461
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node O>]: 151 + 80 + 97 + 101 = 429
 
 Resultado de N->A
 [<Node A>, <Node S>, <Node F>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
 = A->B = 450 + 85 + 142 + 92 + 87 = 856
 [<Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
 = A->B = 418 + 85 + 142 + 92 + 87 = 824
'''

