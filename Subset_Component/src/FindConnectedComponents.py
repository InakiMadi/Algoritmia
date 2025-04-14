from typing import List


def is_bit_one(number: int, lower_bit: int) -> bool:
    bit_in_lower_bit = number >> lower_bit
    return (bit_in_lower_bit & 1) == 1


def how_many_ones_in_binary(number: int) -> int:
    return number.bit_count()


def count_components_from_binary(num_ones_in_joint: int, num_vertices: int = 64) -> int:
    if num_ones_in_joint == 0:
        return num_vertices
    else:
        return num_vertices - (num_ones_in_joint - 1)


def count_components(numbers: List[int], num_vertices: int = 64) -> int:
    joint = 0
    if len(numbers) == 0:
        return num_vertices
    elif len(numbers) == 1:
        joint = numbers[0]
    else:
        for number in numbers:
            if (how_many_ones_in_binary(number)) >= 2:
                joint = joint | number

    num_ones_in_joint = how_many_ones_in_binary(joint)
    return count_components_from_binary(num_ones_in_joint, num_vertices)


def how_many_subsets(count_numbers: int) -> int:
    return 2 ** count_numbers


def find_subset(numbers: List[int], subset_binary: int) -> List[int]:
    subset = []
    for lower_bit in range(len(numbers)):
        should_current_number_be_in_subset = is_bit_one(subset_binary, lower_bit)
        if should_current_number_be_in_subset:
            subset.append(numbers[lower_bit])
    return subset


def find_connected_components(numbers: List[int], num_vertices: int = 64) -> int:
    subsets_amount = how_many_subsets(len(numbers))
    total_sum = num_vertices
    for subset_binary in range(1, subsets_amount):
        subset = find_subset(numbers, subset_binary)
        num_components = count_components(subset, num_vertices)
        total_sum = total_sum + num_components

    return total_sum
