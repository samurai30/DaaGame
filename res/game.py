import pygame

entity = ['goat', 'wolf', 'cabbage']


def eats(x, y):
    if x == 'goat' and y == 'cabbage':
        return True
    elif x == 'wolf' and y == 'goat':
        return True
    else:
        return False


def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True


def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True


def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state) == 'right' and
            state_of('goat', state) == 'right' and
            state_of('wolf', state) == 'right' and
            state_of('cabbage', state) == 'right')


initial_state = {'man': 'left'}
for e in entity:
    initial_state[e] = 'left'

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("MWGC")

goat = pygame.transform.scale(pygame.image.load('goat.png'), (70, 70))
wolf = pygame.transform.scale(pygame.image.load('wolf.png'), (100, 100))
carrot = pygame.transform.scale(pygame.image.load('carrot.png'), (120, 120))
boat = pygame.transform.scale(pygame.image.load('boat.png'), (200, 200))
bg = pygame.image.load('BgDaa.jpg')
man = pygame.transform.scale(pygame.image.load('standing.png'), (100, 100))
gameover = pygame.image.load('gameover.png')
close = pygame.image.load('close.png')
replay = pygame.image.load('replay.png')

gx = 100
gy = 800

wx = 20
wy = 790

cx = 135
cy = 780

bx = 300
by = 850

mx = 190
my = 790

circleX = 50
circleY = 100

# variables

whos = list()

global whosize
whosize = 2

Flip = False

MoveItemGoat = False
MoveItemWolf = False
MoveItemMan = False
MoveItemCarrot = False
Move = False

nextID = initial_state.copy()
STATE = 'MAIN'


def renderGame():
    global STATE
    global whos
    win.blit(bg, (0, 0))
    win.blit(goat, (gx, gy))
    win.blit(wolf, (wx, wy))
    win.blit(carrot, (cx, cy))
    win.blit(man, (mx, my))
    pygame.draw.circle(win, (255, 255, 0), (circleX, circleY), 50)

    global nextID
    global Move

    if nextID and not goal_reach(nextID):
        if safe_state(nextID):
            if Move:
                for who in whos:
                    move(who, nextID)
                    print("moving :", who, "\n")

                Move = False
                whos.clear()
        else:
            nextID = initial_state.copy()
            whos.clear()
            STATE = 'GAMEOVER'

    else:
        print("passed")
    if Flip:
        win.blit(pygame.transform.flip(boat, True, False), (bx, by))
    else:
        win.blit(boat, (bx, by))

    pygame.display.update()


closeX = 250
closeY = 550

replayX = 750
replayY = 550

restart = False


def gameOver():
    global STATE
    global restart
    win.blit(bg, (0, 0))
    win.blit(gameover, (200, 400))
    win.blit(close, (closeX, closeY))
    win.blit(replay, (replayX, replayY))
    pygame.display.update()

    if restart:
        STATE = 'MAIN'
        restart = False


run = True

while run:
    clock.tick(15)

    if STATE == 'MAIN':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()

                    if gx + 70 > mouse[0] > gx and gy + 70 > mouse[1] > gy:
                        if len(whos) < int(whosize):
                            if not ('goat' in whos):
                                if gx < bx:
                                    countX = bx - gx
                                    countY = by - gy
                                    print(countX)
                                    for i in range(countX):
                                        if gx <= bx:
                                            gx += 2
                                            for y in range(countY):
                                                if gy < by:
                                                    gy += 2

                                print("goat")
                                whos.append('goat')

                    elif wx + 100 > mouse[0] > wx and wy + 100 > mouse[1] > wy:
                        if len(whos) < int(whosize):
                            if not ('wolf' in whos):
                                print("wolf")
                                whos.append('wolf')

                    elif mx + 100 > mouse[0] > mx and wy + 100 > mouse[1] > my:
                        if len(whos) < int(whosize):
                            if not ('man' in whos):
                                print("man")
                                whos.append('man')

                    elif cx + 120 > mouse[0] > cx and cy + 120 > mouse[1] > cy:
                        if len(whos) < int(whosize):
                            if not ('cabbage' in whos):
                                print("cabbage")
                                whos.append('cabbage')

                    elif circleX + 100 > mouse[0] > circleX and circleY + 100 > mouse[1] > circleY:
                        print("moving")
                        Move = True
        renderGame()

    elif STATE == 'GAMEOVER':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if replayX + 70 > mouse[0] > replayX and replayY + 70 > mouse[1] > replayY:
                        restart = True
        gameOver()

pygame.quit()
