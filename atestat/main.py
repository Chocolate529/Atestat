import pygame, sys, os, random
from button import Button


pygame.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Says")

MENU_BG = pygame.image.load("assets/Background6D.png")
PLAY_BG = pygame.image.load("assets/Background5D.png")
OPTIONS_BG = pygame.image.load("assets/Background7D.png")

DEFFAULT_DIFF = "Easy"
DIFFICULTY_COLOR = "Green"

#pozitii patratelee
pos = [(x, y) for x in range(1, 8) for y in range(1, 8)]

#patrateleee
class Square(pygame.sprite.Sprite):
    def __init__(self, number):
        
        super(Square, self).__init__()
        self.alpha = 255
        self.number = number
        self.make_image()
    
    def make_image(self):
        
        global font

        self.x, self.y = self.random_pos()
        self.image = pygame.Surface((73, 73),pygame.SRCALPHA)
        r, g, b = [random.randrange(128, 256) for x in range(3)]
        self.image.fill((r, g, b,self.alpha))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.number = str(self.number)
        self.text = font.render(self.number, 1, (0, 0, 0))
        text_rect = self.text.get_rect(center=(75 // 2, 75 // 2))
        self.image.blit(self.text, text_rect)

    def random_pos(self):
        
        global pos

        position = random.choice(pos)

        x, y = position
        
        del pos[pos.index(position)]
        x = 350 + x * 75 
        y = y * 75 
        return x, y


g = pygame.sprite.Group()
num_order = []

score = 0

#acoperis
bgd = pygame.Surface((100, 100),pygame.SRCALPHA)

def hide_cards():
    global pos

    for sprite in g:
        bgd.fill((0, 244, 0))
        sprite.image.blit(bgd, (0, 0))

    
    pos = [(x, y) for x in range(1, 8) for y in range(1, 8)]

def reset():
    global g,counter_on,counter
    counter = 0
    counter_on = 1
    for sprite in g:
        sprite.kill()


def mouse_collision(sprite):
    global num_order, score, maxscore
    global counter_on, max_count, cards_visible
    global bonus
    global DEFFAULT_DIFF

    def clear_screen():
        global num_order, counter_on, cards_visible
        num_order = []
        counter_on = 1
        cards_visible = 1

    x, y = pygame.mouse.get_pos()
    
    if sprite.rect.collidepoint(x, y):

        click.play()
        num_order.append(sprite.number)
        
        sprite.rect = pygame.Rect(-100, -100, 50, 50)
        
        if sprite.number != str(len(num_order)) and DEFFAULT_DIFF != "Easy":
            
            if DEFFAULT_DIFF == "Hard":
                reset()
                squares_init()
            clear_screen()
            score = score - 50
            
            [s.make_image() for s in g]
            SCREEN.fill((0,0,0))
            bgd.fill((255, 0, 0))
        
        else:
            
            if len(num_order) == len(g):
                score += 100 + bonus
                if score > int(maxscore):
                    maxscore = score
                    set_score(maxscore)
                
                g.add(Square(len(g) + 1))
                max_count = max_count + 10
                clear_screen()
                
                [s.make_image() for s in g]
                SCREEN.fill((0,0,0))
                bgd.fill((255, 0, 0))

                



######################
#    sunete        #
######################
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)
pygame.mixer.set_num_channels(32)

click = pygame.mixer.Sound("audio/click.wav")


def squares_init():
    for i in range(1, 4):
        g.add(Square(i))


counter = 0
counter_on = 1
max_count = 50
cards_visible = 1

#score
def get_maxscore() -> int:
    filename = "maxscore.txt"
    if filename in os.listdir():
        with open(filename, "r") as file:
            val = file.read()
            if val == "":
                maxscore = 0
            else:
                maxscore = int(val)
    else:
        maxscore = 0
    return maxscore


def set_score(maxscore) -> None:

    with open("maxscore.txt", "w") as file:
        file.write(str(maxscore))


maxscore = get_maxscore()

#font
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():
    global counter_on, counter, max_count, cards_visible
    global bonus, click, score,bgd
    global font
    global DEFFAULT_DIFF

    font = get_font(16)
    reset()
    squares_init()
    max_count = 50
    score = 0
    clock = pygame.time.Clock()
    while True:  
        
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(PLAY_BG,(0,0))

        text = font.render("Memory: " + str(score), 1, (255, 244, 0))
        record = font.render("Record: " + str(maxscore), 1, (255, 244, 0))
        SCREEN.blit(text, (0, 0))
        SCREEN.blit(record, (0, 100))

        if counter_on:
            if DEFFAULT_DIFF == "Easy":
                hide_cards()
            text = font.render("time: " + str(max_count - counter), 1, (255, 244, 0))
            SCREEN.blit(text, (0,200))
            if DEFFAULT_DIFF == "Easy":
                counter += 1
            elif DEFFAULT_DIFF == "Medium":
                counter += 2
            else:
                counter += 3
            if counter % 10 == 0:
                click.play()
        
           
 

        PLAY_RESTART = Button(image=None, pos=(440,630),
                            text_input="RESTART", font=get_font(75), base_color="Black", hovering_color="#a8ff75")

        PLAY_BACK = Button(image=None, pos=(940, 630), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="#a8ff75")

        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(425-75//2+1,75//2+1,525,525))

        for i in range(1,8):
            for j in range(1,8):
                pygame.draw.rect(SCREEN, (255,0,0), pygame.Rect(350+i*75-75//2+1,j*75-75//2,75,75),1)


        for BUTTON in [PLAY_RESTART, PLAY_BACK]:
            BUTTON.changeColor(PLAY_MOUSE_POS)
            BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    reset()
                    main_menu()
                if PLAY_RESTART.checkForInput(PLAY_MOUSE_POS):
                    reset()
                    play()
                if cards_visible:
                    
                    if DEFFAULT_DIFF == "Medium":
                        hide_cards()
                    else:
                         for sprite in g:
                            bgd.fill((0, 0, 0))
                            sprite.image.blit(bgd, (0, 0))
                    
                    bonus = max_count - counter
                    cards_visible = 0
                    counter_on = 0
                    counter = 0
                
                for s in g:
                    mouse_collision(s)  

        g.draw(SCREEN)
        
        
        if counter >= max_count:
            hide_cards()
            counter = 0
            counter_on = 0
            if DEFFAULT_DIFF != "Medium":
                for sprite in g:
                    bgd.fill((0, 0, 0))
                    sprite.image.blit(bgd, (0, 0))
 

        pygame.display.update()
        clock.tick(20)
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        global DEFFAULT_DIFF
        global DIFFICULTY_COLOR
        global max_count

        SCREEN.blit(OPTIONS_BG,(0,0))

        DIFFICULTY_TEXT = get_font(80).render("DIFFICULTY", True, "Black")
        DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(WIDTH/2, 100))


        OPTIONS_DIFF_EASY = Button(image=None, pos=(640, 250),
                                   text_input="EASY", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_DIFF_MEDIUM = Button(image=None, pos=(640, 350),
                                   text_input="MEDIUM", font=get_font(75), base_color="Black", hovering_color="#ffc800")
        OPTIONS_DIFF_HARD = Button(image=None, pos=(640, 450),
                                   text_input="HARD", font=get_font(75), base_color="Black", hovering_color="Red")

        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="#a8ff75")

        for BUTTON in [OPTIONS_DIFF_EASY, OPTIONS_DIFF_MEDIUM, OPTIONS_DIFF_HARD, OPTIONS_BACK]:
            BUTTON.changeColor(OPTIONS_MOUSE_POS)
            BUTTON.update(SCREEN)
        SCREEN.blit(DIFFICULTY_TEXT,DIFFICULTY_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_DIFF_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    DIFFICULTY_COLOR = "Green"
                    DEFFAULT_DIFF = "Easy"
                    
                    main_menu()
                if OPTIONS_DIFF_MEDIUM.checkForInput(OPTIONS_MOUSE_POS):
                    DIFFICULTY_COLOR = "#ffc800"
                    DEFFAULT_DIFF = "Medium"
                    
                    main_menu()   
                if OPTIONS_DIFF_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    DIFFICULTY_COLOR = "Red"
                    DEFFAULT_DIFF = "Hard"
                    
                    main_menu()
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(MENU_BG, (0, 0))

        global DEFFAULT_DIFF
        global DIFFICULTY_COLOR

        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        MENU_DIFFICULTY_TEXT = get_font(45).render("DIFFICULTY:"+DEFFAULT_DIFF, True, DIFFICULTY_COLOR)
        MENU_DIFFICULTY_RECT = MENU_DIFFICULTY_TEXT.get_rect(center=(WIDTH/2, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#a8ff75")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="#a8ff75")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#a8ff75")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_DIFFICULTY_TEXT, MENU_DIFFICULTY_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
    