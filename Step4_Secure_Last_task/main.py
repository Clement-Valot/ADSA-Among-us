from Create_map_function import *
from GraphClass import *

def adjecent_room(graph, room):
    list_room = graph.graph[room]
    print("list room : {}".format(list_room))
    final_list =[]
    for i in range(0, len(list_room)):
        if list_room[i] != 0:
            final_list.append(i)
    print("final list {}".format(final_list))
    return final_list



'''
#* Function to execute test for question 2
#* You can compute the dijkstra alorithm on different model with different source node
'''
def Question4():
    graph_crew_mate = Create_map_crewmate()
    list_adjacent_room = adjecent_room(graph_crew_mate, "CA")
    for node in list_adjacent_room:
        graph_crew_mate.Ham_Solution(node)
    
    
    
if __name__ == "__main__":
    Question4()