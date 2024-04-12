#Imports
import pygame, sys
from pygame.locals import * # для того чтобы создавать переменные без длинного префикса 
import random, time

#Инициализация
pygame.init()

#Настройка кадров в секунду
FPS = 60
FramePerSec = pygame.time.Clock()

#Создание цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
POINT = 0
#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")  #загружаем фон

#Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite): #Simple base class for visible game objects.
    def __init__(self):
        super().__init__() #вызывает sprite (parent class of enemy)
        self.image = pygame.image.load(r"Enemy.png")
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #центрирует объект в рандомной координате 

    def move(self):
        global SCORE #global позволяет изменять переменную за пределами текущей области видимости
        self.rect.move_ip(0, SPEED) #Rect.move_ip(x, y) – меняет координаты текущего прямоугольника со смещениями x, y
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Monet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Monet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global POINT
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def reset(self): # reset the position of the sprite to the top of the screen with a new random x-coordinate.
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) #move in-place
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0) #Rect.move_ip(x, y)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Monet()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(M1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    points = font_small.render(str(POINT), True, RED)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(points, (380,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r"crash.wav").play()
          time.sleep(1) #pause gives the player a moment to react to the collision before the game continues.
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() #clears the screen
          time.sleep(2) #after 2 second closes the game
          pygame.quit()
          sys.exit()  

    if pygame.sprite.spritecollideany(E1, coins) :
        all_sprites.sprites()[2].reset()
        
    if pygame.sprite.spritecollideany(P1, coins) : 
        
            all_sprites.sprites()[2].reset()
            POINT+=1

    pygame.display.update()
    FramePerSec.tick(FPS)