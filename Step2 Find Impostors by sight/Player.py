class Player:
    def __init__(self, ID):
        self.ID = ID
        self.alive=True
        self.imp_coeff=0
        self.players_seen_by_round=[]
        self.round_coeff=[]

def Get_players_alive(list_players):
    alives=[]
    for player in list_players:
        if player.alive:
            alives.append(player)
    return alives

def Get_list_ID_players(list_players):
    IDs=[]
    for player in list_players:
        IDs.append(player.ID)
    return IDs

def Get_Player_From_ID(ID, list_players_alive):
    for player in list_players_alive:
        if ID==player.ID:
            return player
    
def Get_Best_Suspect(list_players_alive):
    coeff=0
    best_suspect=""
    for player in list_players_alive:
        if player.imp_coeff>coeff:
            best_suspect=player
            coeff=player.imp_coeff
    return best_suspect

