from Q3_show_result import *

'''
#* Function that allows us to display the interval of time between impostor and crew mate for each pair of rooms

#? graph_crewmate : graph of the crew mate
#? graph_impostor : graph of the impostor

#? return the list of difference
#? the list is going to be print by another function
'''
def compare_both_model(graph_crewmate, graph_impostor):
    # We first create the 2 list of result for each graph
    list_of_result_crewmate = all_time(graph_crewmate)
    list_of_result_impostor = all_time(graph_impostor)
    difference = 0
    condition = False
    list_of_difference = []
    # Then we visit all the result of the crew mate graph
    for i in range(len(list_of_result_crewmate)):
        for j in range(len(list_of_result_impostor)):
            condition = False
            # If the result of the crew mate as the same starting node and ending node than the result of the impostor then we compare the distance
            if list_of_result_crewmate[i][0] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][1] == list_of_result_impostor[j][1]:
                condition = True
            if list_of_result_crewmate[i][1] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][0] == list_of_result_impostor[j][1]:
                condition = True
            if condition:
                # We calculate the difference
                difference = list_of_result_crewmate[i][2] - list_of_result_impostor[j][2]
                # We store the result
                list_of_difference.append((list_of_result_crewmate[i][0], list_of_result_crewmate[i][1], difference))
                break
    return list_of_difference

