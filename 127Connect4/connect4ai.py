from random import randint


class Player:
    def __init__(self):
        pass

    def get_move(self,grids):
        test_grids = grids
        player = 2
        n = 6
        x=0
        for grid in test_grids:
            i = 0
            for cell in grid:
                if cell == 0:
                    test_grids[x][i] = player
                    ai_will_win = self.check_if_won(test_grids,player,n)
                    if ai_will_win:
                        test_grids[x][i] = 0
                        return i+1
                    test_grids[x][i] = 0
                i+=1
            x+=1
        player = 1
        test_grids = grids
        x=0
        for grid in test_grids:
            i = 0
            for cell in grid:
                if cell == 0:
                    test_grids[x][i] = player
                    player_will_win = self.check_if_won(test_grids,player,n)
                    if player_will_win:
                        test_grids[x][i] = 0
                        return i+1
                    test_grids[x][i] = 0
                i+=1
            x+=1
        return randint(1,6)


    def check_if_won(self,grids,player,n):
        if self.horcheck_won(grids,player) or self.diagcheck_won(grids,player,n) or self.vertcheck_won(grids,player,n):
            return True

    def horcheck_won(self,grids, player):
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

    def vertcheck_won(self,grids,player,n):
        amount = 0
        for i in range(n):
            for grid in grids:
                if grid[i] == player:
                    amount+=1
                    if amount >= 4:
                        return True
                else:
                    amount = 0
            amount = 0
        return False

    def diagcheck_won(self, grids, player, n):
        for x in range(n - 3):
            for y in range(3, n):
                if grids[x][y] == player and grids[x+1][y-1] == player and grids[x+2][y-2] == player and grids[x+3][y-3] == player:
                    return True

        for x in range(n - 3):
            for y in range(n - 3):
                if grids[x][y] == player and grids[x+1][y+1] == player and grids[x+2][y+2] == player and grids[x+3][y+3] == player:
                    return True


                
                

        