class Card:
    def __init__(self, name = "CARD", color = 'blue', icon = 'stalk', cost = 1, effect = 1, activation = [1]):
        self.name = name
        self.color = color
        self.icon = icon
        self.cost = cost
        self.activation = activation
    
    def __str__(self):
        return self.name
    
    def __repr__(self) :
        return self.name
    
    def print_info(self):
        print("Name: {}, Color: {}, Cost: {}, Activation: {}".format(self.name, self.color, self.cost, self.activation))

class OpeningDeck:
    """
    This class includes all the cards in the base game of Machi Koro
    """
    def __init__(self):
        self.card_types = []
        self.card_amounts = [6]*12 + [4]*7
        self.card_types.append(Card(name = "Wheat Field",               color = 'blue',   icon = 'stalk',   cost = 1, activation = [1]))
        self.card_types.append(Card(name = "Ranch",                     color = 'blue',   icon = 'cow',     cost = 1, activation = [2]))
        self.card_types.append(Card(name = "Forest",                    color = 'blue',   icon = 'gear',    cost = 3, activation = [5]))
        self.card_types.append(Card(name = "Mine",                      color = 'blue',   icon = 'gear',    cost = 6, activation = [9]))
        self.card_types.append(Card(name = "Apple Orchard",             color = 'blue',   icon = 'stalk',   cost = 3, activation = [10]))
        self.card_types.append(Card(name = "Bakery",                    color = 'green',  icon = 'bread',   cost = 1, activation = [2,3]))            
        self.card_types.append(Card(name = "Convenience Store",         color = 'green',  icon = 'bread',   cost = 2, activation = [4]))
        self.card_types.append(Card(name = "Cheese Factory",            color = 'green',  icon = 'factory', cost = 5, activation = [7]))
        self.card_types.append(Card(name = "Furniture Factory",         color = 'green',  icon = 'factory', cost = 3, activation = [8]))
        self.card_types.append(Card(name = "Fruit and Vegatable Market",color = 'green',  icon = 'fruit',   cost = 2, activation = [11, 12]))
        self.card_types.append(Card(name = "Cafe",                      color = 'red',    icon = 'gear',    cost = 6, activation = [3]))
        self.card_types.append(Card(name = "Family Restaurant",         color = 'red',    icon = 'gear',    cost = 6, activation = [9,10]))
        self.card_types.append(Card(name = "Stadium",                   color = 'purple', icon = 'tower',   cost = 6, activation = [6]))
        self.card_types.append(Card(name = "TV Station",                color = 'purple', icon = 'tower',   cost = 7, activation = [6]))
        self.card_types.append(Card(name = "Business Center",           color = 'purple', icon = 'tower',   cost = 8, activation = [6]))
        self.card_types.append(Card(name = "Train Station",             color = 'orange', icon = 'tower',   cost = 4, activation = []))
        self.card_types.append(Card(name = "Shopping Mall",             color = 'orange', icon = 'tower',   cost = 10,activation = []))
        self.card_types.append(Card(name = "Amusement Park",            color = 'orange', icon = 'tower',   cost = 16,activation = []))
        self.card_types.append(Card(name = "Radio Tower",               color = 'orange', icon = 'tower',   cost = 22,activation = []))
    
    def restart(self):
        self.card_amounts = [6]*12 + [4]*7