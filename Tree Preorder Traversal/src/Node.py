from typing import Optional, Self


class Node:
    def __init__(self, info):
        self.info: int = info  # Value of the node
        self.left: Optional[Self] = None  # Left child
        self.right: Optional[Self] = None  # Right child
        self.level = None

    def __str__(self):
        return str(self.info)
