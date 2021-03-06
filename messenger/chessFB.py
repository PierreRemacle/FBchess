import re
from PIL import Image

board1 = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/Chess-board-with-letters_nevit_111.svg.png")

BB = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/bb.png")
BK = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/bk.png")
BN = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/bn.png")
BP = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/bp.png")
BQ = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/bq.png")
BR = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/br.png")

WB = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wb.png")
WK = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wk.png")
WN = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wn.png")
WP = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wp.png")
WQ = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wq.png")
WR = Image.open("/Users/Pierre/Documents/DevFolder/messenger/pieces/wr.png")

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

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        self.type = "0"
        self.game = game
    def pos(self):
        return self.pos
    def color(self):
        return self.color
    def type(self):
        return self.type

class poun(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="P"
        if (color == -1):
            self.type="p"
        self.game = game
        self.ListOfmove()



    def checkmove(self , x1 , y1):


        if (self.color == 1):
            #print ("condition 1 = " + str(y1==self.pos[0]-1 and x1==self.pos[1] and board[y1][x1].type == "0"))
            #print ("condition 2 = " + str(((y1==self.pos[0]-1 and x1==self.pos[1]+1) or (y1==self.pos[0]-1 and x1==self.pos[1]-1)) and board[y1][x1].type != "0" and board[y1][x1].color == -1))
            if (y1==self.pos[0]-1 and x1==self.pos[1] and self.game.board[y1][x1].type == "0"):
                return 1
            elif(((y1==self.pos[0]-1 and x1==self.pos[1]+1) or (y1==self.pos[0]-1 and x1==self.pos[1]-1)) and self.game.board[y1][x1].type != "0" and self.game.board[y1][x1].color == -1 ):
                return 1
            elif(self.pos[0] == 6 and y1==self.pos[0]-2 and x1==self.pos[1] and self.game.board[y1][x1].type == "0"):
                return 1
        elif (self.color == -1):
            if (y1==self.pos[0]+1 and x1==self.pos[1] and self.game.board[y1][x1].type == "0"):
                return 1
            elif(((y1==self.pos[0]+1 and x1==self.pos[1]+1) or (y1==self.pos[0]+1 and x1==self.pos[1]-1)) and self.game.board[y1][x1].type != "0" and self.game.board[y1][x1].color == 1):
                return 1
            elif(self.pos[0] == 1 and y1==self.pos[0]+2 and x1==self.pos[1] and self.game.board[y1][x1].type == "0"):
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
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            if (self.color == -1 and self.pos[0] == 7):
                self.game.board[y1][x1]=Queen(x1,y1)
            if (self.color == 1 and self.pos[0] == 0):
                self.game.board[y1][x1]=Queen(x1,y1)
            else:
                self.game.board[y1][x1]=self
                self.pos=[y1,x1]
            self.ListOfmove()
            return 1;
        else :

            return 0;

class King(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="K"
        if (color == -1):
            self.type="k"
        self.game=game
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
            if (self.game.board[y][x+1].color != self.color):
                self.list.append([y,x+1])
        if (y+1 <8):
            if (self.game.board[y+1][x].color != self.color):
                self.list.append([y+1,x])
        if (x-1 >=0):
            if (self.game.board[y][x-1].color != self.color):
                self.list.append([y,x-1])
        if (y-1 >=0):
            if (self.game.board[y-1][x].color != self.color):
                self.list.append([y-1,x])
        if (x+1 <8 and y+1 <8):
            if (self.game.board[y+1][x+1].color != self.color):
                self.list.append([y+1,x+1])
        if (x+1 <8 and y-1 >=0):
            if (self.game.board[y-1][x+1].color != self.color):
                self.list.append([y-1,x+1])
        if (x-1 >=0 and y+1 <8):
            if (self.game.board[y+1][x-1].color != self.color):
                self.list.append([y+1,x-1])
        if (x-1 >=0 and y-1 >=0):
            if (self.game.board[y-1][x-1].color != self.color):
                self.list.append([y-1,x-1])


    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            self.game.board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Queen(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="Q"
        if (color == -1):
            self.type="q"
        self.game=game
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
        while (x+1 <8 and (self.game.board[y][x+1].color != self.color) ):
            x=x+1
            self.list.append([y,x])

        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and (self.game.board[y+1][x].color != self.color) ):
            y=y+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (x-1 >= 0 and (self.game.board[y][x-1].color != self.color) ):
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and (self.game.board[y-1][x].color != self.color) ):
            y=y-1
            self.list.append([y,x])


        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x+1 <8 and (self.game.board[y+1][x+1].color != self.color) ):
            y=y+1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x-1 >= 0 and (self.game.board[y+1][x-1].color != self.color) ):
            y=y+1
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x+1 <8 and (self.game.board[y-1][x+1].color != self.color) ):
            y=y-1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x-1 >= 0 and (self.game.board[y-1][x-1].color!= self.color) ):
            y=y-1
            x=x-1
            self.list.append([y,x])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            self.game.board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Rook(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="R"
        if (color == -1):
            self.type="r"
        self.game=game
        self.ListOfmove()


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
        while (x+1 <8 and (self.game.board[y][x+1].color != self.color) ):
            x=x+1
            self.list.append([y,x])

        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and (self.game.board[y+1][x].color != self.color) ):
            y=y+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (x-1 >= 0 and (self.game.board[y][x-1].color != self.color) ):
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and (self.game.board[y-1][x].color != self.color) ):
            y=y-1
            self.list.append([y,x])

    def move(self , x1 , y1):


        if self.checkmove(x1,y1)==1:
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            self.game.board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Bishop(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="B"
        if (color == -1):
            self.type="b"
        self.game=game
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
        while (y+1 <8 and x+1 <8 and (self.game.board[y+1][x+1].color != self.color) ):
            y=y+1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y+1 <8 and x-1 >= 0 and (self.game.board[y+1][x-1].color != self.color) ):
            y=y+1
            x=x-1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x+1 <8 and (self.game.board[y-1][x+1].color != self.color) ):
            y=y-1
            x=x+1
            self.list.append([y,x])
        x=self.pos[1]
        y=self.pos[0]
        while (y-1 >= 0 and x-1 >= 0 and (self.game.board[y-1][x-1].color!= self.color) ):
            y=y-1
            x=x-1
            self.list.append([y,x])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            self.game.board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;

