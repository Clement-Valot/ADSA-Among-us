import random
import numpy as np
from Player import *

#This function is the first core of our algorithm. It creates the adjacency matrix
# of who saw who before a player is killed by impostors. 
#It is quite complicated to implement this matrix correctly because several details need
#to be taken into account:
#   -Impostors can't see each other
#   -Dead players musn't be taken into account
#   -The matrix must be symmetrical meaning a player who saw another one must also have been
#seen by this player (most difficult part)
#   -The number of players seen is random between 1 and the number of players seenable
def Create_Adjacency_Matrix(players, Impostors):
    adjacency_matrix=np.zeros((10,10))
    for player in players:
        if(player.alive==True):
            #We get the list of ID of other players this player can see (among the living one)
            players_seenable= Get_Players_Alive(players, player, Impostors)
            
            #randomly choosing the number of players from this list he will see,
            #between 0 and the length of the players_seenable list.
            max=len(players_seenable)
            number_seen=random.randint(1,max)
            players_seen=random.sample(players_seenable, number_seen)
            
            #Finally, we fill the adjacency matrix
            for ID in players_seen:
                adjacency_matrix[player.ID,ID]=1
                adjacency_matrix[ID,player.ID]=1
    return adjacency_matrix

#This function is the second core of our algorithm. it takes care of the kill of one player.
#First, we kill the player, then we kill the impostor if he is immediatly busted
#Second we update Impostorness Coefficient to take into account the death of this player.
def Kill_Crewmate(players, players_killed, Impostors, list_matrices):
    #We get the list of players impostors saw to kill one of them
    killable_players=Get_Players_Killable(players, Impostors, list_matrices[-1])
    #We randomly choose one player to kill in this list
    player_killed = Get_Player_From_ID(players, random.choice(killable_players))
    player_killed.alive=False
    players_killed.append(player_killed)
    print("\nPlayer {} was killed by impostors.".format(player_killed.ID))
    #We get the list of suspects, aka the list of players seen by the killed player
    suspects=Get_list_seen(players, player_killed, list_matrices[-1])
    print("He saw the following suspects (alive and not proven innocent) : {}".format(suspects))
    #If this list contains only one player, then he has to be an impostor. 
    # Therefore, we remove him from the Impostor list and
    # from players since crewmates will vote against him to eliminate him.
    if(len(suspects)==1):
        impostor=Get_Player_From_ID(players, suspects[0])
        Impostors.remove(impostor.ID)
        impostor.alive==False
        players_killed.append(impostor)
        print("\nPlayer {} was eliminated by crewmates because he was an impostor.".format(impostor.ID))
        print("Busted by Length of suspects list\n")
        #If one impostor gets busted, then we can exonerate all the players he saw during 
        # the game since impostors can’t see each other 
        # We still have to check if Impostors haven't all be eliminated
        if(len(Impostors)!=0):
            players, Impostors, players_killed = Exoneration(players, players_killed, Impostors, list_matrices)
    players, Impostors, players_killed = Update_Impostor_Coeff(players, players_killed, Impostors, list_matrices)
    return players, Impostors, players_killed

#we want to redistribute the impostorness coefficients the killed player 
#acquired at each round to the other players convicted with him.
#We also check if after the update, one player gets an impostorness coeff
#equals to 1 then he is an impostor.
def Update_Impostor_Coeff(players, players_killed, Impostors, list_matrices):
    round=-1
    for matrix in list_matrices:
        round+=1
        suspects=Get_list_seen(players, players_killed[round], matrix)
        #If this list contains only one player, he has to be an impostor. 
        # Therefore, we remove him from the Impostor list and
        # from players since crewmates will vote against him to eliminate him.
        if(len(suspects)==1 and len(Impostors)!=0):
            impostor=Get_Player_From_ID(players, suspects[0])
            players_killed.append(impostor)
            impostor.alive=False
            if(impostor.ID in Impostors):
                Impostors.remove(impostor.ID) 
                print("\nPlayer {} was eliminated by crewmates because he was an impostor.".format(impostor.ID))
                print("Busted by Length of suspects list updated (after removing dead or innocent suspects).\n")
            else:
                print("\nPlayer {} was eliminated by crewmates but he was not an impostor.".format(impostor.ID))
                print("He was just at the wrong places at the wrong time.")
            
            #If one impostor gets busted, then we can exonerate all the players he saw during 
            # the game since impostors can’t see each other 
            if(len(Impostors)!=0):
                players, Impostors, players_killed = Exoneration(players, players_killed, Impostors, list_matrices)
        elif(len(suspects)!=0):
            for player in players:
                suspect=Get_Player_From_ID(players, player.ID)
                suspect.round_coeff[round]=0
                if((player.ID in suspects) and (player.alive==True)):
                    suspect.round_coeff[round]=(1/len(suspects))
    for player in players:
        player.imp_coeff=sum(player.round_coeff)
    return players, Impostors, players_killed

