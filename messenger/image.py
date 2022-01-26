from PIL import Image

board = Image.open("pieces/Chess-board-with-letters_nevit_111.svg.png")

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

newboard = board.copy()
for i in range (8):
    for j in range (8):
        newboard.paste(BB , (150+i*212, 170+j*212), BB.convert('RGBA'))

newboard.show()
