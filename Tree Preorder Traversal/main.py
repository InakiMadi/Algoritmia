from src.Node import Node
from src.BinarySearchTree import BinarySearchTree


def preOrder(root: Node) -> None:
    if root == None:
        return
    print(root.info, end=" ")
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)


if __name__ == "__main__":
    tree = BinarySearchTree()

    with open('example1.txt', 'r') as file:
        t = int(file.readline())

        arr = list(map(int, file.readline().split()))

        for i in range(t):
            tree.create(arr[i])

        preOrder(tree.root)

        print()
        expected_output = file.readline()
        print(expected_output)

    print()
    tree = BinarySearchTree()

    with open('example2.txt', 'r') as file:
        t = int(file.readline())

        arr = list(map(int, file.readline().split()))

        for i in range(t):
            tree.create(arr[i])

        preOrder(tree.root)

        print()
        expected_output = file.readline()
        print(expected_output)
