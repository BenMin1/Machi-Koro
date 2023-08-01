import numpy as np

Name2Num = {
    "Wheat Field"               : 0   
    ,"Ranch"                     : 1   
    ,"Forest"                    : 2   
    ,"Mine"                      : 3   
    ,"Apple Orchard"             : 4   
    ,"Bakery"                    : 5   
    ,"Convenience Store"         : 6   
    ,"Cheese Factory"            : 7   
    ,"Furniture Factory"         : 8   
    ,"Fruit and Vegatable Market": 9   
    ,"Cafe"                      : 10 
    ,"Family Restaurant"         : 11 
    ,"Stadium"                   : 12 
    ,"TV Station"                : 13 
    ,"Business Center"           : 14 
    ,"Train Station"             : 15 
    ,"Shopping Mall"             : 16 
    ,"Amusement Park"            : 17 
    ,"Radio Tower"               : 18 
}
Num2Name = {
    0  :"Wheat Field"                 
    , 1  :"Ranch"                       
    , 2  :"Forest"                      
    , 3  :"Mine"                        
    , 4  :"Apple Orchard"               
    , 5  :"Bakery"                      
    , 6  :"Convenience Store"           
    , 7  :"Cheese Factory"              
    , 8  :"Furniture Factory"           
    , 9  :"Fruit and Vegatable Market"  
    , 10 :"Cafe"                       
    , 11 :"Family Restaurant"          
    , 12 :"Stadium"                    
    , 13 :"TV Station"                 
    , 14 :"Business Center"            
    , 15 :"Train Station"              
    , 16 :"Shopping Mall"              
    , 17 :"Amusement Park"             
    , 18 :"Radio Tower"                
}
class Player():

    def __init__(self, name = "Player"):
        # These are the starting values for a new game. They need to be reset every game
        self.name = name
        self.coins = 3
        self.cards  = np.array([0] * 19)
        self.turn_order = 0
        self.deck = []

        # These are the overall stats of the player over many games
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.cardHistory = [0]*19
    
    def __str__(self):
        return self.name
    
    def __repr__(self) :
        return self.name
    
    def print_player_info(self):
        print(f"Name: {self.name}")
        print(f"Coins: {self.coins}")
        for i,num_cards in enumerate(self.cards):
            print(f"{Num2Name[i]}: {num_cards} \n")

    def print_stats(self):
        print(f"{self.name} played {self.gamesPlayed} games and won {self.gamesWon} games. Win percentage {100* self.gamesWon / self.gamesPlayed} \n")
    
    def roll2(self):
        return False
    
    def check_radio(self, roll):
        return False
    
    def choose_buy(self, deck):
        for i,card in enumerate(deck.card_types):
            if deck.card_amounts[i]>0 and card.cost <= self.coins: 
                if (i >=12 and i <=14 and sum(self.cards[12:15]) == 1) or (i >=12 and self.cards[i] == 1): continue
                return i
        return 0

    def TV_Station_Action (self, players):
        if players[0]== self: target_player = players[1]
        else: target_player = players[0]
        return target_player
    
    def Business_Center_Action (self, players):
        if players[0]== self: target_player = players[1]
        else: target_player = players[0]
        
        for i in range(len(target_player.cards)): 
            if target_player.cards[i]>0: return target_player, i
    
    def check_mall (self):
        return self.cards[16]
    
    def check_Amusement (self, dice_roll):
        if(dice_roll[0] == dice_roll[1] and self.cards[17] == 1): return True
        else: return False      
    def check_win (self):
        return sum(self.cards[15:]) == 4
        
    def game_info(self):
        return [self.coins, self.cards]

class Player_1_Die_Strat(Player):
    def __init__ (self, name, turn_order = 0):
        super().__init__(name)
    
    def choose_buy(self, deck):
        order = [1,0,6,16,5,12,15,17,18,10]
        for i in order:
            if deck.card_amounts[i]>0 and deck.card_types[i].cost <= self.coins: 
                if (i >=12 and i <=14 and sum(self.cards[12:15]) == 1) or (i >=12 and self.cards[i] == 1): continue
                return i
        return 0

class Player_2_Die_Strat(Player):
    def __init__ (self, name, turn_order = 0):
        super().__init__(name)
    
    def roll2(self):
        return True
    
    def choose_buy(self, deck):
        order = [1,15,16,17,18,2,7,8,3,5,12,4,10]
        for i in order:
            if deck.card_amounts[i]>0 and deck.card_types[i].cost <= self.coins: 
                if (i >=12 and i <=14 and sum(self.cards[12:15]) == 1) or (i >=12 and self.cards[i] == 1): continue
                return i
        return 0