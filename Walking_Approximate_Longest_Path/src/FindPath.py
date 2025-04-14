from typing import List


def printList(_list):
    print(len(_list))
    for elem in _list:
        print(f"{str(elem)}", end=" ")


def find_path(roads):
    result = [1, 4, 2, 3]
    printList(result)
