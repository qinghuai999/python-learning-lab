"""
File: CloseTo.py
Author: Shiqi(Kiki) Su
Date: 2025-09-28 11:05
Description:
"""
def close_to(p1: tuple[int], p2: tuple[int]) -> bool:
    DISTANCE = 1600
    p1_len, p1_wei = p1
    p2_len, p2_wei = p2
    distance = (p1_len - p2_len) ** 2 + (p1_wei - p2_wei) ** 2
    if distance < DISTANCE:
        return True
    return False
