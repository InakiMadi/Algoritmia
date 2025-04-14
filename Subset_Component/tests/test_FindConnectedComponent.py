from src.FindConnectedComponents import find_connected_components
from src.FindConnectedComponents import count_components


def test_simple_count_component():
    assert count_components([5]) == 1
