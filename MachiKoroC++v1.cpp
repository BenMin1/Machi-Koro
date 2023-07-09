/*
Property ID Reference
    Blue cards:
        0 Wheat Field, 1 Ranch, 2 Forest, 3 Mine, 4 Apple Orchard,
    Green cards:
        5 Bakery, 6 Convenience Store, 7 Cheese Factory, 8 Furniture Factory, 9 Fruit Market,
    Red cards:
        10 Cafe, 11 Family Resturant,
    Purple cards:
        12 Stadium, 13, TV Station, 14 Business Center,
    Landmark cards
        15 Train Station, 16 Shopping Mall, 17 Amusement Park, 18 Radio Tower
*/ 

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class Player {
    public:
        int cards [19];
        int coins;
        string name;

        //Bank Constructor
        Player() {
            for(int i=0; i<=19; i++){
                cards[i] = 6;
            }
            coins = 999;
            name = "bank";
        }

        //player Constructor
        Player(string a) {
            for(int i=0; i<=18; i++){
                cards[i] = 0;
            }
            cards[0] = 1;
            cards[5] = 1;
            coins = 3;
            name = a;
        }

    friend ostream & operator<<(ostream &os, Player a){
        os<< " player " << a.name << " has cards: " << "\n \t";
        for(int i = 0; i <=18; i++){
            os<<a.cards[i];
            if(i==4||i==9||i==11||i==14) cout << "\n \t";
        } 
        os<< endl << "with " << a.coins << " coins" << endl; 
        return os; 
    }
    
    bool operator==(Player& b){
        return(b.name == name && coins == b.coins);
    }
};

Player whoTurn(int turn, int players, Player player1, Player player2, Player player3, Player player4){ 
    //Return the players whose turn it is
        if(turn % players == 0) return player1;
        if(turn % players == 1) return player2;
        if(turn % players == 2) return player3;
        if(turn % players == 3) return player4;
        return player4;
}

void pay(Player& x, Player& y, int pos, Player temp2, Player temp, Player &player1, Player &player2, Player &player3, Player &player4){
//Player x pays Player y
    int multi = 1;

    //Multiplier is 3 for Family Resturant
    if(pos == 11) multi = 3;

    //Add 1 to multiplier if Shopping Mall is owned
    if(y.cards[16] == 1) multi ++;

    int owed = multi * y.cards[pos];

    //Amount owed is 2 for stadium
    if(pos == 12) owed = 2;

    //Amount owed is 5 for TV Station
    if(pos == 13) owed = 5;
    
    //Pay in full when possible
    if(x.coins > owed){
        x.coins -= owed;
        y.coins += owed;
    }
    //Otherwise pay all
    if(x.coins < owed){
        y.coins += x.coins;
        x.coins = 0;
    }
    
    //Update the players
    if(temp2 == player1) 
        player1 = y;
    if(temp2 == player2) 
        player2 = y;
    if(temp2 == player3) 
        player3 = y;
    if(temp2 == player4) 
        player4 = y;
        
    if(temp == player1) 
        player1 = x;
    if(temp == player2) 
        player2 = x;
    if(temp == player3) 
        player3 = x;
    if(temp == player4) 
        player4 = x;
}

