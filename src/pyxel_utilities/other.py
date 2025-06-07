"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 07/06/2025
"""

from .vars import *

def get_anchored_position(x:int, y:int, w:int, h:int, anchor:int)-> tuple:
    if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
        x -= w
    if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
        y -= h
    if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
        x -= w // 2
    if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
        y -= h // 2
        
    return x, y
