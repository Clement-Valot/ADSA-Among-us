class Graph:
  def __init__(self):
      #Dictionnaire de node avec node[name] = value
      self.dico_nodes = {}
      #Liste des edges
      self.list_edges = []

  def add_node(self, node):
      self.dico_nodes[node]= 0

  def add_edge(self, start_node, end_node, cost):
      self.list_edges.append((start_node, end_node, cost))

def remove_element(liste, node1, node2):
    for elements in liste:
        if elements[0] == node1 and elements[1] == node2:
            liste.remove(elements)
        if elements[0] == node2 and elements[1] == node1:
            liste.remove(elements)
    return liste


def dijsktra(graph, initial_node):
    graph.dico_nodes[initial_node] = 0
    for key, value in graph.dico_nodes.items():
        if(key != initial_node):
            graph.dico_nodes[key] = 1000
    list_of_edges = graph.list_edges
    visited = {initial_node : 0}
    #Tems qu'on a pas visité toutes les nodes, ou que la node final n'est pas atteinte
    while len(visited) != len(graph.dico_nodes):
        print("visited = {}".format(len(visited)))
        print("diconode = {}".format(len(graph.dico_nodes)))
        min_node_visited = None
        min_distance = 100
        distance = 0
        #Pour chaque node qui ont deja été visité:
        for node_key, node_value in visited.items():
            neighbour = []
            #On va regarder dans tous les edges qui sont les voisins de la node (sauf ceux deje enregistré)
            #On parcour la liste des edges
            for elements in list_of_edges:
                # Si le depart de l edge est la node dans visité, on l ajoute a voisin
                if elements[0] == node_key:
                    neighbour.append((elements[1], elements[2]))
                # Si le end de l edge est la node dans visité, on l ajoute a voisin
                if elements[1] == node_key:
                    neighbour.append((elements[0], elements[2]))
            # On parcour les voisins a la recherche du min
            for name_node_and_cost in neighbour:
                distance = node_value + name_node_and_cost[1]
                if distance < min_distance:
                    min_distance = distance
                    # Stock la node a ajouter dans visited
                    min_node_visited = (name_node_and_cost[0], distance)
                    # Stock la edge a retirer dans list_edge
                    min_edge = (node_key, name_node_and_cost[0])
        # On ajoute la nouvelle node dans les nodes visité
        visited[min_node_visited[0]] = min_node_visited[1]
        # On retire l'edge parcouru pour ne plus le parcourir
        list_of_edges = remove_element(list_of_edges, min_edge[0], min_edge[1])
    
    return visited



    # for edge in graph.edges[min_node]:
    #   weight = current_weight + graph.distance[(min_node, edge)]
    #   if edge not in visited or weight < visited[edge]:
    #     visited[edge] = weight
    #     path[edge] = min_node

if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("X")
    graph.add_node("U")
    graph.add_node("V")
    graph.add_node("Y")
    graph.add_edge("A","X",5)
    graph.add_edge("A","U",10)
    graph.add_edge("U","X",3)
    graph.add_edge("V","X",9)
    graph.add_edge("Y","X",2)
    graph.add_edge("Y","V",6)
    graph.add_edge("U","V",1)

    resultat = dijsktra(graph,"A")
    print(resultat)
