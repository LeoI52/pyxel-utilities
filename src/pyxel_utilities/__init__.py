"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 05/06/2025
"""

from .game import PyxelManager, Scene
from .var import DEFAULT_PYXEL_COLORS

__version__ = "0.1.2"

__all__ = [
    "PyxelManager", "Scene",
    "DEFAULT_PYXEL_COLORS"
]