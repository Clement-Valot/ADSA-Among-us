from Q3_show_result import *

def print_result(first_node, last_node, difference):
    print("The difference of travel time between room {} and room {} is {} \n".format(first_node, last_node, difference))


'''
#* Function that allows us to display the interval of time between impostor and crew mate for each pair room

#? graph_crewmate : graph of the crew mate
#? graph_impostor : graph of the impostor
'''
def compare_both_model(graph_crewmate, graph_impostor):
    # We first create the 2 list of result for each graph
    list_of_result_crewmate = all_time(graph_crewmate)
    list_of_result_impostor = all_time(graph_impostor)
    difference = 0
    condition = False
    # Then we visit all the result of the crew mate graph
    for i in range(len(list_of_result_crewmate)):
        for j in range(len(list_of_result_impostor)):
            # If the result of the crew mate as the same starting node and ending node thant the result of the impostor we compare them
            if list_of_result_crewmate[i][0] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][1] == list_of_result_impostor[j][1]:
                condition = True
            if list_of_result_crewmate[i][1] == list_of_result_impostor[j][0] and list_of_result_crewmate[i][0] == list_of_result_impostor[j][1]:
                condition = True
            if condition:
                # We calculate the difference
                difference = list_of_result_crewmate[i][2] - list_of_result_impostor[j][2]
                # We print the result
                print_result(list_of_result_crewmate[i][0], list_of_result_crewmate[i][1], difference)
                print(i)
                break
