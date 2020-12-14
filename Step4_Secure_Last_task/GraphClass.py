import pandas as pd
'''
#* This class will allow us to create a graph and manipulate the node and edges of it
'''
class Graph:

  '''
  # To initialize a grah with a dictionnary of node and list of edges
  #? dico_node : dictionnary that store node in the form : dict[name_of_the_node] = value
  #? list_edges : list that store edges in the form : list[(start_node, end_node, cost), (start_node, end_node, cost), ...]
  '''
  def __init__(self, number_of_nodes): 
    self.graph = pd.DataFrame()
    self.N = number_of_nodes



  def isGood(self, n, pos, path):
    if self.graph.iloc[path[pos-1],n] == 0:
      return False
    for node in path:
      if node == n:
        return False
    return True
  
  def hamCycleUtil(self, path, pos):
    # base case: if all vertices are  
    # included in the path  
    if pos == self.N: 
      return True
  
    # Try different vertices as a next candidate  
    # in Hamiltonian Cycle. We don't try for 0 as  
    # we included 0 as starting point in hamCycle()  
    for v in range(0,self.N):  
      if self.isGood(v, pos, path) == True:  
        path[pos] = v  
        if self.hamCycleUtil(path, pos+1) == True:  
          return True
  
        # Remove current vertex if it doesn't  
        # lead to a solution  
        path[pos] = -1
    return False
  
  def hamCycle(self):  
    path = [-1] * self.N  
  
    ''' Let us put vertex 0 as the first vertex  
    in the path. If there is a Hamiltonian Cycle,  
    then the path can be started from any point  
     of the cycle as the graph is undirected '''
    path[0] = 11
  
    if self.hamCycleUtil(path,1) == False:  
      print ("Solution does not exist\n") 
      return False
  
    self.printSolution(path)  
    return True

  def printSolution(self, path):  
    print ("Solution Exists: Following", 
            "is one Hamiltonian Cycle")
    list_room =  ["ME", "AD", "UE", "RE", "SE", "LE", "EL", "ST", "CO", "SH", "O2", "WE", "NA", "CA"] 
    for vertex in path:
      print (list_room[vertex] , " ") 
