class Player():

    def __init__(self, name = "Player"):
        # These are the starting values for a new game. They need to be reset every game
        self.name = name
        self.coins = 3
        self.cards  = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.blue_cards = []
        self.green_cards = []
        self.red_cards = []
        self.purple_cards = []
        self.landmasrk_cards = []
        # These are the overall stats of the player over many games
        self.gamesPlayed = 0
        self.gamesWon = 0

    def print_player_info(self):
        print(f"Name: {self.name}")
        print(f"Coins: {self.coins}")
        print(f"Cards: {self.cards} \n")

    def print_stats(self):
        print(f"{self.name} played {self.gamesPlayed} games and won {self.gamesWon} games. Win percentage {100* self.gamesWon / self.gamesPlayed} \n")
    
    def choose_dice(self, other_players):
        return 1
    
    def choose_reroll(self, other_players):
        return False
    
    def choose_buy(self, other_players):
        return 1  
    
    def check_win (self):
        return len(self.landmasrk_cards) == 4
    
    def game_info(self):
        return [self.coins, self.cards]