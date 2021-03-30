import pygame
import random
import math

class Planet:
    def __init__(self, x, y, surface, colors, number):
        self.pos = [x, y]
        self.radius = 5
        self.surface = surface
        self.color = random.choice(colors)
        self.mass = 4 / 3 * math.pi * self.radius ** 3 * 6 * 10 ** 9
        self.number = number
        self.speed = [0, 0]
        self.adultPlanet = False

    def grow(self):
        if self.radius <= 150:
            self.radius += 0.1

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def calcGravityForce(self, number, mass, x, y):
        if self.adultPlanet:
            G = 6.6743 * 0.1 ** 11
            if number != self.number:
                distance, dx, dy = self.calcDistance(x, y)
                angle = math.atan2(dy, dx)
                force = (G * self.mass * mass) / (distance ** 2)
                acceleration = (force / mass) / 10
                self.speed[0] += acceleration * math.cos(angle)
                self.speed[1] += acceleration * math.sin(angle)

    def outOfScreen(self):
        return self.pos[0] > 1920 or self.pos[0] < 0 or self.pos[1] > 1080 or self.pos[1] < 0

    def calcDistance(self, x, y):
        dx = x - self.pos[0]
        dy = y - self.pos[1]
        dist = math.sqrt(dx**2+dy**2)
        if dist < 2*self.radius:
            return 2*self.radius, dx, dy
        else:
            return dist, dx, dy

    def getInitialSpeed(self):
        pass

    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
