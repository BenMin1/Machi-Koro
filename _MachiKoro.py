import numpy as np
prices = [1,1,3,6,3,1,2,5,3,2,2,3,6,7,8,4,10,16,22]
bank = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]

class MachiKoro():

    def __init__(self, players):
        # The only thing needed to start a new game is an array with players in it
        self.num_players = len(players)
        self.players = players
        self.turn_counter = 0

    def ResetGame(self):
        self.turn_counter = 1
        for player in self.players:
            player.coins = 3
            player.cards = "Starting Cards"

    def Payouts(self, player):
        PayRedCards()
        CollectBlueCards()
        CollectGreenPurpleCards()

    def Buying(self, player):
        buy_attempt = player.choose_buy(other_players)
        if buy_attempt is good then buy it otherwise run it again
      
    def Turn (self, player):
        # Player chooses how many dice to roll. The player needs a train station to have the option to roll 2 dice
        dice = player.choose_dice()
        roll = sum(np.random.randint(1, 7, size = dice))

        # Player chooses if they want to roll again. The player needs the Radio Tower to have this option
        if("Player has Radio Tower"): player.choose_reroll(roll)

        # Now that we know the dice roll everyone gets payed
        self.Payouts()

        # The next step is the buying phase where the player can decide to buy a card
        self.Buying(player)

        # If the player rolled doubles and has the amusement park then they can take another turn once
        if that is true: self.Turn(player)

        # Check if the player won. If the turn returns true than the player won the game
        return player.check_win()
    
    def Game(self):
        # First set up a new game by resetting everyones coins and cards
        self.ResetGame()
        anyoneWin = False
        while(anyoneWin == False):
            for player in self.players:
                anyoneWin = self.Turn (player)
                if anyoneWin == True: break
