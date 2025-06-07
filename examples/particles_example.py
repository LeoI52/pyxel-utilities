from pyxel_utilities import *
import random
import pyxel
import math

particle_manager = ParticleManager()
shockwave_manager = ShockwaveManager()
modes = ["oval particle", "rect particle", "triangle particle"]
mode = modes[0]

def update():
    global mode

    shockwave_manager.update()
    particle_manager.update()

    if pyxel.btnp(pyxel.KEY_SPACE):
        mode = modes[(modes.index(mode) + 1) % len(modes)]

    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        shockwave_manager.add_shockwave(CircleShockwave(pyxel.mouse_x, pyxel.mouse_y, random.randint(5, 30), [random.randint(2, 15) for _ in range(3)], 3, random.uniform(1, 2)))
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if mode == "oval particle":
            for _ in range(5):
                angle = random.uniform(0, 2 * math.pi)
                target_x = pyxel.mouse_x + math.cos(angle) * 50
                target_y = pyxel.mouse_y + math.sin(angle) * 50
                s = random.randint(1, 5)
                particle_manager.add_particle(OvalParticle(pyxel.mouse_x, pyxel.mouse_y, s, s, [11, 10, 9, 8], 60, random.uniform(0.5, 1.5), target_x, target_y, 0.1, -0.01, 20))
        elif mode == "rect particle":
            for _ in range(5):
                angle = random.uniform(0, 2 * math.pi)
                target_x = pyxel.mouse_x + math.cos(angle) * 50
                target_y = pyxel.mouse_y + math.sin(angle) * 50
                s = random.randint(1, 5)
                particle_manager.add_particle(RectangleParticle(pyxel.mouse_x, pyxel.mouse_y, s, s, [11, 10, 9, 8], 60, random.uniform(0.5, 1.5), target_x, target_y, 0.1, -0.01, 20))
        elif mode == "triangle particle":
            for _ in range(5):
                angle = random.uniform(0, 2 * math.pi)
                target_x = pyxel.mouse_x + math.cos(angle) * 50
                target_y = pyxel.mouse_y + math.sin(angle) * 50
                particle_manager.add_particle(TriangleParticle(pyxel.mouse_x, pyxel.mouse_y, random.randint(1, 5), [11, 10, 9, 8], 60, random.uniform(0.5, 1.5), target_x, target_y, random.randint(0, 360), 0.1, -0.01, 20, rotating=True))

def draw():
    pyxel.cls(1)

    shockwave_manager.draw()
    particle_manager.draw()

    pyxel.text(5, 5, "Left Click For Particles", 9)
    pyxel.text(5, 15, "Right Click For Shockwaves", 9)
    pyxel.text(5, 25, "Space to change mode", 9)
    pyxel.text(5, 35, f"Mode: {mode}", 9)

scene = Scene(0, "Particles.py Example", update, draw)
manager = PyxelManager(228, 128, [scene], fullscreen=True, mouse=True)
manager.run()