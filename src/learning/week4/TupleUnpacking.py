"""
File: TupleUnpacking.py
Author: Shiqi Su
Date: 2025-08-22 15:13
Description:
"""
def get_names() -> tuple[str, str]:
    name = input('Enter your name: ' )
    first, _, last =  name.partition(" ")
    return first, last

print(get_names())