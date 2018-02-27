import pygame
import os
import menu
import util
import Camera
import Car
import LevelLoader


display = pygame.display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
action_list = util.action_list

map_name = 0
map_index = 0
gamecycle = True
pygame.init()
background = pygame.image.load(os.path.join('data', 'menu_screen.png'))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
black = (0, 0, 0, 255)
image = 0
rotation_turn = 0
accelerating, rotating, steering = False, False, False
entities = pygame.sprite.Group()
paused = False

music = -1

game_GUI = menu.init_default_GUI(screen)

pygame.mixer.init()

game = False
major_gamecycle = True

music_acceleration = pygame.mixer.Sound(os.path.join('data', 'accelerating.ogg'))
music_rotating = pygame.mixer.Sound(os.path.join('data', 'rotate.ogg'))
music_steering = pygame.mixer.Sound(os.path.join('data', 'steering.ogg'))


while major_gamecycle:
    if gamecycle:
        menu_GUI = menu.menu_GUI(screen)
    while gamecycle:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gamecycle = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = menu_GUI.get_event(e.pos)
                if pressed_button:
                    action = pressed_button.on_click()
                    if action:
                        exec(action_list[action])
        screen.fill(black)
        screen.blit(background, (0, 0))
        menu_GUI.draw(screen)
        display.update()
    if game:
        mapdata, tiles, obstacles, finish = LevelLoader.load_level(map_name)
        entities = pygame.sprite.Group()
        main_car = Car.Car('car')
        camera = Camera.Camera(Camera.camera_configure, mapdata.width * 32, mapdata.height * 32, screen.get_width(), screen.get_height())
        entities.add(main_car)
        game_GUI = menu.init_default_GUI(screen)
        paused = False
        rotation_turn = 0
        accelerating, rotating, steering = False, False, False
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gamecycle = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    rotation_turn = 3
                    rotating = True
                if e.key == pygame.K_s:
                    steering = True
                    # MOVE[0] = main_car.svel / 3
                if e.key == pygame.K_d:
                    rotation_turn = -3
                    rotating = True
                if e.key == pygame.K_w:
                    #  MOVE[0] = -main_car.svel / 3
                    accelerating = True
                if e.key == pygame.K_ESCAPE:
                    game_GUI.get_GUIElement_by_name('menu_overlay').visible = not game_GUI.get_GUIElement_by_name('menu_overlay').visible
                    game_GUI.get_GUIElement_by_name('continue').visible = not game_GUI.get_GUIElement_by_name('continue').visible
                    game_GUI.get_GUIElement_by_name('exit_game').visible = not game_GUI.get_GUIElement_by_name('exit_game').visible
                    game_GUI.get_GUIElement_by_name('exit_to_menu').visible = not game_GUI.get_GUIElement_by_name('exit_to_menu').visible
                    paused = not paused
                    # print(menu_overlay.visible)
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    rotating = False
                    rotation_turn = 0
                if e.key == pygame.K_s:
                    # MOVE[0] =  0
                    steering = False
                if e.key == pygame.K_d:
                    rotation_turn = 0
                    rotating = False
                if e.key == pygame.K_w:
                    # MOVE[0] = 0
                    # MOVE[1] = 0
                    # print('up')
                    accelerating = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = game_GUI.get_event(e.pos)
                if pressed_button:
                    action = pressed_button.on_click()
                    if action:
                        exec(action_list[action])

        # if not rotating and music == 1:
        #     pygame.mixer.stop()
        #     music = -1
        if not (accelerating or abs(main_car.vel) >= 5) and music == 0:
            pygame.mixer.stop()
            music = -1


        #print(abs(main_car.vel))
        if not pygame.mixer.get_busy():
            if abs(main_car.vel) >= 5:
                music_acceleration.play()
                music = 0
        #   elif rotating and abs(main_car.vel) > 0:
        #        music_rotating.play()
        #        music = 1
        #    elif not accelerating and 8 >= abs(main_car.vel) >= 2:
        #        music_steering.play()
        #        music = 2
        #    else:
        #        pass
        if pygame.sprite.collide_rect(main_car, finish):
            exec(action_list['B_EXIT_MENU'])
        screen.fill(black)
        if not paused:
            main_car.update(screen, rotation_turn, tiles, rotating, accelerating, steering)
        for e in tiles:
            screen.blit(e.image, camera.apply(e))
        for e in obstacles:
            screen.blit(e.image, camera.apply(e))
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        # print(GUI.sprite_group)
        game_GUI.draw(screen)
        camera.update(main_car)
        # print(main_car.rect)
        # print(main_car.rect.x, main_car.rect.y)
        display.update()
    pygame.mixer.stop()
pygame.quit()

