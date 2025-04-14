from typing import List


def is_bit_one(number: int, lower_bit: int) -> bool:
    return (number >> lower_bit & 1) == 1


def how_many_ones_in_binary(number: int) -> int:
    return number.bit_count()


'''
def count_total_edges(number: int) -> int:
    Combinatorics. Number of edges = C(n,2). And P(n,r) = C(n,r) * P(r,r). P(2,2) = 2! = 2.
    Can also be seen as calculating P(n,2) and then removing half of them, due to order not mattering.
    
    return int(num_ones * (num_ones - 1) / 2)
'''


def count_components(numbers: List[int]) -> int:
    if len(numbers) == 0:
        return 64
    elif len(numbers) == 1:
        '''
            Number of connected components is 0 if, in binary, there is no 1s or only one 1 (no edges).
            Else, it is the number of vertices (64) - (number of 1s in binary - 1).
            (number of 1s - 1) because it is the number of edges ONLY for the outline/contour, without closing.
        '''
        number = numbers[0]
        num_ones_in_binary = how_many_ones_in_binary(number)
        if num_ones_in_binary == 0:
            return 0
        else:
            return num_ones_in_binary - 1
    else:
        '''
            Same discussion as before, but now the binary representation is the OR of all the binary reprs.,
            except the representations with only one 1 (again, no edges, but with OR can create a new undesirable edge).
            It is the OR of all numbers in binary because it is the number of edges ONLY for the outline. If they were
            separated, they are together due to definition of the problem, so no need to subtract any more 1s. If
            they touch, it's again simply calculating the number of edges of the outline/contour (without closing).
            
            Example:
            {3,21}
            3 -> (0,1). Components: 64 - 1 = 63. (Two 1s in binary).
            21 -> (0,2), (2,4), (0,4). For components, last one didn't matter. So, without closing,
                  (0,2), (2,4). Components: 64 - 2 = 62. (Three 1s in binary).
            [3,21] can be seen as -> (0,1), (0,2), (2,4). (3 | 21 = 25. Four 1s in binary).
                                     Components: 64 - 3 = 61.
            
            Another example:
            {Upwards triangle, downwards triangle}.
            Joint: They touch only in one point (height point of each).
            Connected components: Calculate the edges of the outline of the joint is the same as calculating the edges
            of the outline of the uppercase greek letter Sigma. And we can get Sigma representation calculating the
            OR of the triangles.
        '''
        joint = 0
        for number in numbers:
            if (how_many_ones_in_binary(number)) >= 2:
                joint = joint | number
        num_ones_in_joint = how_many_ones_in_binary(joint)
        if num_ones_in_joint == 0:
            return 0
        else:
            return num_ones_in_joint - 1


def how_many_subsets(count_numbers: int) -> int:
    return 2 ** count_numbers


def find_connected_components(numbers: List[int]) -> int:
    subsets_amount = how_many_subsets(len(numbers))
    total_sum = 64 * subsets_amount
    for subset_binary in range(1, subsets_amount):
        # Find the specific subset
        subset = []
        for lower_bit in range(len(numbers)):
            if is_bit_one(subset_binary, lower_bit):
                subset.append(numbers[lower_bit])
        # Count components for the found subset
        num_components = count_components(subset)
        total_sum = total_sum - num_components

    return total_sum
