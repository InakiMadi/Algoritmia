from src.RangeWithData import RangeWithData
from typing import List

if __name__ == "__main__":
    # Read and parse both files as RangesWithData
    ranges_with_data_X: List[RangeWithData] = RangeWithData.read_file("FileX.txt")
    ranges_with_data_Y: List[RangeWithData] = RangeWithData.read_file("FileY.txt")

    mix_ranges_with_data_X_Y = RangeWithData.intersection_ranges_with_data(ranges_with_data_X, ranges_with_data_Y)

    with open("FileMix.txt", "w") as f_out:
        for range_with_data in mix_ranges_with_data_X_Y:
            # print(elem)
            f_out.write(
                f"{range_with_data.get_range_start()}|{range_with_data.get_range_end()}"
                f"|{range_with_data.get_data()}|\n"
            )