int main(){
    srand(time(0));
    int numPlayers = 4;
    int turn = 0;
    int dice = 1;
    int totalRoll = 0;
    int landmarks;
    int rollAgain = 1;
    int j;
    int buy;
    int purpleCards;
    int cost[19] = {
        1,1,3,6,3, 
        1,2,5,3,2,
        2,3,
        6,7,8,
        4,10,16,22
    };
    
    Player bank;
    Player player1("Jon");
    Player player2("Jawn");
    Player player3("John");
    Player player4("Jhon");    
    Player current;
    Player cc;
    Player temp;
    Player temp2;
    
    //set Max turns
    while(turn != 999){
        rollAgain = 1;
        current = whoTurn(turn,  numPlayers, player1,  player2,  player3,  player4);
        temp = current;
        purpleCards = current.cards[12] + current.cards[13] + current.cards[14];
        cout << current.name << endl;

//if train station owned, ask for dice amount
        if(current.cards[16] == 1){
            cout << "Roll with 1 or 2 dice?";
            cin >> dice;
            if(dice > 2 || dice < 1) dice = 1;
        }

//calculate roll
        for(int i = 0; i < dice; i++){
            j = 1 + (rand() % 6);
            cout << "die " << i+1 << " rolled " << j;
            totalRoll += j;
        }
        cout << " for a total of " << totalRoll << endl;

//if Radio Tower is owned ask for reroll
        if(current.cards[18] == 1){
            int YoN;
            cout << "Roll again? Enter 1 for yes or 0 for no";
            cin >> YoN;
            if(YoN == 1){
                totalRoll = 0;
                if(current.cards[16] == 1){
                    cout << "Roll with 1 or 2 dice?";
                    cin >> dice;
                    if(dice > 2 || dice < 1) dice = 1;
                }

                for(int i = 0; i < dice; i++){
                    j = 1 + (rand() % 6);
                    cout << "die " << i+1 << " rolled " << j;
                    totalRoll += j;
                }
                cout << " for a total of " << totalRoll << endl;
            }
        }

//If amusement Park owned and doubles rolled, increment turn by 0
        if((totalRoll %2 == 0 & j == totalRoll/2 && current.cards[17] == 1)) rollAgain = 0;
        
// if red # rolled pay in counter-clockwise order
        if(totalRoll == 3 || totalRoll == 9 || totalRoll == 10){
            //set CoFR to 10 for cafe and 11 for Family Resturant
            int CoFR = 11;
            if (totalRoll == 3) CoFR = 10;

            for(int i = 1; i <= numPlayers-1; i++){
                if(current.coins == 0) break;
                cc = whoTurn(turn-i, numPlayers, player1, player2, player3, player4);
                temp2 = cc;
                pay(current,cc, CoFR, temp2, temp, player1, player2, player3, player4);
            }
        }

//if blue # rolled
        if(totalRoll == 1 || totalRoll == 2 || totalRoll == 5 || totalRoll == 9 || totalRoll == 10){
            int multi = 1;
            int id;

            //Wheat Field or Ranch
            if(totalRoll == 1 || totalRoll == 2) id = totalRoll - 1;
            //Forest
            if(totalRoll == 5) id = 2;
            //Mine
            if (totalRoll == 9){
                id = 3;
                multi = 5;
            }
            //Apple Orchard
            if (totalRoll == 10){
                id = 4;
                multi = 3;
            }
            
            player1.coins = (player1.coins + multi * player1.cards[id]);
            player2.coins = (player2.coins + multi *  player2.cards[id]);
            player3.coins = (player3.coins + multi *  player3.cards[id]);
            player4.coins = (player4.coins + multi *  player4.cards[id]);
        }

//if rolled a green #
    //bakery
        if(totalRoll == 2 || totalRoll == 3){
            int multi;
            multi = current.cards[15] + 1;
            current.coins = (current.coins + multi * current.cards[5]);
        }
    //convience store    
        if(totalRoll == 4){
            int multi;
            multi = current.cards[15] + 3;
            current.coins = (current.coins + multi * current.cards[6]);
        }
    //cheese factory
        if(totalRoll == 7){
            int multi;
            multi = current.cards[1] * 3;
            current.coins = (current.coins + multi * current.cards[7]);
        }
    //furniture factory
        if(totalRoll == 8){
            int multi;
            multi = (current.cards[2] + current.cards[3]) * 3;
            current.coins = (current.coins + multi * current.cards[8]);
        }
    //fruit market
        if(totalRoll == 1 || totalRoll == 12){
            int multi;
            multi = (current.cards[0] + current.cards[4]) * 2;
            current.coins = (current.coins + multi * current.cards[9]);
        }


//if roll purple
        if(totalRoll == 6){
            //if stadium owned
            if(current.cards[12] == 1){
                //Collect two coins from every player
                for(int i = 1; i <= numPlayers-1; i++){
                cc = whoTurn(turn-i, numPlayers, player1, player2, player3, player4);
                temp2 = cc;
                pay(cc,current, 12, temp2, temp, player1, player2, player3, player4);
                }
            }
            
            //if tv station owned
            if(current.cards[13] == 1){
            //Collect 5 coins from one player
                int steal = 100;
                cout << " Enter # of player to steal from \n";
                cin >> steal;
                while(steal > numPlayers){
                cout << "error";
                cin >> steal;
                }
                
                cc = whoTurn(steal-1, numPlayers, player1, player2, player3, player4);
                temp2 = cc;
                pay(cc,current, 13, temp2, temp, player1, player2, player3, player4);
            }

            //if business center owned
            if(current.cards[14] ==1){
            //Exchange one property
                int steal = 100;
                int ownedProp = 100;
                int stolenProp = 100;
                cout << " Enter player # then owned property ID then stolen property ID \n";
                cin >> steal >> ownedProp >> stolenProp;
                cc = whoTurn(steal-1, numPlayers, player1, player2, player3, player4);
                temp = cc;
                while(steal > numPlayers || ownedProp > 11 || stolenProp > 11 || current.cards[ownedProp] == 0 || cc.cards[stolenProp] == 0){
                    cout << "error";
                    cin >> steal >> ownedProp >> stolenProp;
                    cc = whoTurn(steal-1, numPlayers, player1, player2, player3, player4);
                }

                current.cards[ownedProp] --;
                current.cards[stolenProp] ++;
                cc.cards[ownedProp] ++;
                cc.cards[stolenProp] --;

                //update player stolen from
                if(temp == player1) 
                    player1 = cc;
                if(temp == player2) 
                    player2 = cc;
                if(temp == player3) 
                    player3 = cc;
                if(temp == player4) 
                    player4 = cc;
            }
        }
        
//buying
        cout << current.name << " has " << current.coins << " coins \n";
        cout << "Enter property ID or -1 to pass ";
        cin >> buy;
        
        if(buy >= 0 && buy <= 18 && bank.cards[buy] >= 1 && current.coins > cost[buy]){
            //check for exceptions
            if(buy > 11){
                if(current.cards[buy] == 1) buy = -1;
                if(buy > 11 && buy < 15 && purpleCards == 1) buy = -1;
            }

            current.cards[buy]++;
            current.coins -= cost[buy];
            bank.cards[buy]--;
        }
        buy = -1;

        //update player
        if(temp == player1) 
            player1 = current;
        if(temp == player2) 
            player2 = current;
        if(temp == player3) 
            player3 = current;
        if(temp == player4) 
            player4 = current;        
        
        //check for win
        landmarks = current.cards[15] + current.cards[16] + current.cards[17] + current.cards[18];
        if(landmarks == 4){
            break;
        }

        landmarks = 0;
        turn += rollAgain;
        cout<< "NEW TURN \n";
        totalRoll = 0;
    }
    cout << current.name << " is the winner";
    return 0;
}
