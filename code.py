import ugame
import stage
import time
import random




import constants




def splash_scene():




    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)








    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")




    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    background.tile(2, 2, 0)  # blank white




    background.tile(3, 2, 1)




    background.tile(4, 2, 2)




    background.tile(5, 2, 3)




    background.tile(6, 2, 4)




    background.tile(7, 2, 0)  # blank white












    background.tile(2, 3, 0)  # blank white




    background.tile(3, 3, 5)




    background.tile(4, 3, 6)




    background.tile(5, 3, 7)




    background.tile(6, 3, 8)




    background.tile(7, 3, 0)  # blank white












    background.tile(2, 4, 0)  # blank white




    background.tile(3, 4, 9)




    background.tile(4, 4, 10)




    background.tile(5, 4, 11)




    background.tile(6, 4, 12)




    background.tile(7, 4, 0)  # blank white












    background.tile(2, 5, 0)  # blank white




    background.tile(3, 5, 0)




    background.tile(4, 5, 13)




    background.tile(5, 5, 14)




    background.tile(6, 5, 0)




    background.tile(7, 5, 0)  # blank white








    game = stage.Stage(ugame.display, constants.FPS)




    game.layers = [background]




    game.render_block()




    while True:




        time.sleep(2.0)
        menu_scene()




def menu_scene():








    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")




    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE,
buffer=None)
    text1.move(20,10)
    text1.text("MT Game Studios")
    text.append(text1)




    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE,
buffer=None)
    text2.move(40, 110)
    text2("PRESS START")
    text.append(text2)




    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)








    game = stage.Stage(ugame.display, constants.FPS)




    game.layers = text + [background]




    game.render_block()




    while True:




        keys = ugame.buttons.get_pressed()




        if keys & ugame.K_START != 0:
            print("Start")








        game.tick()




def game_scene():








    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")




    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]




    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)








    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)




    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))




    alien= stage.Sprite(image_bank_sprites, 9,
                        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        lasers.append(a_single_laser)



    game = stage.Stage(ugame.display, constants.FPS)




    game.layers = lasers + [ship] + [alien] + [background]




    game.render_block()




    while True:




        keys = ugame.buttons.get_pressed()




        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button up"]:
                a_button = constants.button_state["button just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)








        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                    ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass




        if a_button == constants.button_state["button_just_pressed"]:

            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship,x, ship,y)
                    sound.play(pew_sound)
                    break




        game.render_sprites([ship] + [alien])
        game.tick()












if __name__ == "__main__":
    menu_scene()


