from GraphClass import *
'''
#* This function create the crew mate map thanks to the class graph

#? Return the crew mate graph
'''
def Create_map_crewmate():
    # Initialize the graph
    graph = Graph()
    # We add the node of the graph (14)
    graph.add_node("UE")
    graph.add_node("RE")
    graph.add_node("SE")
    graph.add_node("LE")
    graph.add_node("ME")
    graph.add_node("EL")
    graph.add_node("CA")
    graph.add_node("ST")
    graph.add_node("AD")
    graph.add_node("CO")
    graph.add_node("O2")
    graph.add_node("SH")
    graph.add_node("WE")
    graph.add_node("NA")
    # We add all the edges one time (not in both way) (25)
    graph.add_edge("RE","UE",6.5)
    graph.add_edge("RE","SE",5)
    graph.add_edge("RE","LE",6.5)
    graph.add_edge("UE","LE",7.5)
    graph.add_edge("UE","SE",5.5)
    graph.add_edge("UE","ME",7.5)
    graph.add_edge("SE","LE",6)
    graph.add_edge("LE","EL",8)
    graph.add_edge("LE","ST",10.5)
    graph.add_edge("EL","ST",7)
    graph.add_edge("ST","CO",6)
    graph.add_edge("ST","SH",6)
    graph.add_edge("CO","SH",4)
    graph.add_edge("ST","AD",6.5)
    graph.add_edge("ST","CA",8)
    graph.add_edge("CA","ME",7.5)
    graph.add_edge("UE","CA",10)
    graph.add_edge("CA","AD",7)
    graph.add_edge("CA","WE",6)
    graph.add_edge("WE","O2",6.5)
    graph.add_edge("WE","SH",8.5)
    graph.add_edge("WE","NA",6.5)
    graph.add_edge("O2","NA",6)
    graph.add_edge("O2","SH",8)
    graph.add_edge("SH","NA",8)
    return graph


'''
#* This function create the impostor map thanks to the class graph

#? Return the crew mate graph
'''
def Create_map_impostor():
    # Since it's the same map but with more edge and one more room we take again the same map
    graph = Create_map_crewmate()
    # First we need to remove some edges because of the corridor room that is added
    graph.list_edges.remove(("WE","O2",6.5))
    graph.list_edges.remove(("WE","SH",8.5))
    graph.list_edges.remove(("WE","NA",6.5))
    graph.list_edges.remove(("O2","NA",6))
    graph.list_edges.remove(("O2","SH",8))
    graph.list_edges.remove(("SH","NA",8))
    # Then we add the new node corridor
    graph.add_node("COR")
    # The we add the edges that repalce previous edges but now with the corridor
    graph.add_edge("COR","WE",3.5)
    graph.add_edge("COR","O2",3)
    graph.add_edge("COR","NA",3)
    graph.add_edge("COR","SH",5)
    # Then we add the new edges, for the vents
    graph.add_edge("UE","RE",0)
    graph.add_edge("RE","LE",0)
    graph.add_edge("SE","ME",0)
    graph.add_edge("ME","EL",0)
    graph.add_edge("SE","EL",0)
    graph.add_edge("CA","AD",0)
    graph.add_edge("CA","COR",0)
    graph.add_edge("AD","COR",0)
    graph.add_edge("WE","NA",0)
    graph.add_edge("SH","NA",0)

    return graph



