import Player
import AVL_Tree


def RandomGames(list_players):
    for i in range (3):
        AVL_Tree=createAVL(list_players)
        root=none
        #In order to avoid players to play against the same players during the 3 random games,
        #We chose to separate them thanks to the inorder, preorder and postorder sorting algorithm
        if(i==0):
            list_players=AVL_Tree.inorderTraversal(root)
        elif(i==1):
            list_players=AVL_Tree.PostorderTraversal(root)
        elif(i==2):
            list_players=AVL_Tree.PreorderTraversal(root)

        for player in list_players:
            player.updateScore()
    
    return list_players


def RankedGames(list_players):
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
            player.updateScore()
        
        #Now, we need to update their ranking and to do so, we are going to put every players
        #in another AVL_Tree and then extract all the players with an inorder sorting algo
        #to finally delete the 10 last players of the tournament (aka the 10 first in the list)
        AVL_Tree_postgame=createAVL(list_players)
        #Then we order those players in a list from the worst to the best with an inorder sorting algo
        root=none
        list_players=AVL_Tree.inorderTraversal(root)
        #We update their ranking (optionnal but still informative)
        UpdateRankingPlayers(list_players)
        #We delete the 10 first players of the list because the inorder algo place players in a list
        #from worst (least point) to best (most point)
        #Each time we delete the worst player, the second worst player takes the place of the popped 
        #worst player at index 0. Therefore we have to pop the element at index 0 10 times.
        for i in range (10):
            eliminated_players.append(list_players[0])
            list_players.pop(0)

        #The 10 worst players have been removed from the tournament, so we can now repeat the same process
        #until 10 players remain
    return list_players, eliminated_players

def FinalGames(list_players):
    #We start by reinitializing each player's score to 0
    ResetScore(list_players)
    #We want them to play 5 games and then display the winners.
    #Therefore, we don't need to update the AVL tree at each round or eliminate some players,
    #all we are going to do is update their score 5 times in a row to simulate 5 games:
    for i in range (5):
        for player in list_players:
            player.updateScore()
    #At the end of those 5 games, we put these 10 players in an AVL Tree
    AVL_Tree_postgame=createAVL(list_players)
    #Then we order those players in a list from the worst to the best with an inorder sorting algo
    root=none
    list_players=AVL_Tree.inorderTraversal(root)
    #We update their ranking to get the podiums
    UpdateRankingPlayers(list_players)
    #We display the 3 best players
    print("the best player of the tournament is : ",list_players[9].name)
    print("the second best player of the tournament is : ",list_players[8].name)
    print("the third best player of the tournament is : ",list_players[7].name)
    for i in range (7):
        print(list_players[6-i].ranking,"th : ",list_players[6-i].name)