class Knight(chesspiece):

    def __init__(self, pos, color,game):
        self.list=[]
        self.pos=pos
        self.color=color
        if (color == 1):
            self.type="N"
        if (color == -1):
            self.type="n"
        self.game=game
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
            if (self.game.board[y+1][x+1].color != self.color):
                self.list.append([y+1,x+2])
        if (x+1 < 8 and y+2 <8):
            if (self.game.board[y+2][x+1].color != self.color):
                self.list.append([y+2,x+1])
        if (x+2 < 8 and y-1 >=0):
            if (self.game.board[y-1][x+1].color != self.color):
                self.list.append([y-1,x+2])
        if (x+1 < 8 and y-2 >=0):
            if (self.game.board[y-2][x+1].color != self.color):
                self.list.append([y-2,x+1])

        if (x-2 >=0 and y+1 <8):
            if (self.game.board[y+1][x-2].color != self.color):
                self.list.append([y+1,x-2])
        if (x-1 >=0 and y+2 <8):
            if (self.game.board[y+2][x-1].color != self.color):
                self.list.append([y+2,x-1])
        if (x-2 >=0 and y-1 >=0):
            if (self.game.board[y-2][x-1].color != self.color):
                self.list.append([y-1,x-2])
        if (x-1 >=0 and y-2 >=0):
            if (self.game.board[y-2][x-1].color != self.color):
                self.list.append([y-2,x-1])

    def move(self , x1 , y1):
        if self.checkmove(x1,y1)==1:
            self.game.board[self.pos[0]][self.pos[1]]=chesspiece(0,0,game)
            self.game.board[y1][x1]=self
            self.pos=[y1,x1]
            return 1;
        else :

            return 0;




