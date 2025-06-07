from pyxel_utilities import *
import pyxel

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        print(pyxel.mouse_x, pyxel.mouse_y)

def draw():
    pyxel.cls(0)

    pyxel.blt(0, 0, 0, 0, 0, 228, 128)
    l1.draw()
    l2.draw()

PALETTE = DEFAULT_PYXEL_COLORS
PALETTE += brightness_adjusted_palette(PALETTE, {"factor":1.5})
PALETTE[16] = 0x3d3d3d

main_scene = Scene(0, "Example 1", update, draw, "assets.pyxres", PALETTE)
scenes = [main_scene]
manager = PyxelManager(228, 128, scenes, fullscreen=True, mouse=True)

lsd = {x:x+16 for x in range(16)}

l1 = CircleLight(198, 61, 20, lsd, 5)
l2 = TriangleLight(39, 35, 22, 64, 46, 89, lsd, 5)

manager.run()