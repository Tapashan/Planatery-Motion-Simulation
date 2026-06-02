import pygame
import random
from sys import exit
import math


earth_x = 600
earth_y = 200

moon_x = 884
moon_y = 200

earth_velocity = 0
moon_velocity = 0

G = 6.67 * 10**1 
mass_earth = 81.3
mass_moon = 1
r_earth = 3.67 *7
r_moon = 1 *7


pygame.init()

earth_pos = pygame.Vector2(earth_x, earth_y)
moon_pos = pygame.Vector2(moon_x, moon_y)

direction = moon_pos - earth_pos

m_velocity = math.sqrt((G * mass_earth) / pygame.Vector2.magnitude(earth_pos - moon_pos))
e_velocity = math.sqrt((G * mass_moon) / pygame.Vector2.magnitude(earth_pos - moon_pos))

earth_velocity = pygame.Vector2(0, 0)
moon_velocity = pygame.Vector2(1, 2)

earth_surf = pygame.Surface((r_earth * 2, r_earth * 2), pygame.SRCALPHA)
pygame.draw.circle(earth_surf,"Orange",(r_earth, r_earth), r_earth)
earth_rect = earth_surf.get_rect(center = earth_pos)

moon_surf = pygame.Surface((r_moon * 2, r_moon * 2), pygame.SRCALPHA)
pygame.draw.circle(moon_surf,"green",(r_moon, r_moon),r_moon)
moon_rect = moon_surf.get_rect(center = moon_pos)

trail_moon = []
trail_earth = []

screen_center = pygame.Vector2(1200/2, 700/2)

screen = pygame.display.set_mode((1200, 700))

stars_world = [pygame.Vector2(random.randint(-2000, 2000), random.randint(-2000, 2000)) for _ in range(5000)]




clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((30, 31, 32))

    earth_rect.center = earth_pos
    moon_rect.center = moon_pos

    screen_center = pygame.Vector2(1200//2, 700//2)
    camera_offset = screen_center - earth_pos


    direction = moon_pos - earth_pos
    direction_sq = direction.magnitude_squared()

    force_earth = (G * mass_earth * mass_moon) / direction_sq
    force_moon = -force_earth

    earth_acc = (force_earth/mass_earth) * direction.normalize()
    moon_acc = (force_moon/mass_moon) * direction.normalize()

    earth_velocity += earth_acc
    moon_velocity += moon_acc

    earth_pos += earth_velocity
    moon_pos += moon_velocity

    trail_moon.append(moon_pos.copy())

    
    for points in trail_moon:
        pygame.draw.circle(screen, "White", (int(points[0]), int(points[1])), 1)


    screen.blit(earth_surf, earth_rect)
    screen.blit(moon_surf, moon_rect)

    pygame.display.update()
    clock.tick(60)