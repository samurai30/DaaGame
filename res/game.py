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

win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("MWGC")

goat = pygame.transform.scale(pygame.image.load('goat.png'), (70, 70))
wolf = pygame.transform.scale(pygame.image.load('wolf.png'), (100, 100))
carrot = pygame.transform.scale(pygame.image.load('carrot.png'), (120, 120))
boat = pygame.transform.scale(pygame.image.load('boat.png'), (200, 200))
bg = pygame.transform.scale(pygame.image.load('BgDaa.jpg'), (1000, 500))
man = pygame.transform.scale(pygame.image.load('standing.png'), (100, 100))
gameover = pygame.image.load('gameover.png')
gamewon = pygame.image.load('gamewon.png')
close = pygame.transform.scale(pygame.image.load('close.png'), (50, 50))
replay = pygame.transform.scale(pygame.image.load('replay.png'), (50, 50))

gx = 25
gy = 320

wx = 80
wy = 300

cx = 120
cy = 300

bx = 300
by = 350

mx = 200
my = 320

circleX = 50
circleY = 100


def defaultCord():
    global gx
    global gy
    global wx
    global wy
    global cx
    global cy
    global bx
    global by
    global mx
    global my
    global gx
    global gy
    global wx
    global wy
    gx = 25
    gy = 320
    wx = 80
    wy = 300
    cx = 120
    cy = 300
    bx = 300
    by = 350
    mx = 200
    my = 320


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
    global gx
    global gy
    global wx
    global wy
    global cx
    global cy
    global bx
    global by
    global mx
    global my
    global gx
    global gy
    global wx
    global wy

    win.blit(bg, (0, 0))
    win.blit(boat, (bx, by))
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
                if bx < 500:
                    if len(whos) == 1:
                        if 'man' in whos:
                            for i in range(0, 50):
                                bx += 5
                                mx += 5
                                pygame.display.update()
                            for m in range(0, 10):
                                mx += 10
                                my -= 3
                                pygame.display.update()
                    if 'goat' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx += 5
                            gx += 5
                            mx += 5
                            pygame.display.update()
                        for g in range(0, 10):
                            gx += 32
                            gy -= 6
                            mx += 10
                            my -= 3
                            pygame.display.update()
                    if 'wolf' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx += 5
                            wx += 5
                            mx += 5
                            pygame.display.update()
                        for w in range(0, 10):
                            wx += 20
                            wy -= 5
                            mx += 10
                            my -= 3
                            pygame.display.update()
                    if 'cabbage' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx += 5
                            cx += 5
                            mx += 5
                            pygame.display.update()
                        for g in range(0, 10):
                            cx += 25
                            cy -= 3
                            mx += 10
                            my -= 3
                            pygame.display.update()

                elif bx > 500:
                    if len(whos) == 1:
                        if 'man' in whos:
                            for i in range(0, 50):
                                bx -= 5
                                mx -= 5
                                pygame.display.update()
                            for m in range(0, 10):
                                mx -= 10
                                my -= 3
                                pygame.display.update()
                    if 'goat' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx -= 5
                            gx -= 5
                            mx -= 5
                            pygame.display.update()
                        for g in range(0, 10):
                            gx -= 32
                            gy -= 6
                            mx -= 10
                            my -= 3
                            pygame.display.update()
                    if 'wolf' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx -= 5
                            wx -= 5
                            mx -= 5
                            pygame.display.update()
                        for w in range(0, 10):
                            wx -= 29
                            wy -= 5
                            mx -= 10
                            my -= 3
                            pygame.display.update()
                    if 'cabbage' in whos and 'man' in whos:
                        for i in range(0, 50):
                            bx -= 5
                            cx -= 5
                            mx -= 5
                            pygame.display.update()
                        for g in range(0, 10):
                            cx -= 25
                            cy -= 3
                            mx -= 10
                            my -= 3
                            pygame.display.update()
                Move = False
                whos.clear()
        else:
            nextID = initial_state.copy()
            whos.clear()
            STATE = 'GAMEOVER'

    else:
        nextID = initial_state.copy()
        whos.clear()
        STATE = 'WON'

    pygame.display.update()


closeX = 300
closeY = 225

replayX = 650
replayY = 225

restart = False


def gameOver():
    global STATE
    global restart
    win.blit(bg, (0, 0))
    win.blit(gameover, (200, 100))
    win.blit(close, (closeX, closeY))
    win.blit(replay, (replayX, replayY))
    pygame.display.update()

    if restart:
        defaultCord()
        STATE = 'MAIN'
        restart = False


def gameWon():
    global STATE
    global restart
    win.blit(bg, (0, 0))
    win.blit(gamewon, (200, 100))
    win.blit(close, (closeX, closeY))
    win.blit(replay, (replayX, replayY))
    pygame.display.update()

    if restart:
        defaultCord()
        STATE = 'MAIN'
        restart = False


run = True

