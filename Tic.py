import pygame

pygame.init()

ww = 600
wh = 600
win = pygame.display.set_mode((ww , wh))
pygame.display.set_caption("Tic Tac Toe")

bg = pygame.image.load('pngkey.com-tic-tac-toe-board-4082814.png')
cross = pygame.image.load('cross.png')
circle = pygame.image.load('circle.png')
u=0
image = cross
donelist = []
square = 0
square_record = []

points = dict({ 1: (65,65) , 2:(255,65) , 3: (450, 65) , 4 : (65,255), 5: (255 , 255),\
                6 : (450, 255) , 7:(65 , 450), 8 : (255 , 450), 9: (450,450) })

green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('Player 1 wins', True, green, blue)
text2 = font.render('Player 2 wins', True, green, blue)
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (300,300)
textRect2.center = (300,300)
recording = []

for i in range(9):
    recording.append(-1)



def champ():
    global recording
    if recording[0] == recording[1] == recording[2] :
        return recording[0]
    elif recording[3] == recording[4] == recording[5] :
        return recording[3]
    elif recording[6] == recording[7] == recording[8] :
        return recording[6]
    elif recording[0] == recording[3] == recording[6] :
        return recording[0]
    elif recording[1] == recording[4] == recording[7] :
        return recording[1]
    elif recording[2] == recording[5] == recording[8]:
        return recording[2]
    elif recording[0] == recording[4] == recording[8]:
        return recording[0]
    elif recording[2] == recording[4] == recording[6]:
        return recording[2]



def isodd(x):
    if x%2 == 0 :
        return False
    else :
        return True

def assign(x,y):
    global recording
    recording[x] = y

def clicked(x, y):
    row = (y + 200)//200
    coloumn = (x + 200)//200
    square = coloumn + (row - 1)*3
    return square
def count():
    global u
    u = u + 1
    yield u


def player_record():
    global u
    global image
    global square
    global recording
    if isodd(u):
        image = cross
        hii = square - 1
        recording[hii] = 1

    else :
        image = circle
        recording[square - 1] = 2


def gamewindow():
    global donelist
    global square
    win.blit(bg,(0,0))
    for i in donelist:
        win.blit(i[0],points[i[1]])
    pygame.display.update()

def winner_rec():
    global p1
    global p2


player_won = -1
run = True
while run :
    pygame.time.delay(100)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            square = clicked(x,y)
            if square in square_record:
                pass
            else :
                u = u + 1
                player_record()
                donelist.append((image,square))
                square_record.append(square)
                player_won = champ()
                if player_won == -1:
                    pass
                else:
                    if player_won == 1:
                        print("Player 1 wins")
                    else :
                        print("player 2 wins")

    if player_won == 1 or player_won == 2 :
        win.fill((255,255,255))
        if player_won == 1 :
            win.blit(text1, textRect1)
        elif player_won == 2 :
            win.blit(text2, textRect2)
        pygame.display.update()
    else :
        gamewindow()