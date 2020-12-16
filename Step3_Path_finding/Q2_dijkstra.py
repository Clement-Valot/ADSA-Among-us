'''
#* Allows dijkstra function to remove all the edges that we won't need to look over again
#* So the goal here is to remove all the edges between the node that are already visited
#* because we don't want to visit them, it will make dijkstra program doesn't work otherwise

#? liste : liste of element to remove
#? dict_visited : dictionnary of already visited node in dijkstra algorithm 

#? return the modified list of edge without the useless edges
'''
def remove_elements(liste, dict_visited):
    # We create a list to store the name of the node that are already visited
    list_node_already_visited = []
    for key in dict_visited.keys():
        list_node_already_visited.append(key)
    # We want to browse the list of node and make every pair possible between nodes 
    # in order to compare the pair of node with the edges that really exist in the list
    # If the pair of node is in the list of edge that exist, we have to remove it
    for i in range(len(list_node_already_visited)):
        for j in range(i+1, len(list_node_already_visited)):
            for elements in liste:
                if elements[0] == list_node_already_visited[i] and elements[1] == list_node_already_visited[j]:
                    liste.remove(elements)
                if elements[0] == list_node_already_visited[j] and elements[1] == list_node_already_visited[i]:
                    liste.remove(elements)
    return liste

'''
#* Allows to run the dijkstra program on a graph from an initial node

#? grah : graph to perfom the dijsktra algorithm
#? initial_node : node you want to take as initial to perform the dijsktra algorithm

#? return the dictionnary visited which contain the name of all the node associated with their cost
#? the cost represent the cost from the initial node to the node in the dictionnary
'''
def dijsktra(graph, initial_node):
    # We initialize our variable for dijkstra algorithm
    # Value of initial node equal 0 and the rest equal infinity (here 1000 is sufficient)
    graph.dico_nodes[initial_node] = 0
    for key, value in graph.dico_nodes.items():
        if(key != initial_node):
            graph.dico_nodes[key] = 1000
    # We copy the list of edges in order not to modify the original one (because we are going to use it several time)
    list_of_edges = []
    for element in graph.list_edges:
        list_of_edges.append(element)
    # We create the dictionnary of alreday visited node
    # This dictionnary will contain the final result (node with their cost)
    visited = {initial_node : 0}
    # While we did't visited all the node, we continue our research
    while len(visited) != len(graph.dico_nodes):
        min_node_visited = None
        min_distance = 100
        # For each node that are already visited (we are going to look at the cost of their neighbour)
        for node_key, node_value in visited.items():
            neighbour = []
            distance = 0
            # We look at every edges of the node (so at all his neighbour, except the one remove because already visited)
            for elements in list_of_edges:
                # If the start node of the edge is the node we visit, it means the end node is a neighbour
                # therefore we add the edge to the list of neighbour
                if elements[0] == node_key:
                    neighbour.append((elements[1], elements[2]))
                # If the end node of the edge is the node we visit, it means the start node is a neighbour
                # therefore we add the edge to the list of neighbour
                if elements[1] == node_key:
                    neighbour.append((elements[0], elements[2]))
            # We visit the neighbour in the search of the minimum edge
            for name_node_and_cost in neighbour:
                # The distance is the distance already traveled + the edge 
                # between the node already visited and the neighbor (adjacent room)
                # The distance already traveled is the cost of the node
                distance = node_value + name_node_and_cost[1]
                # If it is indeed a minimum
                if distance < min_distance:
                    min_distance = distance
                    # We store the node
                    min_node_visited = (name_node_and_cost[0], distance)
                    # We store the edge
                    min_edge = (node_key, name_node_and_cost[0])
        # Once we have the minimum node we store it in the visited list with his cost
        visited[min_node_visited[0]] = min_node_visited[1]
        # Then we remove the edge so we don't visit it again
        # With this function we also remove all the edge that connect the nodes that are in visited
        list_of_edges = remove_elements(list_of_edges, visited)
    
    return visited
