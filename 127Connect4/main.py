import connect4ai

ai = connect4ai.Player()

def start():
    n=6
    grids = [[0]*7 for _ in range(6)]
    print("Current Board:")
    print(*grids,sep='\n')
    player = 1
    domove(grids,player,n)
        
def check_if_won(grids,player,n):
    if horcheck_won(grids,player) or diagcheck_won(grids,player,n) or vertcheck_won(grids,player,n):
        return print(f"Player {player} won the game")
    if player == 1:
        player = 2
    else:
        player = 1
    domove(grids,player,n)

def domove(grids,player,n):
    move=0
    if player == 1:
        while not 0 < move <= 7:
            try:
                move = int(input(f"Which coloumn do you want to place your checker in (1-6)?"))
            except ValueError:
                print("Invalid Column number")
    else:
        move = ai.get_move(grids)
        print(str(move))
    num=0
    for grid in grids:
        if num == 0:
            if grids[0][move-1] != 0:
                print("That column is full")
                domove(grids,player,n)
        if grid[move-1] == 0:
            if num == 5:
                grids[num][move-1]=player
            else:
                num+=1
        else:
            grids[num-1][move-1]=player
    print_table(grids)
    check_if_won(grids,player,n)

def print_table(grids):
    print(*grids,sep='\n')

def horcheck_won(grids, player):
    amount = 0
    for grid in grids:
        for cell in grid:
            if cell == player:
                amount+=1
                if amount >= 4:
                    return True
            else:
                amount=0
        amount=0
    return False

def vertcheck_won(grids,player,n):
    amount = 0
    for i in range(7):
        for grid in grids:
            if grid[i] == player:
                amount+=1
                if amount >= 4:
                    return True
            else:
                amount = 0
        amount = 0
    return False

def diagcheck_won(grids, player, n):
    for x in range(3):
        for y in range(3, 6):
            if grids[x][y] == player and grids[x+1][y-1] == player and grids[x+2][y-2] == player and grids[x+3][y-3] == player:
                return True

    for x in range(3):
        for y in range(3):
            if grids[x][y] == player and grids[x+1][y+1] == player and grids[x+2][y+2] == player and grids[x+3][y+3] == player:
                return True
 
start()