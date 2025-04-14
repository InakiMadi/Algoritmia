from typing import Self, List


class Range:
    def __init__(self, range_start: int, range_end: int):
        self.range_start = range_start
        self.range_end = range_end

    def __repr__(self):
        return f"{self.range_start}|{self.range_end}|"

    def get_range_start(self) -> int:
        return self.range_start

    def get_range_end(self) -> int:
        return self.range_end
