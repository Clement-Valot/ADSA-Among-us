import random
import numpy as np
from Player import *

def Create_Adjacency_Matrix(players_alive, Impostors):
    adjacency_matrix=np.zeros((10,10))
    for player in players_alive:
        #We get the list of ID of other players this player can see (among the living one)
        players_seenable= Get_list_ID_players(players_alive)
        #We remove the ID of the player since he can't see himself
        players_seenable.remove(player.ID)
        #Now we have to distinguish 2 cases:
        #The player is not an impostor then he can see everebody so we don't touch the seenable list.
        #The player is an impostor then he can't see the other impostor (if 2 impostors remain)
        if player.ID==Impostors[0]:
            Remove_Impostors(players_seenable, Impostors[1])
        elif player.ID==Impostors[1]:
            Remove_Impostors(players_seenable, Impostors[0])
        #Now we fill the players seen by round attribute of the player
        #randomly choosing the number of players from this list he will see,
        #between 0 and the length of the players_seenable list.
        number_seen=random.randint(1,len(players_seenable))
        players_seen=random.sample(players_seenable, number_seen)
        
        #Finally, we fill the adjacency matrix
        for ID in players_seen:
            adjacency_matrix[player.ID,ID]=1
            adjacency_matrix[ID,player.ID]=1
    
    #Now we need to update the list of players seen for each player because it doesn't 
    #correspond to the actual adjacency matrix (because we made the matrix symmetrical in a 
    # non ethical way)
    for player in players_alive:
        players_seen=[]
        for player2 in players_alive:
            if(adjacency_matrix[player.ID][player2.ID]==1):
                players_seen.append(player2.ID)
        player.players_seen_by_round.append(players_seen)
    return adjacency_matrix

def Kill_Crewmate(players_alive, Impostors):
    #We get the list of players impostors saw to kill one of them
    killable_players=Get_Players_Killable(players_alive, Impostors)
    #We randomly choose one player to kill in this list
    player_killed= Get_Player_From_ID(players_alive, random.choice(killable_players))
    player_killed.alive=False
    players_alive.remove(player_killed)
    print("Player {} was killed by impostors (coeff: {})".format(player_killed.ID, player_killed.imp_coeff))
    #We get the list of suspects, aka the list of players seen by the killed player
    suspects=player_killed.players_seen_by_round[-1]
    #If this list contains only one player, then he has to be an impostor. 
    # Therefore, we remove him from the Impostor list and
    # from players_alive since crewmates will vote against him to eliminate him.
    if(len(suspects)==1):
        impostor=Get_Player_From_ID(players_alive, suspects[0])
        Impostors.remove(impostor.ID) 
        players_alive.remove(impostor)
        print("Player {} was eliminated by crewmates because he was an impostor\n".format(impostor.ID))
        #If one impostor gets busted, then we can exonerate all the players he saw during 
        # the game since impostors can’t see each other 
        Exonerated_players=Exoneration(players_alive,impostor)
    else:
        for player in players_alive:
            if player.ID in suspects:
                player.round_coeff.append(1/len(suspects))
            else:
                #We still have to append 0 to non suspects players to keep the good index on lists
                player.round_coeff.append(0)
    players_alive, Impostors = Update_Impostor_Coeff(players_alive, player_killed, Impostors)
    return players_alive, Impostors

def Get_Players_Killable(players_alive, Impostors):
    killable_players=[]
    for impostor_ID in Impostors:
        impostor=Get_Player_From_ID(players_alive, impostor_ID)
        killable_players+=impostor.players_seen_by_round[-1]
    return list(set(killable_players)) #To remove duplicates

#we want to redistribute the impostorness coefficients the killed player 
#acquired at each round to the other players convicted with him.
#We also check if after the update, one player gets an impostorness coeff
#equals to 1 then he is an impostor.
def Update_Impostor_Coeff(players_alive, player_killed, Impostors):
    round=-1
    for players_seen in player_killed.players_seen_by_round:
        round+=1
        #We only redistribute coeff to alive players
        players_seen_still_alive= Get_Seen_Alive(players_alive, players_seen)
        imp_coeff_by_round=player_killed.round_coeff[round]
        player_killed.round_coeff[round]=0
        #If no players are alive in this list or the coeff at this round is 0
        if(len(players_seen_still_alive)!=0 and imp_coeff_by_round!=0):
            coeff_to_redistribute=imp_coeff_by_round/len(players_seen_still_alive)
            for player in players_seen_still_alive:
                player.round_coeff[round]+=coeff_to_redistribute
                if(player.round_coeff[round]==1):
                    #if the coeff reaches 1, then the player has 100% chance to be an impostor
                    Impostors.remove(player.ID) 
                    players_alive.remove(player)
                    print("Player {} was eliminated by crewmates because he was an impostor\n".format(player.ID))
                    #If one impostor gets busted, then we can exonerate all the players he saw during 
                    # the game since impostors can’t see each other 
                    Exonerated_players=Exoneration(players_alive, player) 
    #Finally we update the overall Impostorness coeff
    for player in players_alive:
        player.imp_coeff=sum(player.round_coeff)
    return players_alive, Impostors

#If one impostor is found, then all the players this impostor saw aren't impostors
#So we can exonerate them.
#All we need to do is get through all the list of players seen by the impostor at each round.
def Exoneration(players_alive, impostor):
    exonerated=[]
    for players_seen in impostor.players_seen_by_round:
        players_seen_still_alive= Player.Get_players_alive(players_seen)
        for player in players_seen_still_alive:
            if player not in exonerated:
                player.innocent=True
                exonerated.append(player)
    #If the number of exonerated players equals the length of the list of alive players 
    # minus one, this means there is only one other player that the convicted impostor 
    # didn’t see and this means this unseen player is the other impostor.
    if(len(exonerated)==len(players_alive)-1): 
        #We look for the missing player
        for player in players_alive: 
            if player not in exonerated:  
                players_alive.remove(player)
                return players_alive, player
    else:
        #We update coefficient impostorness
        for player in exonerated:
            round=-1
            for players_seen in player.players_seen_by_round:
                round+=1
                #We only redistribute coeff to non exonerated players seen by player
                players_seen_unexonerated= Get_Seen_Unexorated(players_alive, players_seen)
                imp_coeff_by_round=player.round_coeff[round]
                player.round_coeff[round]=0
                #If the coeff at this round is 0 or list is empty, we don't pursue
                if(imp_coeff_by_round!=0 and len(players_seen_unexonerated)!=0):
                    coeff_to_redistribute=imp_coeff_by_round/len(players_seen_unexonerated)
                    for seen_player in players_seen_unexonerated:
                        seen_player.round_coeff[round]+=coeff_to_redistribute
                        if(seen_player.round_coeff[round]==1):
                            #if the coeff reaches 1, then the player has 100% chance to be an impostor
                            players_alive.remove(seen_player)
                            print("Player {} was eliminated by crewmates because he was an impostor\n".format(player.ID))
                            return players_alive, seen_player                   

def Check_impostor(players_alive, summed_adjacency_matrix):
    suspects=[]
    IDs_alives= Get_list_ID_players(players_alive)
    for ID_row in IDs_alives:
        for ID_col in IDs_alives:
            if(ID_row!=ID_col and summed_adjacency_matrix[ID_row][ID_col]==0):
                suspects.append(Get_Player_From_ID(players_alive, ID_row))
    if(len(suspects)==2):
        return suspects
    else:
        return []

    