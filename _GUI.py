from tkinter import *
from tkinter import ttk
from _Cards import *
from _Players import *
from _MachiKoro import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.treeview = ttk.Treeview(root)
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        self.playButton = Button(self, text="Play", command=self.clickPlayButton)

        # place button at (0,0)
        exitButton.pack(side = BOTTOM)
        self.playButton.pack(side = TOP)

        self.entries = []
        self.buttons = []
        self.labels = []
    
        self.players = []
    def clear_buttons(self):
        for button in self.buttons: button.destroy()
        self.buttons = []
    def clear_entries(self):
        for entry in self.entries: entry.destroy()
        self.entries = []
    def clear_labels(self):
        for label in self.labels: label.destroy()
        self.labels = []

    def clickPlayButton(self):
        self.playButton.destroy()
        playercount_label = Label(root, text = "How many Players? ")
        playercount_label.place(x= 0 , y= 0)
        self.labels.append(playercount_label)

        for i in range(1,5):
            button = Button(self, text=str(i), command=lambda i=i:self.playerCount_click(i))
            button.pack()
            self.buttons.append(button)

    def clickExitButton(self):
        self.master.destroy()
        exit()

    def playerCount_click(self, num_players):
        
        for i in range(num_players):
            label = Label(root, text=f"Player {i+1}: ")
            label.pack()
            self.labels.append(label)
            entry = Entry(root)
            entry.pack()
            self.entries.append(entry)
        
        button = Button(root, text="Save Names", command=self.save_names)
        button.pack()
        print("players num is ", num_players)
        self.clear_buttons()
        self.buttons.append(button)
        # for button in self.buttons: button.destroy()
        #createPlayers(numPlayers)

    def create_table(self):
        self.treeview.place(x=0, y=0)
        names = ("Wheat Field","Ranch","Forest","Mine","Apple Orchard", "Bakery","Convenience Store","Cheese Factory","Furniture Factory","Fruit and Vegatable Market","Cafe","Family Restaurant",
                 "Stadium", "TV Station","Business Center", "Train Station","Shopping Mall","Amusement Park","Radio Tower")
        self.treeview["columns"] = tuple(range(1, 21))
        for i in range(1, 20):
            self.treeview.column(f"#{i}", width=100)
            self.treeview.heading(f"#{i}", text=names[i-1])

        self.treeview.column("#0", width=150)
        self.treeview.heading("#0", text="Players")
    def update_table(self):
        for player in self.players:
            self.treeview.insert("", "end", text=player.name, values= player.cards)

    def play_game(self):
        print("hello")
    def save_names(self):
        names = [entry.get() for entry in self.entries]
        self.clear_buttons()
        self.clear_entries()
        self.clear_labels()
        for name in names:
            player = Player(name= name)
            self.players.append(player)
            
        self.treeview.delete(*self.treeview.get_children())
        game = MachiKoro(players=self.players)
        game.ResetGame()
        self.create_table()
        self.update_table()
        self.play_game()
        # for player in players:
        #     label = Label(root, text=f"Player {player.name}: {player.cards}")
        #     label.pack()

root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")

root.mainloop()   
