import random 

class Player:
    def __init__(self, name, ranking, score=0):
        self.name = name
        self.score = score
        self.ranking = ranking
    
    #We update player's score by adding a random number between 1 and 12
    def updateScore(self):
        self.score+=random.randint(0,12)

def ResetScore(list_players):
    for player in list_players:
        player.score=0

def UpdateRankingPlayers(list_players):
    ranking=len(list_players)
    for player in list_players:
        player.ranking=ranking
        ranking-=1

#Put gamers pseudo in a list (about 100 different pseudos)
def listPlayersName(file_name):
    players_name=[]
    file = open(file_name,"r")
    for line in file:
        #At the end of each line we have a 
        name=""
        for i in range (len(line)-1):
            name+=line[i]
        players_name.append(name)
    return players_name

#This method creates all the 100 players with their name, their initial score (0)
#and their ranking depending on where their name was in the text file (not relevant at the beginning)
def CreatePlayers(nb_players, pseudos):
    list_players=[]
    for i in range (nb_players):
        list_players.append(Player(pseudos[i],i+1))
    return list_players

if __name__=='__main__' :
    pseudos = listPlayersName("participants.txt")
    list_players=CreatePlayers(100,pseudos)
    for i in range(len(list_players)):
        tag="th"
        if i==0:
            tag="st"
        elif i==1:
            tag="nd"
        elif i==2:
            tag="rd"
        print("{}: {} {}{}".format(list_players[i].name,list_players[i].score,list_players[i].ranking,tag))
