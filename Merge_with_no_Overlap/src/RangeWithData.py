from src.Range import Range
from typing import Self, List


class RangeWithData:
    def __init__(self, range_start: int, range_end: int, data: str):
        self.range_start = range_start
        self.range_end = range_end
        self.data = data

    def __repr__(self):
        return f"{self.range_start}|{self.range_end}|{self.data}|"

    def get_range_start(self) -> int:
        return self.range_start

    def get_range_end(self) -> int:
        return self.range_end

    def get_data(self) -> str:
        return self.data

    def is_range_in_self_range(self, other_range: Range) -> bool:
        if self.range_start <= other_range.get_range_start() and other_range.get_range_end() <= self.range_end:
            return True
        return False

    @classmethod
    def read_file(cls, filename: str) -> List[Self]:
        entries = []
        with (open(filename, 'r') as file):
            for line in file:
                parts = []
                # Remove any leading/trailing whitespace and split by '|'
                parts_aux = line.strip().split('|')
                # Filter out empty strings from split (in case of || or trailing |)
                for part in parts_aux:
                    if part:
                        parts.append(part)

                if len(parts) == 3:
                    entries.append(RangeWithData(int(parts[0]), int(parts[1]), parts[2]))

        return entries

    @classmethod
    def search_data_in_range(cls, ranges_with_data: List[Self], other_range: Range) -> str:
        for range_with_data in ranges_with_data:
            if range_with_data.is_range_in_self_range(other_range):
                return range_with_data.get_data()
        return ""

    @classmethod
    def ordered_ranges_limits(cls, ranges_with_data_1: List[Self], ranges_with_data_2: List[Self]) -> List[int]:
        ranges_limits = set()  # Avoid repetition
        for range_with_data in ranges_with_data_1 + ranges_with_data_2:
            ranges_limits.add(range_with_data.get_range_start())
            ranges_limits.add(range_with_data.get_range_end())
        return sorted(ranges_limits)

    @classmethod
    def intersection_ranges_with_data(cls, ranges_with_data_1: List[Self], ranges_with_data_2: List[Self]) -> List[
        Self]:
        intersections: List[RangeWithData] = []
        ordered_ranges_limits = RangeWithData.ordered_ranges_limits(ranges_with_data_1, ranges_with_data_2)

        for limit_index in range(len(ordered_ranges_limits) - 1):
            start = ordered_ranges_limits[limit_index]
            end = ordered_ranges_limits[limit_index + 1]
            new_range: Range = Range(start, end)

            data_x = RangeWithData.search_data_in_range(ranges_with_data_1, new_range)
            data_y = RangeWithData.search_data_in_range(ranges_with_data_2, new_range)

            # Only save new intersection when both datas are not empty
            if data_x or data_y:
                new_intersection = RangeWithData(start, end, f"{data_x}|{data_y}")
                intersections.append(new_intersection)
        return intersections
