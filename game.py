import os
import time 
import sqlite3
import sys
players=["Adams","Hillary","Julian","Alves","Jonson","Snoop","Albert"]
health=[10,20,40,80,160,320,640]
cost=[0,50,100,200,400,800,1600]
wallet = 0
db="game.db"
def create_database():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists status(
    id integer AUTOINCREMENT primary key unique not null,
    player varchar(20) unique not null,
    wallet integer not null,
    gold int default 0,
    diamon int default 0    
    )""")
    cursor.execute("INSERT INTO status( player,wallet) values(?,?,?) ", (players[0], wallet))
    print("Process complete!")
    conn.commit()
    conn.close()
    
def view_myplayers():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()    
    cursor.execute("SELECT * from status")
    mine = cursor.fetchone()
    print(f'Current player id: {mine[0]} Player_name:   {mine[1]}')
    conn.close()
    
def my_account():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()    
    cursor.execute("SELECT wallet, gold, diamon from status")
    account = cursor.fetchone()
    print(f'Coins: {account[0]}$|  Gold: {account[1]} | Diamond: {account[2]}')
    conn.close()
        
def buyplayer():
    showplayers()
    for i in range(0,len(cost)):
        if wallet >= cost[i] and cost >=10:
            print("You are eligible for")
            print(f"{i+1}.Player: {players[i]}  Health: {health[i]}units  Cost: {cost[i]}$")
        else:
            print("You have insufficient funds!")
            print("Play again to stand higher chance of buying a player")
                        
def showplayers():
    for i in range (0, len(players)):
        print(f"{i+1}.Player: {players[i]}  Health: {health[i]}units  Cost: {cost[i]}$")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Select player")    
buyplayer()       
