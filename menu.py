import pygame
import pygame_menu
from audio.media import MediaPlayer
from database.models.middleware import QueryDB
import snake

dbmanager = QueryDB()


pygame.init()

surface = pygame.display.set_mode(pygame.display.get_window_size(),pygame.FULLSCREEN)


try:
    current_player = dbmanager.current_user()
    user = dbmanager.get_user(current_player.username)

except AttributeError:
    user='Malphoy'


md  = MediaPlayer('audio/sound/bg.mp3')
md.load_sound()
md.play()
def start_game():
    snake.main_loop()


def userinput(value):
    pass
    
    # print(user.fullname)



def settings():
    pass


menu = pygame_menu.Menu("Snake Xenzia ITF",400,300,
                                                theme=pygame_menu.themes.THEME_BLUE)

# menu.add.text_input('username: ',default='',onreturn=userinput)
try:
    menu.add.label('Welcome '+str(user.fullname))
except AttributeError:
    menu.add.label('Welcome '+str(user))


menu.add.button("Play",start_game)
menu.add.button("Settings",settings)
menu.add.button('Exit',pygame_menu.events.EXIT)



menu.mainloop(surface)