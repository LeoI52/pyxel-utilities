"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 04/06/2025
"""

from .game import PyxelManager, Scene
from .var import DEFAULT_PYXEL_COLORS

__version__ = "0.1.1"

__all__ = [
    "PyxelManager", "Scene",
    "DEFAULT_PYXEL_COLORS"
]