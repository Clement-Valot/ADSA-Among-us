class Graph:
    def __init__(self):
      #Dictionnaire de node avec node[name] = value
      self.dico_nodes = {}
      #Liste des edges
      self.list_edges = []

    def add_node(self, node):
        self.dico_nodes[node]= 0

    def add_edge(self, start_node, end_node, cost):
        self.list_edges.append((start_node, end_node, cost))