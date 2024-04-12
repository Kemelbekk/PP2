import random
import pygame
import pygame.freetype
from my_car import MyCar
from roads import Road

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('Traffic racer')
background_color = (0, 0, 0)

font = pygame.freetype.Font(None, 20)

road_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()  # Group for coins
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

my_car_image = get_car_image('images/mercedes.png', (100, 70), -90)
road_image = pygame.image.load('images/road.png')
road_image = pygame.transform.scale(road_image, (500, 800))
coin_image = pygame.image.load('images/coins.png')
coin_image = pygame.transform.scale(coin_image, (30, 30))

def spawn_road():
    road_bg = Road(road_image, (250, -600))
    road_group.add(road_bg)

    # Randomly spawn coins
    if random.random() < 0.5:  # Adjust the probability as needed
        coin = Coin(coin_image, (random.randint(50, 450), -30))
        coin_group.add(coin)

def draw_all(score):
    road_group.update()
    road_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    my_car.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text[0], (350, 20))

    # Display number of collected coins
    coins_collected_text = font.render(f"Coins: {len(coin_group.sprites())}", True, (255, 255, 255))
    screen.blit(coins_collected_text[0], (350, 50))

my_car = MyCar((300, 600), my_car_image)

# Update method for Road class to move the road
class Road(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()  # Remove the road when it goes off-screen

# Coin class for the coins
class Coin(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()  # Remove the coin when it goes off-screen

# Initialize score
score = 0

# Function to check collisions with coins
def check_collisions():
    global score
    for coin in coin_group:
        if pygame.sprite.collide_rect(my_car, coin):
            coin.kill()
            score += 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()

    screen.fill(background_color)
    my_car.move()
    draw_all(score)
    check_collisions()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()