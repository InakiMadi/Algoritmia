from src.FindConnectedComponents import find_connected_components
import time


def print_success_failure(is_success: bool, num_test: int, expected_output: any, provided_output: any,
                          time_difference: float) -> None:
    if is_success:
        print('\x1b[5;30;42m' + 'Success!' + '\x1b[0m', end=" ")
    else:
        print('\x1b[5;30;41m' + 'Failure.' + '\x1b[0m', end=" ")
    print(
        f"Example {num_test}. Expected: {str(expected_output)} --- Provided: {str(provided_output)}. Time running: {time_difference}.")


if __name__ == '__main__':
    with open('examples.txt', 'r') as f_in:
        num_examples = int(f_in.readline())

        for num_example in range(num_examples):
            d_size = int(f_in.readline())

            d = list(map(int, f_in.readline().rstrip().split()))

            start = time.perf_counter()
            components = find_connected_components(d)
            end = time.perf_counter()
            dif_time = end - start

            expected_output = str(f_in.readline().split()[0])
            if str(components) == expected_output:
                print_success_failure(True, num_example + 1, expected_output, components, dif_time)
            else:
                print_success_failure(False, num_example + 1, expected_output, components, dif_time)
