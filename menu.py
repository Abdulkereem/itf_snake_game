import pygame
import pygame_menu
from audio.media import MediaPlayer


pygame.init()

surface = pygame.display.set_mode((600,400))

md  = MediaPlayer('audio/sound/bg.mp3')
md.load_sound()
md.play()
def start_game():
    print("will start game here")

def settings():
    pass


menu = pygame_menu.Menu("Snake Xenzia ITF",400,300,
                                                theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Set Player Name',default='Omega Man')
menu.add.button("Play",start_game)
menu.add.button("Settings",settings)
menu.add.button('Exit',pygame_menu.events.EXIT)




menu.mainloop(surface)