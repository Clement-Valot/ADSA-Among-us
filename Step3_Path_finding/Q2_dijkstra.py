'''
#* Allows in dijkstra function to remove all the edges that we won't need to look over again
#* So the goal here is to remove all the edges between the node that are already visited
#* because we don't want to visit them, it will make dijkstra program doesn't work otherwise

#? liste : liste to remove elements
#? dict_visited : dictionnary visited in dijkstra that contain all the already visited node

#? return the modified list without the useless edges
'''
def remove_elements(liste, dict_visited):
    # We create a list to store the node that are already visited
    list_node_already_visited = []
    for key in dict_visited.keys():
        list_node_already_visited.append(key)
    # We want to browse the list and make every pair possible between nodes in order to compare the pair with the edges in th list
    # If the pair is in the list, we have to remove it
    for i in range(len(list_node_already_visited)):
        for j in range(i+1, len(list_node_already_visited)):
            for elements in liste:
                if elements[0] == list_node_already_visited[i] and elements[1] == list_node_already_visited[j]:
                    liste.remove(elements)
                if elements[0] == list_node_already_visited[j] and elements[1] == list_node_already_visited[i]:
                    liste.remove(elements)
    return liste

'''
#* Allows to run the dijkstra program on a graph from on initial node

#? grah : graph to perfom the dijsktra algorithm
#? initial_node : node you want to take as initial to perform the dijsktra algorithm

#? return the dictionnary visited which contain the name of all the node associated with their cost
#? the cost represent the cost from the initial node to the node in the dictionnary
'''
def dijsktra(graph, initial_node):
    # We initialize our variable for dijkstra algorithm
    # Value of initial node equal 0 and the rest equl infinity (here 1000 is sufficient)
    graph.dico_nodes[initial_node] = 0
    for key, value in graph.dico_nodes.items():
        if(key != initial_node):
            graph.dico_nodes[key] = 1000
    # We copy the list of edge in order to not modify the original (because we are going to use it several time)
    list_of_edges = []
    for element in graph.list_edges:
        list_of_edges.append(element)
    # We create the dictionnary of alreday visited node
    # This dictionnary will contain the final result
    visited = {initial_node : 0}
    # While we did't visited all the node, we continue our research
    while len(visited) != len(graph.dico_nodes):
        min_node_visited = None
        min_distance = 100
        # For each node that are already visited (we are going to look at the cost of their neighbour)
        for node_key, node_value in visited.items():
            neighbour = []
            distance = 0
            # We look at every edges of the node (so at all his neighboor, except the one remove because already visited)
            for elements in list_of_edges:
                # If the start node of the edge is the node we visit, it means it's a neighboor
                # therefore we add it to the list of neighboor
                if elements[0] == node_key:
                    neighbour.append((elements[1], elements[2]))
                # If the end node of the edge is the node we visit, it means it's a neighboor
                # therefore we add it to the list of neighboor
                if elements[1] == node_key:
                    neighbour.append((elements[0], elements[2]))
            # We visit the neighboor in the search of the minimum edge
            for name_node_and_cost in neighbour:
                # The distance is the distance already traveled + the edge
                # The distance already travel is the cost of the node
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
        # With this function we also remove all the edge that connect the node that are in visited
        list_of_edges = remove_elements(list_of_edges, visited)
    
    return visited