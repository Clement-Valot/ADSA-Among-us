from players import *
from AVL_tree import *


def RandomGames(list_players):
    random_game=1
    for i in range (3):
        AVL, root = CreateAVL(list_players)
        #In order to avoid players to play against the same players during the 3 random games,
        #We chose to separate them thanks to the inorder, preorder and postorder sorting algorithm
        if(random_game==1):
            list_players=AVL.inorderTraversal(root)
        elif(random_game==2):
            list_players=AVL.PostorderTraversal(root)
        elif(random_game==3):
            list_players=AVL.PreorderTraversal(root)

        for player in list_players:
            player.updateScore(random_game)
        random_game+=1
    AVL, root = CreateAVL(list_players)
    list_players=AVL.inorderTraversal(root)
    UpdateRankingPlayers(list_players)
    print("\nHere are the scores and ranking after the 3 random games:")
    DisplayPlayers(list_players)

def RankedGames(list_players):
    print("\n\n\nLet's begin the ranked games with elimination!")
    ranked_game=1
    #Optionnal array retrieving eliminated players to keep track of all of them and not only the 10 best.
    eliminated_players=[]
    #We create the loop that is going to generate the matches leading to 10 remaining players
    #The loop is going from 0 to 8 so 9 rounds will be held.
    #Indeed, since we eliminate 10 players per round, we need 9 rounds to eliminate 90 players.
    for i in range (9):
        #Since we don't care about points counting, meaning we assign a random amount of points at each game,
        #we don't need to separate players into different games each containing 10 players in a ranking order.
        # All we need to do is just update the player's score directly from the list 
        for player in list_players:
            player.updateScore(ranked_game+3)
            #We have to consider the 3 random games for calculating the mean score
        
        #Now, we need to update their ranking and to do so, we are going to put every players
        #in another AVL_Tree and then extract all the players with an inorder sorting algo
        #to finally delete the 10 last players of the tournament (aka the 10 first in the list)
        AVL_postgame, root= CreateAVL(list_players)
        #Then we order those players in a list from the worst to the best with an inorder sorting algo
        list_players=AVL_postgame.inorderTraversal(root)
        #We update their ranking (optionnal but still informative)
        UpdateRankingPlayers(list_players)
        #We delete the 10 first players of the list because the inorder algo place players in a list
        #from worst (least point) to best (most point)
        eliminated_this_round = DeleteLastPlayers(list_players)
        eliminated_players += eliminated_this_round
        print("\n\nPlayers who have been eliminated on round {} are:".format(ranked_game))
        DisplayPlayers(eliminated_this_round)
        #The 10 worst players have been removed from the tournament, so we can now repeat the same process
        #until 10 players remain
        print("\nHere are the scores and ranking after the game {} :".format(ranked_game))
        DisplayPlayers(list_players)
        ranked_game+=1
    return eliminated_players, list_players

def FinalGames(list_players):
    print("\n\n\nLet's start the final games between the top 10 players!")
    #We start by reinitializing each player's score to 0
    ResetScore(list_players)
    print("\n\nHere are the 10 finalists of the tournament: (Scores are reset to 0)")
    DisplayPlayers(list_players)
    #We want them to play 5 games and then display the winners.
    #Therefore, we don't need to update the AVL tree at each round or eliminate some players,
    #all we are going to do is update their score 5 times in a row to simulate 5 games:
    for final_game in range (1,6):
        for player in list_players:
            player.updateScore(final_game)
    #At the end of those 5 games, we put these 10 players in an AVL Tree
    AVL_postgame, root= CreateAVL(list_players)
    #Then we order those players in a list from the worst to the best with an inorder sorting algo
    list_players=AVL_postgame.inorderTraversal(root)
    #We update their ranking to get the podiums
    UpdateRankingPlayers(list_players)
    #We display the 3 best players
    print("\n\nthe best player of the tournament is : {} with {} points".format(list_players[9].name,list_players[9].score))
    print("the second best player of the tournament is : {} with {} points".format(list_players[8].name,list_players[8].score))
    print("the third best player of the tournament is : {} with {} points".format(list_players[7].name,list_players[7].score))
    for i in range (7):
        print("{}th : {} with {} points".format(list_players[6-i].ranking, list_players[6-i].name,list_players[6-i].score))

if __name__=='__main__' :
    list_players= CreatePlayers(100)
    RandomGames(list_players)
    eliminated_players, list_players =RankedGames(list_players)
    FinalGames(list_players)
    
    
