board=[[1,0,0],[1,1,0],[0,0,1]]
def setup():
    size(400,400)
    background(255)
def draw():
    global board
    for i in range(len(board[0])):
        if(board[0][i]==1):
            rect(i*10+50,20,20,20)
        elif(board[0][i]==0):
            ellipse(i*10+55,25,10,10)
    for i in range(len(board[1])):
        if(board[1][i]==1):
            rect(i*10+50,30,10,10)
        elif(board[1][i]==0):
            ellipse(i*10+55,35,10,10)
    for i in range(len(board[2])):
        if(board[2][i]==1):
            rect(i*10+50,40,10,10)
        elif(board[2][i]==0):
            ellipse(i*10+55,45,10,10)
#frameRate(100)
#onLoop += draw
#loop()