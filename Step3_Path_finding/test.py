from Create_map_function import *

def remove_elements(liste, dict_visited):
    list_node_already_visited = []
    for key in dict_visited.keys():
        list_node_already_visited.append(key)
    for i in range(len(list_node_already_visited)):
        for j in range(i+1, len(list_node_already_visited)):
            for elements in liste:
                if elements[0] == list_node_already_visited[i] and elements[1] == list_node_already_visited[j]:
                    liste.remove(elements)
                if elements[0] == list_node_already_visited[j] and elements[1] == list_node_already_visited[i]:
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
        #Pour chaque node qui ont deja été visité:
        for node_key, node_value in visited.items():
            neighbour = []
            distance = 0
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
        list_of_edges = remove_elements(list_of_edges, visited)
    
    return visited



    # for edge in graph.edges[min_node]:
    #   weight = current_weight + graph.distance[(min_node, edge)]
    #   if edge not in visited or weight < visited[edge]:
    #     visited[edge] = weight
    #     path[edge] = min_node


if __name__ == "__main__":
    graph = Create_map_crewmate()

    resultat = dijsktra(graph,"RE")
    print(resultat)
