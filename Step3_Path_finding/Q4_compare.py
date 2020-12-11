from Q3_show_result import *

def print_result(first_node, last_node, difference):
    print("The difference of travel time between room {} and room {} is {} \n".format(first_node, last_node, difference))



def compare_both_model(graph_crewmate, graph_impostor):
    list_of_result_crewmate = all_time(graph_crewmate)
    list_of_result_impostor = all_time(graph_impostor)
    difference = 0
    condition = False
    for i in range(len(list_of_result_crewmate)):
        for j in range(len(list_of_result_impostor)):
            if list_of_result_crewmate[i][0] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][1] == list_of_result_impostor[j][1]:
                condition = True
            if list_of_result_crewmate[i][1] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][0] == list_of_result_impostor[j][1]:
                condition = True
            if condition:
                difference = list_of_result_crewmate[i][2] - list_of_result_impostor[j][2]
                print_result(list_of_result_crewmate[i][0], list_of_result_crewmate[i][1], difference)
                print(i)
                break

