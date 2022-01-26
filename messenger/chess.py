import re
from PIL import Image

board1 = Image.open("pieces/Chess-board-with-letters_nevit_111.svg.png")

BB = Image.open("pieces/bb.png")
BK = Image.open("pieces/bk.png")
BN = Image.open("pieces/bn.png")
BP = Image.open("pieces/bp.png")
BQ = Image.open("pieces/bq.png")
BR = Image.open("pieces/br.png")

WB = Image.open("pieces/wb.png")
WK = Image.open("pieces/wk.png")
WN = Image.open("pieces/wn.png")
WP = Image.open("pieces/wp.png")
WQ = Image.open("pieces/wq.png")
WR = Image.open("pieces/wr.png")

new_width  = 210
new_height = 210

BB = BB.resize((new_width, new_height), Image.ANTIALIAS)
BK = BK.resize((new_width, new_height), Image.ANTIALIAS)
BN = BN.resize((new_width, new_height), Image.ANTIALIAS)
BP = BP.resize((new_width, new_height), Image.ANTIALIAS)
BQ = BQ.resize((new_width, new_height), Image.ANTIALIAS)
BR = BR.resize((new_width, new_height), Image.ANTIALIAS)
WB = WB.resize((new_width, new_height), Image.ANTIALIAS)
WK = WK.resize((new_width, new_height), Image.ANTIALIAS)
WN = WN.resize((new_width, new_height), Image.ANTIALIAS)
WP = WP.resize((new_width, new_height), Image.ANTIALIAS)
WQ = WQ.resize((new_width, new_height), Image.ANTIALIAS)
WR = WR.resize((new_width, new_height), Image.ANTIALIAS)

BBA = BB.convert('RGBA')
BKA = BK.convert('RGBA')
BNA = BN.convert('RGBA')
BPA = BP.convert('RGBA')
BQA = BQ.convert('RGBA')
BRA = BR.convert('RGBA')

WBA = WB.convert('RGBA')
WKA = WK.convert('RGBA')
WNA = WN.convert('RGBA')
WPA = WP.convert('RGBA')
WQA = WQ.convert('RGBA')
WRA = WR.convert('RGBA')



CRED = '\033[91m'
CEND = '\033[0m'
Cother = '\033[94m'
Cooo = '\033[100m'
class chesspiece:

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        self.type = "0"
    def pos(self):
        return self.pos
    def color(self):
        return self.color
    def type(self):
        return self.type