#If one impostor is found, then all the players this impostor saw aren't impostors
#So we can exonerate them.
#All we need to do is get through all the list of players seen by the impostor at each round.
def Exoneration(players, players_killed, Impostors, list_matrices):
    round=-1
    exonerated=[]
    impostor=players_killed[-1]
    for matrix in list_matrices:
        round+=1
        exonerated_by_round=Get_list_seen(players, impostor, matrix)
        for player_ID in exonerated_by_round:
            player=Get_Player_From_ID(players, player_ID)
            player.round_coeff[round]=0
            player.innocent=True
        exonerated+=exonerated_by_round
    exonerated=list(set(exonerated)) #to remove duplicates
    #If the number of exonerated players equals the length of the list of alive players 
    # minus one, this means there is only one other player that the convicted impostor 
    # didn’t see and this means this unseen player is the other impostor.
    if(len(exonerated)==10-len(players_killed)-1): 
        #We look for the missing player
        for player in players: 
            if ((player.ID not in exonerated) and (player.alive==True) and (player!=impostor)):  
                player.alive=False
                Impostors.remove(player.ID)
                players_killed.append(player)
                print("\nPlayer {} was eliminated by crewmates because he was an impostor.".format(player.ID))
                print("Busted by Exoneration.\n")
    return players, Impostors, players_killed             

#If one player sees all other alive players, then he can't be an impostor.
# We must put his innocent attribute to True so that he isn't convicted for other kills
# If he is seen by the killed_player
def Innocent(players, players_killed, Impostors, matrix):
    for row_ID in range(10):
        sum=0
        player=Get_Player_From_ID(players,row_ID)
        if(player.alive==True):
            for col_ID in range(10):
                if(matrix[row_ID][col_ID]!=0):
                    sum+=1
        if(sum==9):
            player.innocent=True
            print("Player {} was innocented because he saw every other players".format(player.ID))
            for round in range(10):
                player.round_coeff[round]=0
    
    innocent=0
    for player in players:
        if(player.innocent==True and player.alive==True):
            innocent+=1
    #If we have as many innocented player as there are crewmates still in the game,
    # then we can deduce who are/is the impostors
    remaining_crewmates=10-len(players_killed)-len(Impostors)
    if(innocent==remaining_crewmates):
        for player in players: 
            if ((player.alive==True) and (player.innocent==False)):  
                player.alive=False
                Impostors.remove(player.ID)
                players_killed.append(player)
                print("\nPlayer {} was eliminated by crewmates because he was an impostor.".format(player.ID))
                print("Busted by Innocentation of all crewmates.\n")
    return players, Impostors, players_killed

def Check_impostor(players, players_killed, Impostors, summed_adjacency_matrix):
    suspects=[]
    for ID_row in range(10):
        if(Get_Player_From_ID(players, ID_row).alive==True):
            for ID_col in range(10):
                if(ID_row!=ID_col and summed_adjacency_matrix[ID_row][ID_col]==0):
                    suspects.append(Get_Player_From_ID(players, ID_row))
    if(len(suspects)==2):
        for impostor_ID in Impostors:
            impostor=Get_Player_From_ID(players, impostor_ID)
            Impostors.remove(impostor.ID)
            players_killed.append(impostor)
            print("Player {} was eliminated by crewmates because he was an impostor".format(impostor.ID))
        print("Busted by the sum of Adjacency Matrix\n")
        return True
    return False

