"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 07/06/2025
"""

from .animation import *
from .collisions import *
from .draw import *
from .game import *
from .lights import *
from .other import *
from .palette import *
from .vars import *

__version__ = "0.1.10"

__all__ = [
    "follow_path", "target_motion", "lerp", "ease_in_out", "wave_motion", "circular_motion", "elliptical_motion", "spiral_motion", "infinity_motion", "back_forth_motion",

    "collision_point_rect", "collision_point_circle", "collision_rect_rect", "collision_circle_circle", "collision_rect_circle", "collision_line_line",

    "Sprite", "Animation", "rounded_rect", "rounded_rectb", "draw_speech_bubble", "draw_checkered_pattern", "draw_brick_wall", "draw_glitch", "draw_eye", "draw_moving_spiral",

    "PyxelManager", "Scene",

    "TriangleLight", "CircleLight", "LightManager",

    "get_anchored_position",

    "hex_to_rgb", "rgb_to_hex", "inverted_palette", "grayscaled_palette", "black_white_palette", "random_color_jitter_palette", "night_vision_palette", "heat_map_palette", "water_palette", "fire_palette", "psychedelic_shifting_palette", "sepia_palette", "neon_palette", "brightness_adjusted_palette", "posterize_palette",

    "DEFAULT_PYXEL_COLORS", "ANCHOR_TOP_LEFT", "ANCHOR_TOP_RIGHT", "ANCHOR_BOTTOM_LEFT", "ANCHOR_BOTTOM_RIGHT", "ANCHOR_LEFT", "ANCHOR_RIGHT", "ANCHOR_TOP", "ANCHOR_BOTTOM", "ANCHOR_CENTER", "BOTTOM", "TOP", "LEFT", "RIGHT"
]