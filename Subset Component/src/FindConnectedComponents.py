from typing import List


def is_bit_one(number: int, lower_bit: int) -> bool:
    return (number >> lower_bit & 1) == 1


def how_many_ones_in_binary(number: int) -> int:
    num_ones = 0
    for lower_bit in range(64):
        if is_bit_one(number, lower_bit):
            num_ones += 1
    return num_ones


def how_many_ones_in_list(zeroes_and_ones: List[int]) -> int:
    return zeroes_and_ones.count(1)


def count_edges(number: int) -> int:
    '''
    Old version (qudratic):
    for lower_bit_i in range(63):
        for lower_bit_j in range(lower_bit_i + 1, 63):
            if bit(number, lower_bit_i) == 1 and bit(number, lower_bit_j) == 1:
                edges_count += 1
    '''
    num_ones = how_many_ones_in_binary(number)
    '''
    Combinatorics. Number of edges = C(n,2). And P(n,r) = C(n,r) * P(r,r). P(2,2) = 2! = 2.
    Can also be seen as calculating P(n,2) and then removing half of them, due to order not mattering.
    '''
    return int(num_ones * (num_ones - 1) / 2)


# Needs optimization
def count_components(numbers: List[int]) -> int:
    if len(numbers) == 0:
        return 64
    elif len(numbers) == 1:
        return how_many_ones_in_binary(numbers[0]) - 1
    else:
        binary_joint = [0] * 64
        for number in numbers:
            if (how_many_ones_in_binary(number)) >= 2:
                number_binary = [int(x) for x in bin(number)[2:]]
                index_differences = len(binary_joint) - len(number_binary)
                number_binary = [0] * index_differences + number_binary
                binary_joint = [a | b for a, b in zip(binary_joint, number_binary)]
        count_ones_in_binary_joint = how_many_ones_in_list(binary_joint)
        if count_ones_in_binary_joint == 0:
            return 0
        else:
            return how_many_ones_in_list(binary_joint) - 1


def how_many_subsets(count_numbers: int) -> int:
    return 2 ** count_numbers


def find_connected_components(numbers: List[int]) -> int:
    subsets_amount = how_many_subsets(len(numbers))
    total_sum = 64 * subsets_amount
    for i in range(1, subsets_amount):
        # Find the specific subset
        subset = []
        for lower_bit in range(len(numbers)):
            if is_bit_one(i, lower_bit):
                subset.append(numbers[lower_bit])
        # Count components for the found subset
        num_components = count_components(subset)
        total_sum = total_sum - num_components

    return total_sum
