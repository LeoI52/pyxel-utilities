"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 06/06/2025
"""

from .animation import *
from .game import *
from .palette import *
from .var import *

__version__ = "0.1.7"

__all__ = [
    "follow_path", "target_motion", "lerp", "ease_in_out", "wave_motion", "circular_motion", "elliptical_motion", "spiral_motion", "infinity_motion", "back_forth_motion",
    "PyxelManager", "Scene",
    "hex_to_rgb", "rgb_to_hex", "inverted_palette", "grayscaled_palette", "black_white_palette", "random_color_jitter_palette", "night_vision_palette", "heat_map_palette", "water_palette", "fire_palette", "psychedelic_shifting_palette", "sepia_palette", "neon_palette", "brightness_adjusted_palette", "posterize_palette",
    "DEFAULT_PYXEL_COLORS"
]