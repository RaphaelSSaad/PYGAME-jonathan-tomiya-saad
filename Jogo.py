import pygame, random
pygame.init()

width = 700
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Planet Pong')

width_planets = 25
height_planets = 25
branco = pygame.Color('grey100')
#Imagens-----------------------------------------------------------
terra_img = pygame.image.load('Terran.png').convert_alpha()
terra_img = pygame.transform.scale(terra_img, (width_planets, height_planets))
lava_img = pygame.image.load('Lava.png').convert_alpha()
lava_img = pygame.transform.scale(lava_img,(width_planets, height_planets))
Ice_img = pygame.image.load('Ice.png')
Ice_img = pygame.transform.scale(Ice_img, (width_planets, height_planets))
black_hole_img = pygame.image.load('Black_hole.png').convert_alpha()
black_hole_img = pygame.transform.scale(black_hole_img, (width_planets, height_planets))
baren_img = pygame.image.load('Baren.png')
baren_img = pygame.transform.scale(baren_img, (width_planets, height_planets))
background_img = pygame.image.load('Space Background.png').convert()
background_img = pygame.transform.scale(background_img, (width, height))
#------------------------------------------------------------------------
# player1 = pygame.Rect(width-10, height/2-40,20,80)
# player2 = pygame.Rect(-10, height/2-40,20,80)
player1_speed = 0
player2_speed = 0
player1_score = 0
player2_score = 0
game_font =pygame.font.Font("freesansbold.ttf", 40)
#---------------------------------------------------------------

#Classe Planetas--------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x-10, y/2-40, 20, 80)
        self.rect.x = (x)
        self.rect.y = (height / 2) - 12.5
        
class Planetas(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (width / 2) - 12.5
        self.rect.y = (height / 2) - 12.5
        self.speedx = 2 * random.choice((1, -1))
        self.speedy = 2 * random.choice((1, -1))
        self.ultima_atualizacao = 0

    def update(self, player1, player2):
        global player2_score, player1_score
        agora = pygame.time.get_ticks()
        if agora - self.ultima_atualizacao >3000:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        if pygame.sprite.collide_rect(self, player1) or pygame.sprite.collide_rect(self, player2):
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speedy *= -1
        if self.rect.right >= width:
            player2_score += 1
            self.rect.x = width/2 - 12.5
            self.rect.y = height/2 -12.5
            self.speedx =  2 * random.choice((1, -1))
            self.ultima_atualizacao = pygame.time.get_ticks()
        if self.rect.left <= 0:
            player1_score += 1
            self.rect.x = width/2 - 12.5
            self.rect.y = height/2- 12.5
            self.speedx =  2 * random.choice((1, -1))
            self.ultima_atualizacao = pygame.time.get_ticks()
            
        
       
#---------------------------------------------------------

#Planetas-----------------------------------------------------------
terra = Planetas(terra_img)
lava = Planetas(lava_img)
gelo = Planetas(Ice_img)
black_hole = Planetas(black_hole_img)
baren = Planetas(baren_img)
planetas_lista = [terra, lava, gelo, black_hole, baren, ]
escolhido = random.choice(planetas_lista)
#----------------------------------------------------------------------
player1 = Player(width-10, height)
player2 = Player(0-10, height)

game = True
clock = pygame.time.Clock()
FPS = 50
PLUS_DIF = 20e3
n = 1

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 4
            if event.key == pygame.K_UP:
                player1_speed -= 4
            if event.key == pygame.K_w:
                player2_speed -= 4
            if event.key == pygame.K_s:
                player2_speed += 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 4
            if event.key == pygame.K_UP:
                player1_speed += 4
            if event.key == pygame.K_w:
                player2_speed += 4
            if event.key == pygame.K_s:
                player2_speed -= 4
    if player1.rect.top <= 0:
        player1.rect.top = 0
    if player1.rect.bottom >= height:
        player1.rect.bottom = height
    if player2.rect.top <= 0:
        player2.rect.top = 0
    if player2.rect.bottom >= height:
        player2.rect.bottom = height
    if pygame.time.get_ticks() > n * PLUS_DIF:
        if escolhido.speedx < 0:
            escolhido.speedx -= 2 
        elif escolhido.speedx < 0:
            escolhido.speedx += 2
        n += 1
    
    player1.rect.y += player1_speed
    player2.rect.y += player2_speed
    player1_text = game_font.render(f'{player1_score}', False,branco)
    player2_text = game_font.render(f'{player2_score}', False,branco)
    escolhido.update(player1, player2)
    window.fill((255,255,255))
    window.blit(background_img, (0,0))
    pygame.draw.rect(window,branco,player1)
    pygame.draw.rect(window,branco, player2)
    pygame.draw.aaline(window,branco, (width/2,0), (width/2, height))
    window.blit(player1_text, (500, 10))
    window.blit(player2_text, (height/2, 10))
    window.blit(escolhido.image, escolhido.rect)

    pygame.display.update()

pygame.quit()