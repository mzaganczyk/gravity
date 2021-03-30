import pygame
import sys
from colors import chooseColorPack, switchColor, chooseColor
from planet import Planet

planets = []
clock = pygame.time.Clock()
mouseClick = False
bgColor, colorPack = chooseColorPack()
txtColor = chooseColor(colorPack)
planetNum = 0


def initGame():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.Font('Roboto-Thin.ttf', 20)
    clock.tick(30)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    background = pygame.Surface(screen.get_size())
    background.fill(bgColor)
    while True:
        checkEvents(background)
        updateScreen(screen, background, myfont)
        if mouseClick:
            try:
                planets[-1].grow()
            except IndexError:
                pass


def checkEvents(background):
    global mouseClick, bgColor, colorPack, planetNum, txtColor
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_c:
                bgColor, colorPack, txtColor = switchColor(planets)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                planetNum += 1
                planets.append(Planet(x, y, background, colorPack, planetNum))
                mouseClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseClick = False
                planets[-1].adultPlanet = True
        if event.type == pygame.MOUSEMOTION and mouseClick:
            x, y = event.pos
            planets[-1].pos[0], planets[-1].pos[1] = x, y


def updateScreen(screen, background, font):
    global bgColor
    screen.blit(background, (0, 0))
    textSurface = font.render('Press C to change colors', True, txtColor)
    screen.blit(textSurface, (1600, 1000))
    pygame.display.update()
    background.fill(bgColor)
    gravity()
    for planet in planets:
        planet.update()
        planet.draw()
        if planet.outOfScreen():
            planets.remove(planet)


def gravity():
    for planetCurr in planets:
        for planet in planets:
            planetCurr.calcGravityForce(planet.number, planet.mass, planet.pos[0], planet.pos[1])
