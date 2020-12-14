from Player import *
from Game_functions import *

players_alive=[]
for i in range(10):
    players_alive.append(Player(i)) 

Impostors=[1,7] 

summed_adjacency_matrix=np.zeros((10,10))

Game_ended=False
Crewmates_won=True 

round=-1
while(not Game_ended):
    round+=1
    #We randomly create the Adjacency matrix 
    new_adjacency_matrix= Create_Adjacency_Matrix(players_alive, Impostors)   
    print("\n\nHere is the adjacency matrix of round {}:\n{}".format(11-len(players_alive),new_adjacency_matrix))
    #The summed adjacency matrix is useful to see how many times each players saw each other
    # but most of all to highlight if players didn't see each other at all during the game.
    # Indeed if we have players that saw each other 3 to 4 times and others 0, those players have
    # a higher probability to be impostors. 
    # However, this technic is only useful when 2 impostors are remaining.
    if(len(Impostors)==2):
        summed_adjacency_matrix+=new_adjacency_matrix
        print("Here is the summed adjacency matrix of round {}:\n{}".format(11-len(players_alive),summed_adjacency_matrix))
        impostors=Check_impostor(players_alive, summed_adjacency_matrix)
        if(len(impostors)!=0):
            for impostor in impostors:
                Impostors.remove(impostor.ID) 
                players_alive.remove(impostor)
                print("Player {} was eliminated by crewmates because he was an impostor".format(impostor.ID))
            print("\nBusted by the sum of Adjacency Matrix")
            break
            
    #Now we kill one crewmate; we remove this player from  players_alive and we 
    #return the list of suspects for this kill, i.e. the previously updated attribute of seen players. 
    #Plus, we update all the Impostorness coefficients. 
    players_alive, Impostors=Kill_Crewmate(players_alive, Impostors)
    #If we arrive in a critical situation where if we don't unmask the impostor this round
    #they will win by numerical superiority after their next kill, we have to make a decision.
    # And this is where the Impostorness coefficient plays its role.
    if (len(players_alive)-len(Impostors)<=1): 
        Most_probable_impostor=Get_Best_Suspect(players_alive) 
        players_alive.remove(Most_probable_impostor) 

        #If the player we decided to kill wasn’t the impostor, then we couldn’t get past 
        # the critical situation and impostors won. Nonetheless, if we succeed to kill 
        # one impostor, then either the game ends and crewmates win since there are no impostors 
        # remaining, or the game continues, and we loop once again. 
        if(Most_probable_impostor not in Impostors): 
            print("{} was eliminated but he was not an impostor!".format(Most_probable_impostor.ID))
            Game_ended=True 
            Crewmates_won=False   
        else:
            print("{} was eliminated and he was an impostor!".format(Most_probable_impostor.ID))   

    if(len(Impostors)==0):
        Game_ended=True    

#After the game ends, we display a winning message 

if(Crewmates_won): 
    print("\n\nCongratulations to crewmates, you found and eliminated all impostors!\n\n") 
else: 
    print("\n\nImpostors {} got the best of you and killed everyone!\n\n".format(Impostors)) 