class poun(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="P"
        if (color == -1):
            self.type="p"
        self.ListOfmove()


    def checkmove(self , x1 , y1):


        if (self.color == 1):
            #print ("condition 1 = " + str(y1==self.pos[0]-1 and x1==self.pos[1] and board[y1][x1].type == "0"))
            #print ("condition 2 = " + str(((y1==self.pos[0]-1 and x1==self.pos[1]+1) or (y1==self.pos[0]-1 and x1==self.pos[1]-1)) and board[y1][x1].type != "0" and board[y1][x1].color == -1))
            if (y1==self.pos[0]-1 and x1==self.pos[1] and board[y1][x1].type == "0"):
                return 1
            elif(((y1==self.pos[0]-1 and x1==self.pos[1]+1) or (y1==self.pos[0]-1 and x1==self.pos[1]-1)) and board[y1][x1].type != "0" and board[y1][x1].color == -1 ):
                return 1
            elif(self.pos[0] == 6 and y1==self.pos[0]-2 and x1==self.pos[1] and board[y1][x1].type == "0"):
                return 1
        elif (self.color == -1):
            if (y1==self.pos[0]+1 and x1==self.pos[1] and board[y1][x1].type == "0"):
                return 1
            elif(((y1==self.pos[0]+1 and x1==self.pos[1]+1) or (y1==self.pos[0]+1 and x1==self.pos[1]-1)) and board[y1][x1].type != "0" and board[y1][x1].color == 1):
                return 1
            elif(self.pos[0] == 1 and y1==self.pos[0]+2 and x1==self.pos[1] and board[y1][x1].type == "0"):
                return 1
        else:
            return 0;
    def ListOfmove(self):
        self.list=[]
        if (self.color == 1):
            #print("position "+str(self.pos[0])+" "+str(self.pos[1])+" test position "+ str(self.pos[0]-1) + " " + str(self.pos[1]) + " result ")
            if (self.pos[0]-1 >= 0):
                if (self.checkmove(self.pos[1],self.pos[0]-1)==1):
                    self.list.append([self.pos[0]-1,self.pos[1]])

            #print("position "+str(self.pos[0])+" "+str(self.pos[1])+" test position "+ str(self.pos[0]-1) + " " + str(self.pos[1]+1) + " result " )
            if (self.pos[1]+1 < 8 and self.pos[0]-1 >= 0):
                if (self.checkmove(self.pos[1]+1,self.pos[0]-1)==1):
                    self.list.append([self.pos[0]-1,self.pos[1]+1])

            #print("position "+str(self.pos[0])+" "+str(self.pos[1])+" test position "+ str(self.pos[0]-1) + " " + str(self.pos[1]-1) + " result " )
            if (self.pos[1]-1 >= 0 and self.pos[0]-1 >= 0):
                if (self.checkmove(self.pos[1]-1,self.pos[0]-1)==1):
                    self.list.append([self.pos[0]-1,self.pos[1]-1])
            if (self.pos[0] == 6):
                if (self.checkmove(self.pos[1],self.pos[0]-2)==1):
                    self.list.append([self.pos[0]-2,self.pos[1]])

        if (self.color == -1):
            if (self.pos[0]+1 <8):
                if (self.checkmove(self.pos[1],self.pos[0]+1)==1):
                    self.list.append([self.pos[0]+1,self.pos[1]])
            if (self.pos[1]+1 <8 and self.pos[0]+1 < 8):
                if (self.checkmove(self.pos[1]+1,self.pos[0]+1)==1):
                    self.list.append([self.pos[0]+1,self.pos[1]+1])
            if (self.pos[1]-1 >=0 and self.pos[0]+1 <8):
                if (self.checkmove(self.pos[1]-1,self.pos[0]+1)==1):
                    self.list.append([self.pos[0]+1,self.pos[1]-1])
            if (self.pos[0] == 1):
                if (self.checkmove(self.pos[1],self.pos[0]+2)==1):
                    self.list.append([self.pos[0]+2,self.pos[1]])

    def list(self):
        return self.list

    def move(self , x1 , y1):

        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            if (self.color == -1 and self.pos[0] == 7):
                board[y1][x1]=Queen(x1,y1)
            if (self.color == 1 and self.pos[0] == 0):
                board[y1][x1]=Queen(x1,y1)
            else:
                board[y1][x1]=self
                self.pos=[y1,x1]
            self.ListOfmove()
            return 1;
        else :

            return 0;

class King(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="K"
        if (color == -1):
            self.type="k"
        self.ListOfmove()

    def checkmove(self , x1 , y1):
        if ([y1,x1] in self.list):
            return 1
        else:
            return 0
    def ListOfmove(self):
        self.list=[]
        x=self.pos[1]
        y=self.pos[0]
        if (x+1 <8):
            if (board[y][x+1].color != self.color):
                self.list.append([y,x+1])
        if (y+1 <8):
            if (board[y+1][x].color != self.color):
                self.list.append([y+1,x])
        if (x-1 >=0):
            if (board[y][x-1].color != self.color):
                self.list.append([y,x-1])
        if (y-1 >=0):
            if (board[y-1][x].color != self.color):
                self.list.append([y-1,x])
        if (x+1 <8 and y+1 <8):
            if (board[y+1][x+1].color != self.color):
                self.list.append([y+1,x+1])
        if (x+1 <8 and y-1 >=0):
            if (board[y-1][x+1].color != self.color):
                self.list.append([y-1,x+1])
        if (x-1 >=0 and y+1 <8):
            if (board[y+1][x-1].color != self.color):
                self.list.append([y+1,x-1])
        if (x-1 >=0 and y-1 >=0):
            if (board[y-1][x-1].color != self.color):
                self.list.append([y-1,x-1])


    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Queen(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="Q"
        if (color == -1):
            self.type="q"
        self.ListOfmove()

    def checkmove(self , x1 , y1):
        if ([y1,x1] in self.list):
            return 1
        else:
            return 0

    def ListOfmove(self):
        self.list=[]
        x=self.pos[1]
        y=self.pos[0]
        while (x+1 <8 and (board[y][x+1].color != self.color) ):
            x=x+1
            self.list.append([y,x])

        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and (board[y+1][x].color != self.color) ):
            y=y+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (x-1 >= 0 and (board[y][x-1].color != self.color) ):
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and (board[y-1][x].color != self.color) ):
            y=y-1
            self.list.append([y,x])


        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x+1 <8 and (board[y+1][x+1].color != self.color) ):
            y=y+1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x-1 >= 0 and (board[y+1][x-1].color != self.color) ):
            y=y+1
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x+1 <8 and (board[y-1][x+1].color != self.color) ):
            y=y-1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x-1 >= 0 and (board[y-1][x-1].color!= self.color) ):
            y=y-1
            x=x-1
            self.list.append([y,x])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Rook(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="R"
        if (color == -1):
            self.type="r"


    def checkmove(self , x1 , y1):
        if ([y1,x1] in self.list):
            return 1
        else:
            return 0
    def list(self):
        return self.list

    def ListOfmove(self):

        self.list=[]

        x=self.pos[1]
        y=self.pos[0]
        while (x+1 <8 and (board[y][x+1].color != self.color) ):
            x=x+1
            self.list.append([y,x])

        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and (board[y+1][x].color != self.color) ):
            y=y+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (x-1 >= 0 and (board[y][x-1].color != self.color) ):
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and (board[y-1][x].color != self.color) ):
            y=y-1
            self.list.append([y,x])

    def move(self , x1 , y1):


        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Bishop(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="B"
        if (color == -1):
            self.type="b"
        self.ListOfmove()

    def checkmove(self , x1 , y1):
        if ([y1,x1] in self.list):
            return 1
        else:
            return 0

    def ListOfmove(self):
        self.list=[]
        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x+1 <8 and (board[y+1][x+1].color != self.color) ):
            y=y+1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x-1 >= 0 and (board[y+1][x-1].color != self.color) ):
            y=y+1
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x+1 <8 and (board[y-1][x+1].color != self.color) ):
            y=y-1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x-1 >= 0 and (board[y-1][x-1].color!= self.color) ):
            y=y-1
            x=x-1
            self.list.append([y,x])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Knight(chesspiece):

    def __init__(self, pos, color):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="N"
        if (color == -1):
            self.type="n"
        self.ListOfmove()

    def checkmove(self , x1 , y1):
        if ([y1,x1] in self.list):
            return 1
        else:
            return 0

    def ListOfmove(self):
        self.list=[]
        x=self.pos[1]
        y=self.pos[0]
        if (x+2 < 8 and y+1 <8):
            if (board[y+1][x+1].color != self.color):
                self.list.append([y+1,x+2])
        if (x+1 < 8 and y+2 <8):
            if (board[y+2][x+1].color != self.color):
                self.list.append([y+2,x+1])
        if (x+2 < 8 and y-1 >=0):
            if (board[y-1][x+1].color != self.color):
                self.list.append([y-1,x+2])
        if (x+1 < 8 and y-2 >=0):
            if (board[y-2][x+1].color != self.color):
                self.list.append([y-2,x+1])

        if (x-2 >=0 and y+1 <8):
            if (board[y+1][x-2].color != self.color):
                self.list.append([y+1,x-2])
        if (x-1 >=0 and y+2 <8):
            if (board[y+2][x-1].color != self.color):
                self.list.append([y+2,x-1])
        if (x-2 >=0 and y-1 >=0):
            if (board[y-2][x-1].color != self.color):
                self.list.append([y-1,x-2])
        if (x-1 >=0 and y-2 >=0):
            if (board[y-2][x-1].color != self.color):
                self.list.append([y-2,x-1])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            board[self.pos[0]][self.pos[1]]=chesspiece(0,0)
            board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;



