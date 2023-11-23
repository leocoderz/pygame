import pygame
import sys

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Scenario:
    def __init__(self):
        self.palm_tree = pygame.image.load('D:\CAIR\—Pngtree—palm tree 5-real png_5670308.png')
        self.tractor = pygame.image.load('D:\CAIR\—Pngtree—palm tree 5-real png_5670308.png')
        self.house = pygame.image.load('D:\CAIR\—Pngtree—palm tree 5-real png_5670308.png')
        self.person = pygame.image.load('D:\CAIR\—Pngtree—palm tree 5-real png_5670308.png')


        self.house_rect = self.house.get_rect()
        self.house_rect.center = (width // 2, height - 50)

        self.motor_rect = pygame.Rect(0, 0, 20, 20)  # Example motor (rectangle)
        self.motor_rect.center = (width // 2, height - 50)

        self.person_rect = self.person.get_rect()
        self.person_rect.center = (width // 2, height - 100)

        self.watering = False

    def draw(self):
        screen.blit(self.palm_tree, (50, 50))
        screen.blit(self.tractor, (width - 150, height - 100))
        screen.blit(self.house, self.house_rect)
        screen.blit(self.person, self.person_rect)
        pygame.draw.rect(screen, (0, 255, 0), self.motor_rect)  # Green motor

scenario = Scenario()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scenario.watering = not scenario.watering

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        scenario.person_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        scenario.person_rect.x += 5

    # Watering animation logic
    if scenario.watering:
        scenario.motor_rect.y -= 5
        if scenario.motor_rect.y < 0:
            scenario.watering = False
            scenario.motor_rect.y = 0

    screen.fill((255, 255, 255))  # White background
    scenario.draw()

    pygame.display.flip()
    clock.tick(60)
