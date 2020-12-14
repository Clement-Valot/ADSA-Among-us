#def isSafe(self, node, pos, path):
      # Check if the node is adjacent of the previous node (path[pos-1])
      # Check if the node is not already in the path if (node is in vertex return false)



    #def Hamiltonian(self, path, pos):
      # Si toutes les nodes sont dans le path on return True 
      # On essaye pour chaque node comme prochain candidat
        # Pour chaque node dans la liste de node
        # Si la node est safe 
          # path[pos] =  node
          # Si Hamiltonian(path, pos+1) == True
            #return true
          # Supprime la node si elle ne mene pas a une solution
            #path[pos] = -1
        # Return false




    #def Hamiltonian_Path(self):
      # On determine la node du debut en creant la liste path : on la remplit de -1 de la taille len(node)
      # path[0] = "WE" pour mettre WE comme debut
      # Si self.Ha(path,1) == False
        #Print ("pas de solution")
        #Return false
      #Self.printSolution(path)
      #Return True
    
    def Print_Path(path):
      print("There is an Hamiltionian path :\n")
      for node in path:
        print(node + " ")