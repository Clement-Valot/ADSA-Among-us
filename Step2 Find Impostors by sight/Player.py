class Player:
    def __init__(self, ID):
        self.ID = ID
        self.alive=True
        self.innocent=False
        self.imp_coeff=0
        self.players_seen_by_round=[]
        self.round_coeff=[0]

def Get_Seen_Alive(players, players_seen):
    alives=[]
    for player in players:
        if((player.alive) and (player.ID in players_seen)):
            alives.append(player)
    return alives

def Get_Seen_Unexorated(players, players_seen):
    seen_unexonerated=[]
    for player in players:
        if((not player.innocent) and (player.ID in players_seen)):
            seen_unexonerated.append(player)
    return seen_unexonerated

def Get_list_ID_players(players):
    IDs=[]
    for player in players:
        IDs.append(player.ID)
    return IDs

def Get_Player_From_ID(players, ID):
    for player in  players:
        if ID==player.ID:
            return player

def Remove_Impostors(players, impostors):
    if type(impostors)==list:
        for impostor in impostors:
            if impostor in players:
                players.remove(impostor)
    elif type(impostors)==int:
        if impostors in players:
            players.remove(impostors)

def Get_Best_Suspect(players):
    coeff=0
    best_suspect=""
    for player in players:
        if player.imp_coeff>coeff:
            best_suspect=player
            coeff=player.imp_coeff
    return best_suspect
