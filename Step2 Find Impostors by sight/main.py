from Player import *
from Game_functions import *

players=[]
for i in range(10):
    players.append(Player(i)) 

Impostors=[0,1] 
players_killed=[]

summed_adjacency_matrix=np.zeros((10,10))
list_matrices=[]

Game_ended=False
Crewmates_won=True 

round=-1
while(not Game_ended):
    round+=1
    print("\n\nPlayers remaining : {}".format(len(players)-round))
    print("Impostors remaining : {}".format(len(Impostors)))
    #We randomly create the Adjacency matrix 
    new_adjacency_matrix= Create_Adjacency_Matrix(players, Impostors)  
    #We need to store this adjacency matrix in a list to be able to know
    # who saw who at every round 
    list_matrices.append(new_adjacency_matrix)
    print("Here is the adjacency matrix of round {}:\n{}".format(round+1,new_adjacency_matrix))

    #The summed adjacency matrix is useful to see how many times each players saw each other
    # but most of all to highlight if players didn't see each other at all during the game.
    # Indeed if we have players that didn't see each other once and everybody else has seen
    # all others, then we are going to be able to detect it with this matrix (the only zeros
    # in the matrix will be in [row][col] and [col][row] which correspond to the ID of impostors (col and row) ). 
    # However, this technic is only useful when 2 impostors are remaining.
    summed_adjacency_matrix+=new_adjacency_matrix
    print("Here is the summed adjacency matrix of round {}:\n{}\n".format(round+1,summed_adjacency_matrix))
    players, Impostors, players_killed=Innocent(players, players_killed, Impostors, summed_adjacency_matrix)
    if(len(Impostors)==2): 
        busted=Check_impostor(players, players_killed, Impostors, summed_adjacency_matrix)
        if(busted):
            Game_ended=True
            break
    elif(len(Impostors)==0):
        Game_ended=True
        break
            
    #Now we kill one crewmate, taking care of killing one seen by impostors. 
    players, Impostors, players_killed=Kill_Crewmate(players, players_killed, Impostors, list_matrices)

    #If we arrive in a critical situation where if we don't unmask the impostor this round
    #they will win by numerical superiority after their next kill, we have to make a decision.
    # And this is where the Impostorness coefficient plays its role.
    if ((len(players_killed)==7 and len(Impostors)==1) or(len(players_killed)==5 and len(Impostors)==2)): 
        print("\nWe have a critical situation! Crewmates need to take a decision:")
        Most_probable_impostor=Get_Best_Suspect(players) 
        Most_probable_impostor.alive=False 
        players_killed.append(Most_probable_impostor)
        print("{} was eliminated because he had an Impostorness coefficient equals to {}".format(Most_probable_impostor.ID, Most_probable_impostor.imp_coeff))
        #If the player we decided to kill wasn’t the impostor, then we couldn’t get past 
        # the critical situation and impostors won. Nonetheless, if we succeed to kill 
        # one impostor, then either the game ends and crewmates win since there are no impostors 
        # remaining, or the game continues, and we loop once again. 
        if(Most_probable_impostor.ID not in Impostors): 
            print("He was not an impostor!\nThere is now as much crewmates as impostors, crewmates can no longer win...")
            Game_ended=True 
            Crewmates_won=False   
        else:
            Impostors.remove(Most_probable_impostor.ID)
            print("He was an impostor!\n")  
            if(len(Impostors)!=0):
                players, Impostors, players_killed = Exoneration(players, players_killed, Impostors, list_matrices) 
    if(len(Impostors)==0):
        Game_ended=True 

#After the game ends, we display a winning message 
if(Crewmates_won): 
    print("\n\nCongratulations to crewmates, you found and eliminated all impostors!\n\n") 
else: 
    print("\n\nImpostors {} got the best of you and killed everyone!\n\n".format(Impostors)) 