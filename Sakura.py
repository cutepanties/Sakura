#!/usr/bin/env python3

import pygame
import game

# run the game
sakura = game.Sakura()
sakura.start_screen()
while not sakura.done:
    sakura.new_game()
    if sakura.won:
        sakura.bgsound.fadeout(1000)
        sakura.game_over()

pygame.quit()
