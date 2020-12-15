import pandas as pd

from GraphClass import *

'''
#* This function create the crew mate map thanks to the class graph

#? Return the crew mate graph
'''
def Create_map_crewmate():
    # Initialize the graph
    graph = Graph(14)
    list_room =  ["ME", "AD", "UE", "RE", "SE", "LE", "EL", "ST", "CO", "SH", "O2", "WE", "NA", "CA"]
    graph.graph = pd.DataFrame([[0,0,7.5,0,0,0,0,0,0,0,0,0,0,7.5],
                                [0,0,0,0,0,0,0,6.5,0,0,0,0,0,7],
                                [7.5,0,0,6.5,5.5,7.5,0,0,0,0,0,0,0,10],
                                [0,0,6.5,0,5,6.5,0,0,0,0,0,0,0,0],
                                [0,0,5.5,5,0,6,0,0,0,0,0,0,0,0],
                                [0,0,7.5,6.5,6,0,8,10.5,0,0,0,0,0,0],
                                [0,0,0,0,0,8,0,7,0,0,0,0,0,0],
                                [0,6.5,0,0,0,10.5,7,0,6,6,0,0,0,8],
                                [0,0,0,0,0,0,0,6,0,4,0,0,0,0],
                                [0,0,0,0,0,0,0,6,4,0,8,8.5,8,0],
                                [0,0,0,0,0,0,0,0,0,8,0,6.5,6,0],
                                [0,0,0,0,0,0,0,0,0,8.5,6.5,0,6.5,6],
                                [0,0,0,0,0,0,0,0,0,8,6,6.5,0,0],
                                [7.5,7,10,0,0,0,0,8,0,0,0,6,0,0]], 
                                columns = list_room, index = list_room)
    return graph

graph_crew_mate = Create_map_crewmate()
print(graph_crew_mate.graph)

