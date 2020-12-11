from Create_map_function import *
from Q2_dijkstra import *
from Q3_show_result import *
from Q4_compare import *


def Question2():
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()
    
    resultat = dijsktra(graph_crew_mate,"RE")
    print(resultat)
    resultat2 = dijsktra(graph_crew_mate,"UE")
    print(resultat2)

    resultat3 = dijsktra(graph_impostor,"UE")
    print(resultat3)
    

def Question3():
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()

    list_of_result_crewmate = all_time(graph_crew_mate)
    print_the_result(list_of_result_crewmate)
    print("The lenght is : {}".format(len(list_of_result_crewmate)))

    list_of_result_impostor = all_time(graph_impostor)
    print_the_result(list_of_result_impostor)
    print("The lenght is : {}".format(len(list_of_result_impostor)))


def Question4():
    graph_crew_mate = Create_map_crewmate()
    graph_impostor = Create_map_impostor()

    compare_both_model(graph_crew_mate, graph_impostor)


if __name__ == "__main__":
    Question2()
    #Question3()
    #Question4()