"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 07/06/2025
"""

from .other import get_anchored_position
from .vars import *
import random
import pyxel
import math

class Sprite:

    def __init__(self, img:int, u:int, v:int, w:int, h:int, colkey:int=None):
        self.img = img
        self.u, self.v = u, v
        self.w, self.h = w, h
        self.colkey = 0 if colkey == 0 else colkey
        self.flip_horizontal = False
        self.flip_vertical = False

class Animation:

    def __init__(self, sprite:Sprite, total_frames:int=1, frame_duration:int=20, loop:bool=True):
        self.sprite = sprite
        self.__total_frames = total_frames
        self.frame_duration = frame_duration
        self.__loop = loop
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def is_finished(self)-> bool:
        return self.__is_finished and not self.__loop
    
    def is_looped(self)-> bool:
        return self.__loop
    
    def reset(self):
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def update(self):
        if self.is_finished():
            return
        
        if pyxel.frame_count - self.__start_frame >= self.frame_duration:
            self.__start_frame = pyxel.frame_count
            self.current_frame += 1
            if self.current_frame >= self.__total_frames:
                if self.__loop:
                    self.current_frame = 0
                else:
                    self.__is_finished = True
                    self.current_frame = self.__total_frames - 1

    def draw(self, x:int, y:int, anchor:int=ANCHOR_TOP_LEFT):
        x, y = get_anchored_position(x, y, self.sprite.w, self.sprite.h, anchor)

        w = -self.sprite.w if self.sprite.flip_horizontal else self.sprite.w
        h = -self.sprite.h if self.sprite.flip_vertical else self.sprite.h
        pyxel.blt(x, y, self.sprite.img, self.sprite.u + self.current_frame * abs(self.sprite.w), self.sprite.v, w, h, self.sprite.colkey)

def rounded_rect(x:int, y:int, width:int, height:int, corner_radius:int, color:int):
    corner_radius = min(corner_radius, min(width, height) // 2)
    corner_radius = int(corner_radius)

    pyxel.rect(x + corner_radius, y, width - 2 * corner_radius, height, color)
    pyxel.rect(x, y + corner_radius, width, height - 2 * corner_radius, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                if i*i + j*j <= corner_radius*corner_radius:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

def rounded_rectb(x:int, y:int, width:int, height:int, corner_radius:int, color:int):
    corner_radius = min(corner_radius, min(width, height) // 2)

    pyxel.line(x + corner_radius, y, x + width - corner_radius - 1, y, color)
    pyxel.line(x + corner_radius, y + height - 1, x + width - corner_radius - 1, y + height - 1, color)
    pyxel.line(x, y + corner_radius, x, y + height - corner_radius - 1, color)
    pyxel.line(x + width - 1, y + corner_radius, x + width - 1, y + height - corner_radius - 1, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                dist = math.sqrt(i*i + j*j)
                if corner_radius - 0.5 <= dist <= corner_radius + 0.5:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

def draw_speech_bubble(x:int, y:int, width:int, height:int, tail_size:int, tail_target_x:int, tail_target_y:int, color:int, corner_radius:int=0, border:bool=False, border_color:int=0, tail_position:int=BOTTOM):
    rounded_rect(x, y, width, height, corner_radius, color)
    if border:
        rounded_rectb(x, y, width, height, corner_radius, border_color)

    tail_x = x + width // 2
    tail_y = y + height // 2
    if tail_position == BOTTOM:
        pyxel.tri(tail_x - tail_size // 2, y + height, tail_x + tail_size // 2, y + height, tail_target_x, tail_target_y, color)
        if border:
            pyxel.line(tail_x - tail_size // 2, y + height, tail_target_x, tail_target_y, border_color)
            pyxel.line(tail_x + tail_size // 2, y + height, tail_target_x, tail_target_y, border_color)
    elif tail_position == TOP:
        pyxel.tri(tail_x - tail_size // 2, y, tail_x + tail_size // 2, y, tail_target_x, tail_target_y, color)
        if border:
            pyxel.line(tail_x - tail_size // 2, y, tail_target_x, tail_target_y, border_color)
            pyxel.line(tail_x + tail_size // 2, y, tail_target_x, tail_target_y, border_color)
    elif tail_position == LEFT:
        pyxel.tri(x, tail_y - tail_size // 2, x, tail_y + tail_size // 2, tail_target_x, tail_target_y, color)
        if border:
            pyxel.line(x, tail_y - tail_size // 2, tail_target_x, tail_target_y, border_color)
            pyxel.line(x, tail_y + tail_size // 2, tail_target_x, tail_target_y, border_color)
    elif tail_position == RIGHT:
        pyxel.tri(x + width, tail_y - tail_size // 2, x + width, tail_y + tail_size // 2,tail_target_x, tail_target_y,color)
        if border:
            pyxel.line(x + width, tail_y - tail_size // 2, tail_target_x, tail_target_y, border_color)
            pyxel.line(x + width, tail_y + tail_size // 2, tail_target_x, tail_target_y, border_color)

def draw_checkered_pattern(x:int, y:int, width:int, height:int, cell_size:int, color1:int, color2:int):
    for row in range((height + cell_size - 1) // cell_size):
        for col in range((width + cell_size - 1) // cell_size):
            color = color1 if (row + col) % 2 == 0 else color2
            rect_x = x + col * cell_size
            rect_y = y + row * cell_size
            rect_w = min(cell_size, x + width - rect_x)
            rect_h = min(cell_size, y + height - rect_y)
            pyxel.rect(rect_x, rect_y, rect_w, rect_h, color)

def draw_brick_wall(x:int, y:int, width:int, height:int, brick_width:int, brick_height:int, color:int, mortar_color:int, mortar_thickness:int=1):
    pyxel.rect(x, y, width, height, mortar_color)
    
    row = 0
    while row * (brick_height + mortar_thickness) < height:
        offset = (row % 2) * (brick_width + mortar_thickness) // 2
        
        col = 0
        while col * (brick_width + mortar_thickness) - offset < width:
            brick_x = x + col * (brick_width + mortar_thickness) - offset
            brick_y = y + row * (brick_height + mortar_thickness)
            
            if brick_x < x + width and brick_y < y + height:
                actual_width = min(brick_width, x + width - brick_x)
                actual_height = min(brick_height, y + height - brick_y)
                if actual_width > 0 and actual_height > 0:
                    pyxel.rect(brick_x, brick_y, actual_width, actual_height, color)
            
            col += 1
        row += 1

def draw_glitch(x:int, y:int, width:int, height:int, intensity:int, colors:list|int):
    colors = [colors] if isinstance(colors, int) else colors
    for _ in range(intensity):
        glitch_y = random.randint(y, y + height)
        pyxel.rect(x, glitch_y, width, 1, random.choice(colors))

def draw_eye(x:int, y:int, target_x:int, target_y:int, eye_radius:int, pupil_radius:int, eye_color:int=7, pupil_color:int=0, max_offset:int=4):
    angle = math.atan2(target_y - y, target_x - x)
    offset_x = math.cos(angle) * max_offset
    offset_y = math.sin(angle) * max_offset
    pyxel.circ(x, y, eye_radius, eye_color)
    pyxel.circ(x + offset_x, y + offset_y, pupil_radius, pupil_color)

def draw_moving_spiral(x:int, y:int, radius:int, color:int, time:int, turns:int=3, segments:int=50, speed:float=0.05):
    for i in range(segments):
        angle = (i / segments) * (turns * math.pi * 2) + time * speed
        r = (i / segments) * radius
        px = x + math.cos(angle) * r
        py = y + math.sin(angle) * r
        pyxel.pset(int(px), int(py), color)
