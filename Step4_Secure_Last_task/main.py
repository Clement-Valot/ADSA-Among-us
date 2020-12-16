from Create_map_function import *
from GraphClass import *

'''
#* Function that find all the adjacents rooms of one room

#? graph : graph on which we want to find the adjacents rooms
#? room : room that we want to find its adjacents rooms

#? return a list composed of the index of the row that correspond to the adjacents rooms
'''
def adjecent_room(graph, room):
    # We store the row of the room we want to check in the adjacency matrix
    list_room = graph.graph[room]
    # We initialize the list of adjacent room we want to return
    final_list =[]
    # We travel through the row of the adjacency matrix of the room put in parameter
    for i in range(0, len(list_room)):
        # If the value is different from 0, it means there is an edge between both rooms
        if list_room[i] != 0:
            # So we add the index (corresponding to a room in adjacency matrix) to the final list
            final_list.append(i)
    return final_list



'''
#* Function to execute test for question 4
#* This function shows our result for the part 4
#* We take "CA" as the original node
#* We show all the possible Hamiltonian path that begin from adjacents rooms of "CA"
'''
def Question4():
    # We first initialize the graph
    graph_crew_mate = Create_map_crewmate()
    # We store the adjacent room of Cafeteria
    list_adjacent_room = adjecent_room(graph_crew_mate, "CA")
    # For each adjacent room as starting point, we look for an Hamiltonian path
    for node in list_adjacent_room:
        graph_crew_mate.Ham_Solution(node)
    
    
    
if __name__ == "__main__":
    Question4()