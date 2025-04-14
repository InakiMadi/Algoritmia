from src.FindPath import find_path
from io import StringIO
from unittest.mock import patch
import time
import math


def success_ratio(cities_visited: int, cities: int) -> float:
    percentage = (cities_visited / cities) ** 2 * 100
    return math.ceil(percentage / 5) * 5


def print_success_ratio(cities_visited: int, cities: int) -> None:
    print(f"Success ratio: {str(success_ratio(cities_visited, cities))}.")


def print_success_failure(num_test: int, expected_output: any, provided_output: any,
                          time_difference: float) -> None:
    if str(expected_output) == str(provided_output):
        print('\x1b[5;30;42m' + 'Success!' + '\x1b[0m', end=" ")
    else:
        print('\x1b[5;30;41m' + 'Failure.' + '\x1b[0m', end=" ")
    print(
        f"Example {num_test}. Expected: {str(expected_output)} --- Provided: {str(provided_output)}. Time running: {time_difference}."
    )


if __name__ == '__main__':
    with open('examples.txt', 'r') as f_in:
        num_examples = int(f_in.readline())

        for num_example in range(num_examples):
            n_cities, m_roads = map(int, f_in.readline().split())

            roads = []
            for road in range(m_roads):
                city_a, city_b = map(int, f_in.readline().split())
                roads.append((city_a, city_b))

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                start = time.perf_counter()
                find_path(roads)
                end = time.perf_counter()
                time_dif = end - start

                output = mock_stdout.getvalue().strip()
            expected = f_in.readline() + f_in.readline().strip()

            print_success_failure(num_example + 1, expected, output, time_dif)
            d = int(output.split()[0])
            n = int(expected.split()[0])
            print_success_ratio(d, n)
