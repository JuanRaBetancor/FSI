# Search methods
import search
ab = search.GPSProblem('A', 'B', search.romania)

print "***GRAPH SEARCH***"
print "El camino mas corto. Busqueda en anchura (graph search)"
lista=search.breadth_first_graph_search(ab).path()
lista.reverse()
print lista

print "\nEl camino mas largo. Busqueda en profundidad (graph search)"
lista=search.depth_first_graph_search(ab).path()
lista.reverse()
print lista

print "\nEl mas barato. Busqueda en ramificacion y acotacion (graph search)"
lista=search.ramum_et_vinctum_graph_search(ab).path()
lista.reverse()
print lista

print "\nEl mas barato. Busqueda en ramificacion y acotacion con heuristica (graph search)"
lista=search.ramum_et_vinctum_heuristic_graph_search(ab).path()
lista.reverse()
print lista

print "\n***TREE SEARCH***"
print "El mas barato. Busqueda en ramificacion y acotacion (tree search)"
lista=search.ramum_et_vinctum_tree_search(ab).path()
lista.reverse()
print lista

print "\nEl mas barato. Busqueda en ramificacion y acotacion con heuristica (tree search)"
print search.ramum_et_vinctum_heuristic_tree_search(ab).path()


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
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
#print search.astar_search(ab).path()

