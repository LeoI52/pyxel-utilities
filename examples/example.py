from pyxel_utilities import *
import pyxel
import time

def update_main():
    if pyxel.btnp(pyxel.KEY_SPACE):
        manager.change_scene_triangle(1, 10, 1, 10)

def draw_main():
    pyxel.cls(10)

def update_game():
    if pyxel.btnp(pyxel.KEY_SPACE):
        manager.change_scene(0)

def draw_game():
    pyxel.cls(8)

main_scene = Scene(0, "Main", update_main, draw_main, on_exit=lambda:print("quit main"))
game_scene = Scene(1, "Game", update_game, draw_game, on_enter=lambda:print("enter game"))
manager = PyxelManager(228, 128, [main_scene, game_scene], fullscreen=True, mouse=True)

manager.run()