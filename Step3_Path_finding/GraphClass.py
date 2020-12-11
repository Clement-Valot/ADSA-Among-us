'''
#* This class will allow us to create a graph and manipulate the node and edges of it
'''
class Graph:

    '''
    # To initialize a grah with a dictionnary of node and list of edges
    #? dico_node : dictionnary that store node in the form : dict[name_of_the_node] = value
    #? list_edges : list that store edges in the form : list[(start_node, end_node, cost), (start_node, end_node, cost), ...]
    '''
    def __init__(self):
      #Dictionnaire de node avec node[name] = value
      self.dico_nodes = {}
      #Liste des edges
      self.list_edges = []
    
    '''
    # To add a node to the graph
    #? we initialize its value to zero
    '''
    def add_node(self, node):
        self.dico_nodes[node]= 0

    '''
    # To add an edge to the graph
    '''
    def add_edge(self, start_node, end_node, cost):
        self.list_edges.append((start_node, end_node, cost))