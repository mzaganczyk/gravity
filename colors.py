import random

# First color in each list is the background color
colors = [
    [(230, 222, 211), (135, 186, 179), (219, 100, 68), (76, 40, 44), (247, 165, 39)],
    [(232, 213, 185), (252, 58, 81), (245, 179, 73), (14, 36, 48)],
    [(161, 219, 178), (254, 229, 173), (250, 202, 102), (247, 165, 65), (244, 93, 76)],
    [(193, 179, 152), (96, 89, 81), (97, 166, 171), (172, 206, 192)],
    [(238, 233, 229), (250, 211, 178), (255, 186, 127), (255, 156, 151)],
    [(28, 20, 13), (203, 232, 107), (242, 233, 225), (255, 255, 255)],
    [(92, 50, 62), (168, 39, 67), (225, 94, 50), (192, 210, 62), (229, 240, 76)],
    [(26, 8, 31), (77, 29, 77), (5, 103, 110), (72, 156, 121), (235, 194, 136)]
]


def chooseColorPack():
    pack = random.choice(colors)
    bgColor = pack[0]
    planetColors = pack[1:]
    return bgColor, planetColors


def switchColor(planets):
    bg, newColorPack = chooseColorPack()
    txtColor = random.choice(newColorPack)
    for planet in planets:
        planet.color = random.choice(newColorPack)
    return bg, newColorPack, txtColor


def chooseColor(colorPack):
    return random.choice(colorPack)
