from pyxel_utilities import *
import pyxel
import math

spiral_colors = [8, 9, 10, 11, 12, 13, 14, 15]

def update():
    pass

def draw():
    pyxel.cls(1)

    #? Rounded Rects
    pyxel.text(5, 5, "Rounded Rects:", 9)
    rounded_rect(5, 15, 30, 15, 5, 11)
    rounded_rectb(40, 15, 30, 15, 5, 8)
    rounded_rect(75, 15, 25, 15, 3, 12)
    rounded_rectb(75, 15, 25, 15, 3, 4)

    #? Checkered pattern
    pyxel.text(115, 5, "Checkered:", 9)
    draw_checkered_pattern(115, 15, 40, 25, 5, 6, 14)
    
    #? Brick wall pattern
    pyxel.text(160, 5, "Brick Wall:", 9)
    draw_brick_wall(162, 15, 45, 25, 12, 6, 4, 1, 1)

    #? Glitch effect
    pyxel.text(5, 35, "Glitch Effect:", 9)
    pyxel.rect(5, 45, 40, 25, 7)
    pyxel.text(7, 55, "CORRUPTED", 0)
    draw_glitch(5, 45, 40, 25, 5 + int(math.sin(pyxel.frame_count * 0.1) * 3), [8, 9, 10, 11])

    #? Moving spirals
    pyxel.text(5, 80, "Moving Spirals:", 9)
    draw_moving_spiral(20, 108, 15, 8, pyxel.frame_count, 2, 30, 0.08)
    draw_moving_spiral(50, 108, 12, 11, pyxel.frame_count, 3, 40, -0.06)
    draw_moving_spiral(76, 108, 10, 14, pyxel.frame_count, 4, 25, 0.1)

    #? Colored Spiral
    spiral_color = spiral_colors[int(pyxel.frame_count * 0.1) % len(spiral_colors)]
    draw_moving_spiral(208, 108, 18, spiral_color, pyxel.frame_count, 5, 60, 0.05)

    #? Speech Bubbles
    pyxel.text(80, 44, "Speech Bubbles:", 9)
    draw_speech_bubble(80, 52, 40, 20, 8, 100, 77, 13, 3, True, 5, BOTTOM)
    pyxel.text(85, 57, "Hello!", 0)
    draw_speech_bubble(125, 65, 35, 15, 6, 150, 50, 14, 2, True, 0, TOP)
    pyxel.text(130, 70, "Hi!", 0)
    draw_speech_bubble(170, 50, 25, 15, 5, 160, 58, 9, 2, True, 3, LEFT)
    pyxel.text(175, 55, "Hey", 0)

    #? Tracking Eyes
    pyxel.text(100, 82, "Tracking Eyes:", 9)
    draw_eye(120, 105, pyxel.mouse_x, pyxel.mouse_y, 8, 3, 7, 0, 5)
    draw_eye(150, 105, pyxel.mouse_x, pyxel.mouse_y, 8, 3, 7, 0, 5)

scene = Scene(0, "Draw.py Example", update, draw)
manager = PyxelManager(228, 128, [scene], fullscreen=True, mouse=True)
manager.run()