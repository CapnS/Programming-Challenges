import datetime
import os

numbers = {"1": ["  "," |", " |"], "2" : [" _ ",  " _|","|_ "], \
    "3": [" _ ", " _|", " _|"], "4": ["   ", "|_|", "  |"], \
    "5": [" _ ","|_ "," _|"], "6": [" _ ","|_ ", "|_|"], \
    "7": [" _ ", "  |", "  |"], "8": [" _ ", "|_|", "|_|"], \
    "9":[" _ ", "|_|","  |"], "0": [" _ ", "| |", "|_|"], \
    ":": ["   ", " • ", " • "]}
clear = lambda: os.system('cls')

while True:
    t = str(datetime.datetime.now().time())
    if float(t[6:12]) % 1 == 0: 
        t = t[:8]  
        clear()    
        for i in range(3):
            for x in t:
                print(numbers[x][i], end="", flush=True)
            print("")
        