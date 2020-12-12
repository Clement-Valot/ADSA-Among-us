import random
import numpy as np
import Player

impostors=[1,7]
np.array()
def Create_Adjacency_Matrix(players_alive):
    for player in players_alive:
        #We get the list of ID of other players this player can see (among the living one)
        players_seenable=Player.Get_list_ID_players(players_alive)
        #We remove the ID of the player since he can't see himself
        players_seenable.remove(player.ID)
        #Now we have to distinguish 2 cases:
        #The player is not an impostor then he can see everebody
        if(player.ID not in impostors):
            return 0
        #The player is an impostor then he can't see the other impostor
        else:
            if len(impostors>1):
                if player.ID==impostors[0]:
                    players_seenable.remove(impostors[1])
                else:
                    players_seenable.remove(impostors[0])
            


    return 0

def Kill_Crewmate(list_players_alive):
    list_IDs_alive= Player.Get_list_ID_players(list_players_alive)
    player_killed= Player.Get_Player_From_ID(random.choice(list_IDs_alive))
    print("Player {} was killed (coeff: {})")
    round=-1
    for players_seen in player_killed.players_seen_by_round:
        round+=1
        players_seen_still_alive= Player.Get_players_alive(players_seen)
        coeff_to_redistribute=player_killed.round_coeff[round]/len(players_seen_still_alive)
        for player in players_seen_still_alive:
            player.imp_coeff+=coeff_to_redistribute