while run:
    clock.tick(30)

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
                                print("goat")
                                whos.append('goat')
                                print(whos)
                                if gx < 300:
                                    for i in range(0, 10):
                                        gx += 30
                                        gy += 6
                                        pygame.display.update()
                                elif gx > 600:
                                    for i in range(0, 10):
                                        gx -= 30
                                        gy += 6
                                        pygame.display.update()
                            elif 'goat' in whos:
                                whos.remove('goat')
                                print(whos)
                                if 400 > gx > 300:
                                    for i in range(0, 10):
                                        gx -= 30
                                        gy -= 6
                                        pygame.display.update()
                                elif 540 < gx < 600:
                                    for i in range(0, 10):
                                        gx += 30
                                        gy -= 6
                                        pygame.display.update()
                        elif 'goat' in whos:
                            whos.remove('goat')
                            if 400 > gx > 300:
                                for i in range(0, 10):
                                    gx -= 30
                                    gy -= 6
                                    pygame.display.update()
                            elif 540 < gx < 600:
                                for i in range(0, 10):
                                    gx += 30
                                    gy -= 6
                                    pygame.display.update()
                            print(whos)

                    elif wx + 100 > mouse[0] > wx and wy + 100 > mouse[1] > wy:
                        if len(whos) < int(whosize):
                            if not ('wolf' in whos):
                                print("wolf")
                                whos.append('wolf')
                                if wx < 300:
                                    for i in range(0, 10):
                                        wx += 29
                                        wy += 5
                                        pygame.display.update()
                                elif wx > 600:
                                    for i in range(0, 10):
                                        wx -= 20
                                        wy += 5
                                        pygame.display.update()
                                print(whos)
                            elif 'wolf' in whos:
                                whos.remove('wolf')
                                if 400 > wx > 300:
                                    for i in range(0, 10):
                                        wx -= 29
                                        wy -= 5
                                        pygame.display.update()
                                elif 500 < wx < 680:
                                    for i in range(0, 10):
                                        wx += 20
                                        wy -= 5
                                        pygame.display.update()
                                print(whos)
                        elif 'wolf' in whos:
                            whos.remove('wolf')
                            if 400 > wx > 300:
                                for i in range(0, 10):
                                    wx -= 29
                                    wy -= 5
                                    pygame.display.update()
                            elif 500 < wx < 680:
                                for i in range(0, 10):
                                    wx += 20
                                    wy -= 5
                                    pygame.display.update()
                            print(whos)

                    elif mx + 100 > mouse[0] > mx and wy + 100 > mouse[1] > my:
                        if len(whos) < int(whosize):
                            if not ('man' in whos):
                                print("man")
                                whos.append('man')
                                if mx < 300:
                                    for i in range(0, 10):
                                        mx += 20
                                        my += 3
                                        pygame.display.update()
                                elif mx > 600:
                                    for i in range(0, 10):
                                        mx -= 20
                                        my += 3
                                        pygame.display.update()
                            elif 'man' in whos:
                                whos.remove('man')
                                if 500 > mx > 300:
                                    for i in range(0, 10):
                                        mx -= 20
                                        my -= 3
                                        pygame.display.update()
                                elif 540 < mx < 600:
                                    for i in range(0, 10):
                                        mx += 20
                                        my -= 3
                                        pygame.display.update()
                                print(whos)
                        elif 'man' in whos:
                            whos.remove('man')
                            if 500 > mx > 300:
                                for i in range(0, 10):
                                    mx -= 20
                                    my -= 3
                                    pygame.display.update()
                            elif 540 < mx < 600:
                                for i in range(0, 10):
                                    mx += 20
                                    my -= 3
                                    pygame.display.update()
                            print(whos)
                    elif cx + 120 > mouse[0] > cx and cy + 120 > mouse[1] > cy:
                        if len(whos) < int(whosize):
                            if not ('cabbage' in whos):
                                print("cabbage")
                                whos.append('cabbage')
                                if cx < 300:
                                    for i in range(0, 10):
                                        cx += 20
                                        cy += 3
                                        pygame.display.update()
                                elif cx > 600:
                                    for i in range(0, 10):
                                        cx -= 20
                                        cy += 3
                                        pygame.display.update()
                            elif 'cabbage' in whos:
                                whos.remove('cabbage')
                                if 500 > cx > 300:
                                    for i in range(0, 10):
                                        cx -= 20
                                        cy -= 3
                                        pygame.display.update()
                                elif 500 < cx < 650:
                                    for i in range(0, 10):
                                        cx += 20
                                        cy -= 3
                                        pygame.display.update()
                                print(whos)
                        elif 'cabbage' in whos:
                            whos.remove('cabbage')
                            if 500 > cx > 300:
                                for i in range(0, 10):
                                    cx -= 20
                                    cy -= 3
                                    pygame.display.update()
                            elif 500 < cx < 650:
                                for i in range(0, 10):
                                    cx += 20
                                    cy -= 3
                                    pygame.display.update()
                            print(whos)

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
                    elif closeX + 70 > mouse[0] > closeX and closeY + 70 > mouse[1] > closeY:
                        run = False
                        exit(1)
        gameOver()
    elif STATE == 'WON':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if replayX + 70 > mouse[0] > replayX and replayY + 70 > mouse[1] > replayY:
                        restart = True
                    elif closeX + 70 > mouse[0] > closeX and closeY + 70 > mouse[1] > closeY:
                        run = False
                        exit(1)
        gameWon()

pygame.quit()
