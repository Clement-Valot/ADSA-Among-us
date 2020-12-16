class Player:
    def __init__(self, ID):
        self.ID = ID
        self.alive=True
        self.innocent=False
        self.avenged=False
        self.imp_coeff=0
        self.round_coeff=[0,0,0,0,0,0,0,0,0,0]

#Method that returns the object player corresponding to ID.
#We need it since we mostly work with player ID for lists and matrices.
def Get_Player_From_ID(players, ID):
    for player in  players:
        if ID==player.ID:
            return player

#Method that returns the list of players seen by the player_who_saw.
#players is the list of all players (dead or alive, crewmate or impostors)
#player_who_saw is the player who we want to know who he saw
#matrix is the adjacency matrix that is going to tell us who saw who on a particular round.
def Get_list_seen(players, player_who_saw, matrix):
    suspects=[]
    for player_ID in range(10):
        if matrix[player_who_saw.ID][player_ID]==1:
            player=Get_Player_From_ID(players, player_ID)
            if player.alive==True and player.innocent==False:
                suspects.append(player_ID)
    return suspects

#Method that returns the list of players seen by the impostors.
#We can't use the above function because it returns the alive and 
#not innocent player while we want impostors to be able to kill innocent 
#players as well.
def Get_list_seen_impostor(players, player_who_saw, matrix):
    suspects=[]
    for player_ID in range(10):
        if matrix[player_who_saw.ID][player_ID]==1:
            player=Get_Player_From_ID(players, player_ID)
            if player.alive==True:
                suspects.append(player_ID)
    return suspects

#Method useful for Impostors to know who they saw in a round to know who they can kill.
def Get_Players_Killable(players, Impostors, matrix):
    killable_players=[]
    for impostor_ID in Impostors:
        impostor=Get_Player_From_ID(players, impostor_ID)
        killable_players+=Get_list_seen_impostor(players, impostor, matrix)
    return list(set(killable_players)) #To remove duplicates

#We get the players still alive in the game which can be seen by player_who_sees.
#It is not the same as the Get_list_seen method since it doesn't take into account
#the player_who_sees in the returned list because a player can't see himself, and 
#also because we need to remove impostor number 2 if player_who_sees is impostor number 1
#because they can't see each other (only if there are still 2 impostors alive in the game)
def Get_Players_Alive(players, player_who_sees, Impostors):
    alive_players=[]
    for player in players:
        #We don't add the ID of the player since he can't see himself
        #We don't add the ID of the player if he is dead
        if player!=player_who_sees and player.alive==True:
            #Now we have to distinguish 2 cases:
            #The player is not an impostor then he can see everybody.
            #The player is an impostor then he can't see the other impostor (if 2 impostors remain)
            if (not(len(Impostors)==2 and (player.ID in Impostors))):
                alive_players.append(player.ID)
    return alive_players

#Method that returns the best suspect depending on its impostorness coefficient.
#Only used in critical situation to kill a player based on probability and not on 
#certainty like every other method.
def Get_Best_Suspect(players):
    coeff=0
    best_suspect=None
    for player in players:
        if player.imp_coeff>coeff:
            best_suspect=player
            coeff=player.imp_coeff
    return best_suspect
