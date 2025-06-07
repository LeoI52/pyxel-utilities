from pyxel_utilities import *
import pyxel

lerp_current = 40
lerp_target = 160

wave_points = []

inf_points = []

path_follower_x = 75
path_follower_y = 75
path_current_point = 0
path_points = [(75, 75), (175, 75), (175, 110), (75, 110)]

def update():
    global lerp_current, lerp_target, path_follower_x, path_follower_y, path_current_point

    #? Lerp
    if pyxel.frame_count % 120 == 0:
        lerp_target = 160 if lerp_target == 40 else 40
    lerp_current = lerp(lerp_current, lerp_target, 0.05)

    #? Path Follower
    path_follower_x, path_follower_y, path_current_point = follow_path(path_follower_x, path_follower_y, 1.5, path_current_point, path_points, True)

def draw():
    pyxel.cls(12)

    #? Lerp
    pyxel.text(5, 5, "Lerp:", 1)
    pyxel.rectb(40, 5, 8, 4, 9)
    pyxel.rectb(160, 5, 8, 4, 9)
    pyxel.rect(lerp_current, 5, 8, 4, 1)

    #? Ease In Out
    pyxel.text(5, 15, "Ease In/Out:", 1)
    t = (pyxel.frame_count % 120) / 120.0
    eased_t = ease_in_out(t)
    ease_x = 60 + eased_t * 50
    pyxel.line(60, 19, 110, 19, 9)
    pyxel.circ(ease_x, 17, 2, 1)

    #? Wave Motion
    pyxel.text(5, 25, "Wave:", 1)
    wave_y = wave_motion(27, 20, 3, pyxel.frame_count)
    if wave_y not in wave_points:
        wave_points.append(wave_y)
    for y in wave_points:
        pyxel.pset(30, y, 9)
    pyxel.circ(30, wave_y, 2, 1)

    #? Circular Motion
    pyxel.text(5, 35, "Circular:", 1)
    circ_x, circ_y = circular_motion(60, 38, 10, 0.05, pyxel.frame_count)
    pyxel.circb(60, 38, 10, 9)
    pyxel.circ(circ_x, circ_y, 2, 1)

    #? Infinity Motion
    pyxel.text(5, 45, "Infinity:", 1)
    inf_x, inf_y = infinity_motion(120, 48, 30, 0.03, pyxel.frame_count)
    if (inf_x, inf_y) not in inf_points:
        inf_points.append((inf_x, inf_y))
    for x, y in inf_points:
        pyxel.pset(x, y, 9)
    pyxel.circ(inf_x, inf_y, 2, 1)

    #? Path Follower
    pyxel.text(5, 75, "Path Follower:", 1)
    for i in range(len(path_points)):
        next_i = (i + 1) % len(path_points)
        pyxel.line(path_points[i][0], path_points[i][1], path_points[next_i][0], path_points[next_i][1], 9)
        pyxel.circb(path_points[i][0], path_points[i][1], 2, 9)
    pyxel.circ(int(path_follower_x), int(path_follower_y), 3, 1)

scene = Scene(0, "Animations.py Example", update, draw)
manager = PyxelManager(228, 128, [scene], fullscreen=True, mouse=True)
manager.run()