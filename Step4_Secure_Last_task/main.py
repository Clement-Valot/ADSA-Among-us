from Create_map_function import *
from GraphClass import *

'''
#* Function to execute test for question 2
#* You can compute the dijkstra alorithm on different model with different source node
'''
def Question2():
    graph_crew_mate = Create_map_crewmate()
    graph_crew_mate.hamCycle()
    
    
if __name__ == "__main__":
    Question2()