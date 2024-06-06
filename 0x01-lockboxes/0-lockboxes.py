#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """check if the boxes contain key to unlocked all the each other"""
    if not boxes:
        return False

    keys = set()
    keys.add(0)
    size = len(boxes)
    idx = 0
    for box in boxes:
        for key in box:
            if key < size and key != idx:
                keys.add(key)

            if len(keys) == size:
                return True
        idx += 1
    return False
