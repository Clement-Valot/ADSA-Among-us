from Q2_dijkstra import *

def Condition_for_all_time(result, list_of_all_result):
    condition = True
    # We verify if it is not the first node coupled with the firts node
    if result[0] == result[1]:
        condition = False
    # We verify if we already have the result but in an other way (start_node <-> end_node)
    # and if the room is "COR" which doesn't interst us
    for i in range (len(list_of_all_result)):
        if result[0] == list_of_all_result[i][0] and result[1] == list_of_all_result[i][1]:
            condition = False
        if result[1] == list_of_all_result[i][0] and result[0] == list_of_all_result[i][1]:
            condition = False
        if result[1] == "COR" or result[0] == "COR":
            condition = False
    
    return condition

def all_time(graph):
    list_final = []
    list_of_all_result = []
    list_of_node = []
    dict_of_result = {}
    condition = False
    # Creation of the list that contain all the node
    for key in graph.dico_nodes.keys():
        list_of_node.append(key)
    # For every node in the list, we run dijkstra
    for start_node in list_of_node:
        # We store the result
        dict_of_result = dijsktra(graph, start_node)
        # For every result
        for node_final, value in dict_of_result.items():
            # We create a tuple of the result
            result = ((start_node, node_final, value))
            condition = Condition_for_all_time(result, list_of_all_result)
            if condition:
                list_final.append(result)
            list_of_all_result.append(result)
    return list_final
    
def print_the_result(list_of_result):
    for i in range(len(list_of_result)):
        print("The connexion betweem room {} and room {} takes {} second \n".format(list_of_result[i][0], 
        list_of_result[i][1], list_of_result[i][2]))