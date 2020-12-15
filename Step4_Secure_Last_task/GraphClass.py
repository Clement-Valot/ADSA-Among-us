import pandas as pd
'''
#* This class will allow us to create a graph and manipulate the node and edges of it
'''
class Graph:

  '''
  # To initialize a grah with a dictionnary of node and list of edges
  #? number_of_node : number of the node in the graph
  #? N : number of the node in the graph
  #? graph : data frame that is going to store the adjacency matrix
  '''
  def __init__(self, number_of_nodes): 
    self.graph = pd.DataFrame()
    self.N = number_of_nodes

  '''
  #* Function use in Hamiltonian to verify if the node is good : 
  #* -not already in the path
  #* -node is adjacent of the previous node 

  #? n : node to verify, it correspond to a line in the adjacency matrix
  #? pos : position in the path
  #? path : Hamiltonian path, with all the node already in the path

  #? return True if the node is good
  #? return False otherwise
  '''
  def isGood(self, n, pos, path):
    # Verify if the node is adjacent to the previous node in the adjacency matrix
    if self.graph.iloc[path[pos-1],n] == 0:
      return False
    # Verify if the node is already in the path 
    for node in path:
      if node == n:
        return False
    return True
  
  '''
  #* Function that finds the Hamiltonian path from an original node
  #* The original node is put in parameter in Ham_Solution

  #? path : store the Hamiltonian path
  #? pos : store the position (the state of the recursive function)
  '''
  def Hamiltonian(self, path, pos):
    # if all vertices are included in the path we stop the recursion and return true
    if pos == self.N: 
      return True
  
    # Try different vertices as a next candidate in Hamiltonian path
    # So we travel through each node (meaning each line of the adjacency matrix)
    for node in range(0,self.N): 
      # We verify that the node is good (not already in the path, previous node adjacent to the current node) 
      # The node is represented by his line number in the adjacency matrix
      if self.isGood(node, pos, path) == True:  
        # If the node is good we put it in the path
        path[pos] = node  
        # Recursion to find the Hamiltonian path
        if self.Hamiltonian(path, pos+1) == True:  
          return True
  
        # Remove the current node if it doesn't lead to a solution  
        path[pos] = -1
    # If it never return True we return False
    return False
  

  '''
  #* Function to lunch the search for Hamiltonian path

  #? starting_node : node where we want to start the Hamiltonian path

  #? return True and print the solution if there is a Hamiltonian path
  #? retunr False and print an error message if there is no solution
  '''
  def Ham_Solution(self, starting_node): 
    # We initialized the list that will store the path 
    # It has the size of the number of node and we initialize to -1 each node of the path 
    path = [-1] * self.N  

    # We initialize the first node of the path that will be used to lunch the Hamiltonian function
    path[0] = starting_node

    list_room =  ["ME", "AD", "UE", "RE", "SE", "LE", "EL", "ST", "CO", "SH", "O2", "WE", "NA", "CA"]

    # We lunch the Hamiltonian function with the path that we just initialize,
    # and a position of 1 (because one node is already in the path)
    if self.Hamiltonian(path,1) == False:
      # If the result is false it means there is no Hamiltonian path from the starting node  
      print ("Solution does not exist for room : {}\n".format(list_room[starting_node])) 
      return False

    # If we didn't return false previously, it means the Hamiltonian path exist
    # So we use the print function to print the path
    self.printSolution(path, starting_node)  
    return True

  '''
  #* Function that print the solution once the Hamiltonian path is found

  #? path : Hamiltonian path found previously composed of node (indicated by their index in the adjacency matrix)
  '''
  def printSolution(self, path,original_node):  
    # To print the solution we need to have the index of each room in the adjacency matrix
    # To do so we recover the list of room use in the creation of the map in 'Create_map_function
    list_room =  ["ME", "AD", "UE", "RE", "SE", "LE", "EL", "ST", "CO", "SH", "O2", "WE", "NA", "CA"] 
    print ("One Hamiltonian path has been found from the original node : {}".format(list_room[original_node]))
    # The path list is composed of node represented by their index in the adjacency matrix
    # So for each node (index) we print it in thanks to its corresponding room contain in list_room
    for vertex in path:
      print (list_room[vertex] , " ") 
