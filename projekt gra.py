import pygame
import random
import os
pygame.init()
pygame.mixer.init()
random.seed()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'assets/ufo.png')

#stworzenie ekranu
screen = pygame.display.set_mode([800, 600]) #(szerokosc, wysokosc)
screen_width = 800
screen_height = 600

#ikona i nazwa gry
pygame.display.set_caption("The universe is an infinite computer!")
filename = os.path.join(dirname, 'assets/ufo.png')
icon = pygame.image.load(filename)
pygame.display.set_icon(icon)

#tlo gry
filename = os.path.join(dirname, 'assets/background.png')
background_image = pygame.image.load(filename).convert()

#gracz
filename = os.path.join(dirname, 'assets/kitty.png')
player_img = pygame.image.load(filename)
player_width = 64
player_height = 64

#laser
filename = os.path.join(dirname, 'assets/lazer7.wav')
laser_sound = pygame.mixer.Sound(filename)

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
        filename = os.path.join(dirname, 'assets/ufo.png')
        self.image = pygame.image.load(filename)
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
        filename = os.path.join(dirname, 'assets/bullet.png')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.y = self.y - 0.2
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        if self.y < 0:
            all_bullets.remove(self)

pygame.mixer.music.load("Soundtrack adekwatny do strzelanki.mp3")
pygame.mixer.music.play()

running = True
while running:


    #dzia??anie gry a?? do zamkni??cia okna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #poruszanie si?? po planszy strza??kami
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -0.1
            if event.key == pygame.K_RIGHT:
                speedX = 0.1
            if event.key == pygame.K_UP:
                speedY = -0.1
            if event.key == pygame.K_DOWN:
                speedY = 0.1
            if event.key == pygame.K_SPACE:
                all_bullets.add(Bullet(int(playerX+32), int(playerY)))
                laser_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedY = 0



    #??eby gracz nie wychodzi?? poza ekran:
    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width - player_width:
        playerX = screen_width - player_width

    #poruszanie si?? gracza, cz?????? w??a??ciwa:
    playerX += speedX
    playerY += speedY


    #spawnienie wrog??w
    if len(all_aliens) < 1:
        all_aliens.add(AlienEnemy(random.randint(0, screen_width), random.randint(50, screen_height/2)))

    all_aliens.update()
    all_bullets.update()
    for bullet in all_bullets:
        for hit_alien in pygame.sprite.spritecollide(bullet, all_aliens, True):
            all_aliens.remove(hit_alien)
            all_bullets.remove(bullet)
    #od??wie??anie ekranu
    screen.blit(background_image, [0, 0])
    player(playerX, playerY)
    all_aliens.draw(screen)
    all_bullets.draw(screen)
    pygame.display.update()

pygame.mixer.quit()
pygame.quit()
quit()
