import numpy as np
from random import shuffle
from tkinter import *
from _Cards import *

class MachiKoro():

    def __init__(self, players = []):
        # The only thing needed to start a new game is an array with players in it.
        self.num_players = len(players)
        self.players = players
        self.turn_counter = 0
        self.Deck = OpeningDeck()        

    def ResetGame(self, shuffle_players = False):
        if shuffle_players == True: shuffle(self.players)
        self.turn_counter = 1
        self.Deck.restart()
        for i, player in enumerate(self.players):
            player.turn_order = i
            player.coins = 3
            player.cards = [1]+ [0] * 4 + [1] + [0]*13
            player.deck = self.Deck
            other_players = self.players[player.turn_order::-1] + self.players[:player.turn_order:-1]
            player.other_players = other_players[1:]
            player.gamesPlayed += 1

    def WinSequence(self, winner):
        print(winner.cards)
        winner.gamesWon += 1
        winner.turns.append (self.turn_counter)
        print(f"{winner.name} WON!!! Their win percentage is {100* winner.gamesWon / winner.gamesPlayed}")

#  Actions when 6 is rolled
    def Stadium_Roll(self, player):
        for other_player in self.players:
            if other_player == player : continue
            paid = min(2, other_player.coins)
            other_player.coins -= paid
            player.coins += paid

    def TV_Station_Roll(self, player):
        target_player = player.TV_Station_Action(self.players)
        paid = min(5, target_player.coins)
        target_player.coins -= paid
        player.coins += paid

    def Business_Center_Roll(self, player):
        target_player, target_card = player.Business_Center_Action(self.players)
        if target_player != player and target_card <12 and target_player.cards[target_card] > 0:
            target_player.cards[target_card] -= 1
            player.cards[target_card] += 1
        
    def Red_Payouts (self, red_index, cost, player_rolled, player_other):
        mall = player_other.check_mall()  
        owed = player_other.cards[red_index] * (cost + mall)
        paid = min(player_rolled.coins, owed)
        player_rolled.coins -= paid
        player_other.coins += paid
    
    def Blue_Payouts(self, roll, player):

        if roll    ==1: player.coins += player.cards[0]
        elif roll  ==2: player.coins += player.cards[1]
        elif roll  ==5: player.coins += player.cards[2]
        elif roll  ==9: player.coins += player.cards[3] * 5
        elif roll ==10: player.coins += player.cards[4] * 3
        else: return False
    
    def Green_Payouts(self, roll, player):
        if roll==2 or roll ==3:     player.coins +=  player.cards[4] * (1 + player.check_mall())
        elif roll  ==4:             player.coins +=  player.cards[5] * (3 + player.check_mall())
        elif roll  ==7:             player.coins +=  player.cards[6] * (3 * player.cards[1])
        elif roll  ==8:             player.coins +=  player.cards[7] * (3 * (player.cards[2] + player.cards[3]))
        elif roll ==11 or roll==12: player.coins +=  player.cards[8] * (2 * (player.cards[0] + player.cards[4]))
        else: return False
    
    def Purple_Payouts(self, player):
        if player.cards[12] ==1: self.Stadium_Roll(player)
        if player.cards[13] ==1: self.TV_Station_Roll(player)
        if player.cards[14] ==1: self.Business_Center_Roll(player)
    
    def Buy (self, player):
        buy_attempt = player.choose_buy(self.Deck)
        if buy_attempt ==19: return True
        elif (player.coins < self.Deck.card_types[buy_attempt].cost) or (self.Deck.card_amounts[buy_attempt] == 0): return False
        elif buy_attempt >=12 and buy_attempt<=14 and sum(player.cards[12:15]) == 1: return False
        elif buy_attempt >=15 and player.cards[buy_attempt] == 1: return False 
        else: 
            player.coins -= self.Deck.card_types[buy_attempt].cost
            player.cards[buy_attempt] += 1
            self.Deck.card_amounts[buy_attempt] -=1
            return True

    def Turn (self, player, doubles = False):
        # Player chooses how many dice to roll. The player needs a train station to have the option to roll 2 dice
        if(player.cards[15]== 0):dice_num = 1
        else: dice_num = 1 + player.roll2()

        dice_roll = np.random.randint(1, 7, size = dice_num)
        roll = sum(dice_roll)

        # Player chooses if they want to roll again. The player needs the Radio Tower to have this option
        if(player.check_radio(roll)): 
            dice_roll = np.random.randint(1, 7, size = dice_num)
            roll = sum(dice_roll)

        # Now that we know the dice roll check for red cards from other players
        if (roll == 3 or roll == 9 or roll == 10) and player.coins > 0: 
            if roll == 3:               red_index = 10; cost = 1
            if roll == 9 or roll == 10: red_index = 11; cost = 2
            other_player = self.players[player.turn_order::-1] + self.players[:player.turn_order:-1]
            for player_other in other_player[1:]:
                if player_other == player: continue 
                self.Red_Payouts(red_index = red_index, cost = cost, player_rolled = player, player_other = player_other)

        # If the roll has a blue card then everyone checks their blue cards
        if (roll == 1 or roll == 2 or roll ==5 or roll == 9 or roll == 10):
            for blue_player in self.players: self.Blue_Payouts(roll=roll, player=blue_player)

        # Player now checks green cards
        self.Green_Payouts(roll= roll, player=player)

        #Lastly check for purple cards if 6 is rolled
        if roll == 6: self.Purple_Payouts(player= player)

        # The next step is the buying phase where the player can decide to buy a card
        buy_card = self.Buy(player)

        # If the player rolled doubles and has the amusement park then they can take another turn once
        if (dice_num == 2 and doubles == False and player.check_Amusement(dice_roll) ): self.Turn(player, doubles = True)

        # Check if the player won. If the turn returns true than the player won the game
        return player.check_win()
    
    def Game(self, shuffle_players = False):
        # First set up a new game by resetting everyones coins and cards
        self.ResetGame(shuffle_players)
        anyoneWin = False
        while(anyoneWin == False):
            for player in self.players:
                anyoneWin = self.Turn (player)
                if anyoneWin == True: winner = player; break
            self.turn_counter += 1
        self.WinSequence(winner)
