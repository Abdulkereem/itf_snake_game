import pygame_menu
import pygame
# import os
# os.environ['SDL_VIDEODRIVER'] = 'dummy'
from utilities.state import *
import snake


pygame.init()


surface = pygame.display.set_mode((dis_width,dis_height),pygame.FULLSCREEN)



menu = pygame_menu.Menu("Join ITF Snake Team",400,300,
                                                theme=pygame_menu.themes.THEME_BLUE)


menu.add.label('Your fullname')
menu.add.text_input('',default='')


menu.add.label('Your username')
menu.add.text_input('',default='')

menu.add.label('Your email address')
menu.add.text_input('',default='')


menu.mainloop(surface)