import pygame, sys
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

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(PLAY_BG,(0,0))

        PLAY_RESTART = Button(image=None, pos=(440,600),
                            text_input="RESTART", font=get_font(75), base_color="Black", hovering_color="#a8ff75")

        PLAY_BACK = Button(image=None, pos=(940, 600), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="#a8ff75")

        for BUTTON in [PLAY_RESTART, PLAY_BACK]:
            BUTTON.changeColor(PLAY_MOUSE_POS)
            BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        global DEFFAULT_DIFF
        global DIFFICULTY_COLOR

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
    