board = [[chesspiece(0,0)]*8 for i in range(8)]

Wking=King([7,4],1)
Bking=King([0,4],-1)

def initialiseboard():
    for i in range (8):
        board[1][i]=poun([1,i],-1)
    for i in range (8):
        board[6][i]=poun([6,i],1)
    board[0][0]=Rook([0,0],-1)
    board[0][1]=Knight([0,1],-1)
    board[0][2]=Bishop([0,2],-1)
    board[0][3]=Queen([0,3],-1)
    board[0][4]=Bking
    board[0][5]=Bishop([0,5],-1)
    board[0][6]=Knight([0,6],-1)
    board[0][7]=Rook([0,7],-1)

    board[7][0]=Rook([7,0],1)
    board[7][1]=Knight([7,1],1)
    board[7][2]=Bishop([7,2],1)
    board[7][3]=Queen([7,3],1)
    board[7][4]=Wking
    board[7][5]=Bishop([7,5],1)
    board[7][6]=Knight([7,6],1)
    board[7][7]=Rook([7,7],1)

def check():
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j].type != "0"):
                if (board[i][j].color == 1):
                    if (Bking.pos in board[i][j].list):
                        return 1
                if (board[i][j].color == -1):
                    if (Wking.pos in board[i][j].list):
                        return 1
                else: return 0


