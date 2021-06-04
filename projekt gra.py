
import pygame
import random
pygame.init()
random.seed()

#stworzenie ekranu
screen = pygame.display.set_mode([800, 600]) #(szerokość, wysokość)
screen_width = 800
screen_height = 600

#ikona i nazwa gry
pygame.display.set_caption("Poisk")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

#tło gry
background_image = pygame.image.load("assets/background.png").convert()

#gracz
player_img = pygame.image.load("assets/kitty.png")
player_width = 64
player_height = 64

playerX = screen_width/2 - player_width/2
playerY = screen_height - 120
speedX = 0
speedY = 0

#laser
laser_sound = pygame.mixer.Sound('assets/lazer7.wav')

#alien
alien_width = 64
alien_height = 64


playerX = screen_width/2 - player_width/2
playerY = screen_height - 120
speedX = 0
speedY = 0


def player(x, y):
    screen.blit(player_img, (x, y))
    
    all_aliens = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

class AlienEnemy(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.direction = random.randint(-1, 1) / 10 + 0.2

    def update(self):
        if self.direction > 0 and self.x > screen_width:
            self.direction = -0.1
        elif self.direction < 0 and self.x < 0:
            self.direction = 0.1
        self.x = self.x + self.direction
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.y = self.y - 0.2
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        if self.y < 0:
            all_bullets.remove(self)




running = True
while running:
    screen.blit(background_image, [0, 0])


    #działanie gry aż do zamknięcia okna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #poruszanie się po planszy strzałkami
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -0.1
            if event.key == pygame.K_RIGHT:
                speedX = 0.1
            if event.key == pygame.K_UP:
                speedY = -0.1
            if event.key == pygame.K_DOWN:
                speedY = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedY = 0



    #żeby gracz nie wychodził poza ekran:
    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width - player_width:
        playerX = screen_width - player_width

    #poruszanie się gracza, część właściwa:
    playerX += speedX
    playerY += speedY
    player(playerX, playerY)

    #odświeżanie ekranu
    pygame.display.update()
