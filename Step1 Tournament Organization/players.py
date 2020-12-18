import random 

class Player:
    def __init__(self, name, ranking, score=0):
        self.name = name
        self.score = score
        self.ranking = ranking
    
    #We update player's score by adding a random number between 0 and 6 twice 
    #so that we raise chances of getting middle numbers like 6,7,8.
    def updateScore(self,game):
        score_game= random.randint(0,6)+random.randint(0,6)
        self.score= self.score * (game-1)/game + score_game/game

#Function to reset the scores of all players in the list_players to 0.
#Usefull when we get into the final step of the tournament with the 10 best players.
def ResetScore(list_players):
    for player in list_players:
        player.score=0

#Update the rank of the players inside the list.
#The first player in the list is ranked at the same number as the length of the list.
#Until the last player of the list ranked 1.
def UpdateRankingPlayers(list_players):
    ranking=len(list_players)
    for player in list_players:
        player.ranking=ranking
        ranking-=1

#Each time we delete the worst player, the second worst player takes the place of the popped 
#worst player at index 0. Therefore we have to pop the element at index 0 10 times.
def DeleteLastPlayers(list_players):
    eliminated=[]
    for i in range(10):
        eliminated.append(list_players.pop(0))
    return eliminated

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

#Method that puts batch of 10 players in different games while updating their score
def CreateGames(list_players, number_game):
    games=[]
    game=[]
    for player in list_players:
        #tous les 10 joueurs, on ajoute la liste des 10 joueurs d'une game dans la liste des games.
        #On prend bien soin de réinitialiser la liste d'une game pour la re-remplir de 10 joueurs.
        if player.ranking%10==1 and player.ranking!=1:
            games.append(game)
            game=[]
        game.append(player)
        #In the same time we add those players in different games, we update their score.
        player.updateScore(number_game)
        #We have to consider the 3 random games for calculating the mean score
    return list_players

#This method creates all the 100 players with their name, their initial score (0)
#and their ranking depending on where their name was in the text file (not relevant at the beginning)
def CreatePlayers(nb_players):
    pseudos = listPlayersName("participants.txt")
    #pseudos = listPlayersName("Step1 Tournament Organization/participants.txt")
    list_players=[]
    for i in range (nb_players):
        list_players.append(Player(pseudos[nb_players-i-1],nb_players-i))
    DisplayPlayers(list_players)
    return list_players

#Simply display players on the console with rank, name and score.
def DisplayPlayers(list_players):
    length=len(list_players)
    for i in range(length):
        player=list_players[length-i-1]
        tag="th"
        if player.ranking==1:
            tag="st"
        elif player.ranking==2:
            tag="nd"
        elif player.ranking==3:
            tag="rd"
        print("{}{} {} {}".format(player.ranking,tag,player.name,player.score))
