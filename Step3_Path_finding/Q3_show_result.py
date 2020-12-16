import pandas as pd

from Q2_dijkstra import *

'''
#* Function use in all time to verify that a node is not coupled with itself 
#* it happened for the first node of dijkstra
#* We also verify that the node is not already in the list of result (we don't want a repeat)

#? result : list composed of (first_node, last_node, cost)
#? list_of_all_result : list that contain all the result that we already visit

#? return the condition
'''
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


'''
#* Allows to show the time to travel for any pair of rooms for a graph

#? graph : crew mate graph or impostor graph

#? return the list of the result
'''
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
            # We create a element of the result
            result = ((start_node, node_final, value))
            # We verify the condition (see below to see all the condition)
            condition = Condition_for_all_time(result, list_of_all_result)
            if condition:
                # We add the result to the final list
                list_final.append(result)
            # Even if the result is not good we add it to be sure it will not be seen another time
            list_of_all_result.append(result)
    return list_final


'''
#* Function that allows us to print the result from the previous function
#* It print a graph that show all the result
#* To read a result you look at the row and column name, then at its value
#* The value is the minimal cost between the row name room and the column name room

#? list_of_result : list of all the result calculted in the previous function
'''
def print_the_result(list_of_result):
    # We first store the list of room 
    list_room =  ["ME", "AD", "UE", "RE", "SE", "LE", "EL", "ST", "CO", "SH", "O2", "WE", "NA", "CA"]
    # We use the list of room to create the matrix of the result with row and column names
    # Each row name correspond to a room name, same things for the column name
    graph = pd.DataFrame([[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0]], 
                                columns = list_room, index = list_room)
    # For each result, we put the result in the good row and column
    for i in range(len(list_of_result)):
        for rows in list_room:
            for colunms in graph:
                if list_of_result[i][0] == rows and list_of_result[i][1] == colunms:
                    graph.loc[rows, colunms] = list_of_result[i][2]
                if list_of_result[i][1] == rows and list_of_result[i][0] == colunms:
                    graph.loc[rows, colunms] = list_of_result[i][2]
    # Finally we print the graph
    print(graph)