def updateMoves():
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j].type != "0"):
                board[i][j].ListOfmove()

def getAllList():

    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j].type != "0"):

                print(board[i][j].pos)

                print(board[i][j].list)



def printboard (board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            print (CRED+board[i][j].type+CEND, end = '')
        print()
def showBoard (board):
    newboard = board1.copy()
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j].type == "P"):
                newboard.paste(WP , (150+j*212, 170+i*212), WPA)
            if (board[i][j].type == "p"):
                newboard.paste(BP , (150+j*212, 170+i*212), BPA)
            if (board[i][j].type == "R"):
                newboard.paste(WR , (150+j*212, 170+i*212), WRA)
            if (board[i][j].type == "r"):
                newboard.paste(BR , (150+j*212, 170+i*212), BRA)
            if (board[i][j].type == "B"):
                newboard.paste(WB , (150+j*212, 170+i*212), WBA)
            if (board[i][j].type == "b"):
                newboard.paste(BB , (150+j*212, 170+i*212), BBA)
            if (board[i][j].type == "N"):
                newboard.paste(WN , (150+j*212, 170+i*212), WNA)
            if (board[i][j].type == "n"):
                newboard.paste(BN , (150+j*212, 170+i*212), BNA)
            if (board[i][j].type == "Q"):
                newboard.paste(WQ , (150+j*212, 170+i*212), WQA)
            if (board[i][j].type == "q"):
                newboard.paste(BQ , (150+j*212, 170+i*212), BQA)
            if (board[i][j].type == "K"):
                newboard.paste(WK , (150+j*212, 170+i*212), WKA)
            if (board[i][j].type == "k"):
                newboard.paste(BK , (150+j*212, 170+i*212), BKA)
    newboard.show()



def printboardmoves(x,y):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (i == y and j == x):
                print (Cooo+board[i][j].type+CEND, end = '')
            elif ([i,j] in board[y][x].list):
                print (Cother+board[i][j].type+CEND, end = '')
            else :
                print (CRED+board[i][j].type+CEND, end = '')

        print()
initialiseboard()

number = ["0","1","2","3","4","5","6","7"]
letter = ["a","b","c","d","e","f","g","h","A","B","C","D","E","F","G","H"]
r = re.compile('@chess .{2} .{2}')
turn =0
turntable=[1,-1]
while(True):
    print("updated")
    updateMoves()



    if (turn ==0):
        print("WHITE'S TURN")
    if (turn ==1):
        print("BLACK'S TURN")
    if (turn ==2):
        print("CHECKMATE")
    printboard(board)
    print("----------------")
    printboardmoves(2,6)
    showBoard(board)
    print("----------------")


    incheck=0
    x0=0
    y0=0
    x1=0
    y1=0
    a = input()
    if len(a) == 12:
        if r.match(a) is not None:
            if (a[8] in number and a[11] in number and a[7] in letter and a[10] in letter):
                x0=ord(a[7].lower()) -97
                x1=ord(a[10].lower()) -97
                y0=int(a[8])
                y1=int(a[11])

                if (board[y0][x0].type != "0" and board[y0][x0].color==turntable[turn]):
                    if ((board[y0][x0].move(x1,y1))==1):
                        if (incheck ==1):
                            lastboard = board.copy()
                            updateMoves()
                            incheck = check()
                            if (incheck ==1):
                                board = lastboard
                                print("not a valid move , you are in check")
                            else :
                                turn = (turn+1)%2

                        turn = (turn+1)%2
                        updateMoves()
                        incheck = check()
                        if (incheck == 1):
                            print("you are checked")
                    else :print("not a valid move")
                else:print("not a valid move")
            else :print("error in syntax")
        else :print("error in syntax")
    else:print("error in syntax")
    
