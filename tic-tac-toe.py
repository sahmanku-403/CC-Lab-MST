grid = [['-','-','-'],['-','-','-'],['-','-','-']]


def showGrid():
    global grid
    for row in grid:
        print(row[0], row[1], row[2])
def didSomeoneWin(ch):
    global grid
    if(grid[0][0] == ch and grid[1][1] == ch and grid[2][2] == ch):
        return True
    if(grid[0][2] == ch and grid[1][1] == ch and grid[2][0] == ch):
        return True
    for i in range(0,3):
        if(grid[0][i] == ch and grid[1][i] == ch and grid[2][i] == ch):
            return True
        if(grid[i][0] == ch and grid[i][1] == ch and grid[i][2] == ch):
            return True
def Player1Input():
    inp = input("Player 1 enter comma separated x, y values: ").split(',')
    x, y = int(inp[0]), int(inp[1])
    return x, y
def Player2Input():
    inp = input("Player 2 enter comma separated x, y values: ").split(',')
    x, y = int(inp[0]), int(inp[1])
    return x, y
    
def main():
    global grid
    showGrid()
    for i in range(0,9):
        if(i%2==0):
            x,y = Player1Input()
            grid[x][y] = 'X'
        else:
            x,y = Player2Input()
            grid[x][y] = 'O'
        showGrid()
        if (didSomeoneWin('X')):
            print("PLAYER 1 WINS!")
            return
        if(didSomeoneWin('O')):
            print("PLAYER 2 WINS!")
            return
        
        
main()
