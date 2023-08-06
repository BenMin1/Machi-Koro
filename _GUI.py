from tkinter import *
from _Players import *
def Create_GUI():

    def quit():
        root.destroy()

    def getPlayers():
        play_button.destroy()
        
        def playerCount_click(event):
            numPlayers = (event.widget.cget("text"))
            numPlayers = int(numPlayers)
            print("players num is ", numPlayers)
            for button in buttons:
                button.destroy()
            playercount_label.destroy()
            
            createPlayers(numPlayers)

        playercount_label = Label(root, text = "How many Players? ")
        playercount_label.pack()
        buttons = []
        for i in range(2,5):
            buttons.append(Button(root, text = str(i)))

        for button in buttons:
            button.pack()
            button.bind("<Button-1>", playerCount_click)  

    def getName(i):
        e = Entry(root, width = 50)
        e.pack()
        def named():
            global player_name
            player_name = e.get()
            button_name.destroy()
            e.destroy()
            player_frames[i].config(text = name)  

        j = str(i)
        i = int(i)
        button_name = Button(root, text="Enter Player " + j + "'s name", command = named)
        button_name.pack()  

    def createPlayers(numPlayers):
        info_frame = LabelFrame(my_frame, text="Game Info", bd =0)
        info_frame.grid(row=0,column=50,padx=20,ipadx=20)
        labelturn = Label(info_frame, text = "GAME SET-UP")
        labelturn.pack(side = RIGHT)
        labeldie = Label(info_frame, text = "")
        labeldie.pack(side = RIGHT, pady = 20, padx = 20)
        
        var = []
        players = []
        player_frames = []
        player_labels = []
        name = StringVar()
        for i in range(numPlayers):
            var.append ( StringVar())
            var[i].set("coins = 3 cards = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]")
            player_frames.append (LabelFrame(my_frame, text="player1", bd =0))
            player_frames[i].grid(row=2*i,column=0,padx=20,ipadx=20)
            player_labels.append (Label(player_frames[i], textvariable=var[i]))
            player_labels[i].pack(pady=20)      
            player_frames[i].config(text = name)  

    #Create Tkinter Window
    root = Tk()
    root.title('MACHI KORO GAME')
    root.geometry("900x500")
    root.configure(background = "blue")

    my_frame = Frame(root, bg = "blue")
    my_frame.pack(pady=20)

    quit_button = Button(root,text="QUIT", command = quit)
    quit_button.pack(side = BOTTOM)

    play_button = Button(root, text="NEW GAME", command = getPlayers)
    play_button.pack(side = TOP)
    
    root.mainloop()

    