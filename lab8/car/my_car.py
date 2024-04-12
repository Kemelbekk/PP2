import pygame.key
import pygame


class MyCar:
    def __init__(self, position, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.game_status = 'game'

    def border(self):
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.left < 0:
            self.rect.left = 0

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.x -= 4
        elif key[pygame.K_DOWN]:
            self.rect.x += 4
        self.border()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def border(self):
        if self.rect.right>500:
            self.rect.right=500
        if self.rect.left<0:
            self.rect.left = 0
        
    
    def move(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x-=4
        if key[pygame.K_RIGHT]:
            self.rect.x+=4
        self.border()
        

    def crash(self, sound, traffic_cars):
        for car in traffic_cars:
            if car.rect.colliderect(self.rect):
                print('Game over')
                sound.play()
                self.game_status = 'game_over'
