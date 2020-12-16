from Create_map_function import *
from Q2_dijkstra import *
from Q3_show_result import *
from Q4_compare import *

'''
#* Function to execute test for question 2
#* You can compute the dijkstra alorithm on different model with different source node
'''
def Question2():
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()
    
    resultat = dijsktra(graph_crew_mate,"RE")
    print("resultat 1:")
    print(resultat)

    resultat2 = dijsktra(graph_crew_mate,"UE")
    print("resultat 2:")
    print(resultat2)

    print("resultat 3:")
    resultat3 = dijsktra(graph_impostor,"UE")
    print(resultat3)

    
'''
#* Function to execute to test the question 3
#* This function will show you the time travel for any pair of room for both model
'''
def Question3():
    # We create the 2 graph
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()

    # We create the list of result for the crew mate
    list_of_result_crewmate = all_time(graph_crew_mate)
    print("Here are the result for the crew mate :\n")
    # We print the result
    print_the_result(list_of_result_crewmate)
    print("The lenght is : {}".format(len(list_of_result_crewmate)))

    # We create the list of result for the impostor
    list_of_result_impostor = all_time(graph_impostor)
    print("Here are the result for the impostor :\n")
    # We print the result
    print_the_result(list_of_result_impostor)
    print("The lenght is : {}".format(len(list_of_result_impostor)))


'''
#* Function to execute to test question 3
#* This function compare the time travel between the two model for any paif of room
'''
def Question4():
    # We create the 2 graph
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()

    # We do the comparison
    compare_both_model(graph_crew_mate, graph_impostor)


if __name__ == "__main__":
    Question2()
    Question3()
    Question4()