from pyxel_utilities import *
import pyxel

def update():
    pass

def draw():
    global x1, y1, x2, y2, x3, y3, cp

    pyxel.cls(12)

    x1, y1 = infinity_motion(140, 70, 20, 0.05, pyxel.frame_count)
    x2, y2 = circular_motion(30, 90, 10, 0.1, pyxel.frame_count)
    x3, y3, cp = follow_path(x3, y3, 1, cp, points)

    pyxel.circ(30, wave_motion(50, 20, 5, pyxel.frame_count), 4, 8)
    pyxel.circ(x1, y1, 4, 9)
    pyxel.circ(x2, y2, 4, 10)
    pyxel.circ(x3, y3, 4, 11)

main_scene = Scene(0, "Example 1", update, draw)
scenes = [main_scene]
manager = PyxelManager(228, 128, scenes, fullscreen=True, mouse=True)

x1 = y1 = 0
x2 = y2 = 0
x3 = y3 = cp = 0

points = [(40, 5), (200, 30), (180, 100)]

manager.run()