"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 06/06/2025
"""

from .animation import follow_path, target_motion, lerp, ease_in_out, wave_motion, circular_motion, elliptical_motion, spiral_motion, infinity_motion, back_forth_motion
from .game import PyxelManager, Scene
from .var import DEFAULT_PYXEL_COLORS

__version__ = "0.1.5"

__all__ = [
    "follow_path", "target_motion", "lerp", "ease_in_out", "wave_motion", "circular_motion", "elliptical_motion", "spiral_motion", "infinity_motion", "back_forth_motion",
    "PyxelManager", "Scene",
    "DEFAULT_PYXEL_COLORS"
]