class game:

    def __init__(self):
        self.number = ["1","2","3","4","5","6","7","8"]
        self.letter = ["a","b","c","d","e","f","g","h","A","B","C","D","E","F","G","H"]
        self.r = re.compile('@chess .{2} .{2}')
        self.turntable=[1,-1]
        self.turn=0
        self.board = [[chesspiece(0,0,self)]*8 for i in range(8)]
        self.Wking=King([7,4],1,self)
        self.Bking=King([0,4],-1,self)



    def nextMove(self,text):

        print("updated")
        self.updateMoves()


        if (self.turn ==0):
            print("WHITE'S TURN")
        if (self.turn ==1):
            print("BLACK'S TURN")
        if (self.turn ==2):
            print("CHECKMATE")



        incheck=0
        x0=0
        y0=0
        x1=0
        y1=0
        a = str(text)

        if a == "@chess newgame":
            self.initialiseboard()
            self.showBoard()
        elif len(a) == 12:
            if self.r.match(a) is not None:
                if (a[8] in self.number and a[11] in self.number and a[7] in self.letter and a[10] in self.letter):
                    x0=ord(a[7].lower()) -97
                    x1=ord(a[10].lower()) -97
                    y0=(-int(a[8]))%8
                    y1=(-int(a[11]))%8
                    print(y0)
                    print(y1)

                    if (self.board[y0][x0].type != "0" and self.board[y0][x0].color==self.turntable[self.turn]):
                        if ((self.board[y0][x0].move(x1,y1))==1):
                            if (incheck ==1):
                                lastboard = self.board.copy()
                                self.updateMoves()
                                incheck = self.check()
                                if (incheck ==1):
                                    self.board = lastboard
                                    print("not a valid move , you are in check")
                                else :
                                    self.turn = (self.turn+1)%2

                            self.turn = (self.turn+1)%2
                            self.updateMoves()
                            incheck = self.check()
                            if (incheck == 1):
                                print("you are checked")
                        else :print("not a valid move")
                    else:print("not a valid move")
                else :print("error in syntax")
            else :print("error in syntax")
        else:print("error in syntax")
        self.printboard()
        print("----------------")
        self.printboardmoves(1,0)
        print("----------------")
        self.showBoard()


    def initialiseboard(self):
        self.board =[[chesspiece(0,0,self)]*8 for i in range(8)]
        for i in range (8):
            self.board[1][i]=poun([1,i],-1,self)
        for i in range (8):
            self.board[6][i]=poun([6,i],1,self)
        self.board[0][0]=Rook([0,0],-1,self)
        self.board[0][1]=Knight([0,1],-1,self)
        self.board[0][2]=Bishop([0,2],-1,self)
        self.board[0][3]=Queen([0,3],-1,self)
        self.board[0][4]=self.Bking
        self.board[0][5]=Bishop([0,5],-1,self)
        self.board[0][6]=Knight([0,6],-1,self)
        self.board[0][7]=Rook([0,7],-1,self)

        self.board[7][0]=Rook([7,0],1,self)
        self.board[7][1]=Knight([7,1],1,self)
        self.board[7][2]=Bishop([7,2],1,self)
        self.board[7][3]=Queen([7,3],1,self)
        self.board[7][4]=self.Wking
        self.board[7][5]=Bishop([7,5],1,self)
        self.board[7][6]=Knight([7,6],1,self)
        self.board[7][7]=Rook([7,7],1,self)

    def check(self):
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if (self.board[i][j].type != "0"):
                    if (self.board[i][j].color == 1):
                        if (self.Bking.pos in self.board[i][j].list):
                            return 1
                    if (self.board[i][j].color == -1):
                        if (self.Wking.pos in self.board[i][j].list):
                            return 1
                    else: return 0


    def updateMoves(self):
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if (self.board[i][j].type != "0"):
                    self.board[i][j].ListOfmove()

    def getAllList(self):

        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if (self.board[i][j].type != "0"):

                    print(self.board[i][j].pos)

                    print(self.board[i][j].list)



    def printboard (self):
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                print (CRED+self.board[i][j].type+CEND)
            print()

    newboard=board1.copy()

    def showBoard (self):
        newboard = board1.copy()
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if (self.board[i][j].type == "P"):
                    newboard.paste(WP , (150+j*212, 170+i*212), WPA)
                if (self.board[i][j].type == "p"):
                    newboard.paste(BP , (150+j*212, 170+i*212), BPA)
                if (self.board[i][j].type == "R"):
                    newboard.paste(WR , (150+j*212, 170+i*212), WRA)
                if (self.board[i][j].type == "r"):
                    newboard.paste(BR , (150+j*212, 170+i*212), BRA)
                if (self.board[i][j].type == "B"):
                    newboard.paste(WB , (150+j*212, 170+i*212), WBA)
                if (self.board[i][j].type == "b"):
                    newboard.paste(BB , (150+j*212, 170+i*212), BBA)
                if (self.board[i][j].type == "N"):
                    newboard.paste(WN , (150+j*212, 170+i*212), WNA)
                if (self.board[i][j].type == "n"):
                    newboard.paste(BN , (150+j*212, 170+i*212), BNA)
                if (self.board[i][j].type == "Q"):
                    newboard.paste(WQ , (150+j*212, 170+i*212), WQA)
                if (self.board[i][j].type == "q"):
                    newboard.paste(BQ , (150+j*212, 170+i*212), BQA)
                if (self.board[i][j].type == "K"):
                    newboard.paste(WK , (150+j*212, 170+i*212), WKA)
                if (self.board[i][j].type == "k"):
                    newboard.paste(BK , (150+j*212, 170+i*212), BKA)
        newboard.save("newboard.png")



    def printboardmoves(self,x,y):
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if (i == y and j == x):
                    print (Cooo+self.board[i][j].type+CEND)
                elif ([i,j] in self.board[y][x].list):
                    print (Cother+self.board[i][j].type+CEND)
                else :
                    print (CRED+self.board[i][j].type+CEND)

            print()


import fbchat
from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):

    def onMessage(self, author_id, message_object, thread_id=id, thread_type=2, **kwargs):
                log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))


                if "@chess" in message_object.text:
                    if (str(thread_id) not in id):
                        id.append(str(thread_id))
                        games.append(game())

                    print(id)
                    print("message")
                    print(message_object.text)
                    index =id.index(str(thread_id))
                    currentgame = games[index]
                    currentgame.nextMove(str(message_object.text))
                    self.sendLocalFiles("newboard.png", thread_id=thread_id, thread_type=thread_type)


games=[]
id=[]
client = EchoBot(email, MDP)
client.listen()
