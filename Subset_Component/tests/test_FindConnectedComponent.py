from Subset_Component.src.FindConnectedComponents import find_connected_components, count_components

NUM_VERTICES = 64


def test_single_subset_count_component():
    assert count_components([5], NUM_VERTICES) == NUM_VERTICES - 1
    assert count_components([2], NUM_VERTICES) == NUM_VERTICES
    assert count_components([8], NUM_VERTICES) == NUM_VERTICES
    assert count_components([13], NUM_VERTICES) == NUM_VERTICES - 2
    assert count_components([21], NUM_VERTICES) == NUM_VERTICES - 2
    assert count_components([1864], NUM_VERTICES) == NUM_VERTICES - 4


def test_multiple_subset_count_component():
    assert count_components([2, 5], NUM_VERTICES) == count_components([5], NUM_VERTICES)
    assert count_components([16, 1, 2, 1, 0], NUM_VERTICES) == count_components([16], NUM_VERTICES)
    assert count_components([3, 5], NUM_VERTICES) == NUM_VERTICES - 2
    assert count_components([13, 1864], NUM_VERTICES) == NUM_VERTICES - 6


def test_find_connected_components():
    assert find_connected_components([2, 5, 9], NUM_VERTICES) == 504
    assert find_connected_components([1, 2, 3, 5], NUM_VERTICES) == 1008
    assert find_connected_components(
        [4436029718484152282, 7960688025537172878, 8158153106283749652, 816298623023398913, 7910562653274884366,
         4146540260192962824, 7707065686924684372, 95813014895467638], NUM_VERTICES) == 2044
    assert find_connected_components(
        [8522357958038330373, 2212193802576548715, 182733964020046049, 5938151776961444566, 2702478012963329436,
         4495601037073630765, 713431950751932924, 8971767746286798272, 2845016184399378689, 7060716320187277676,
         7393123719362815506, 103488518718542576, 4609307071421890032, 7380165043248963518, 1514470810187520170,
         7866443618601539512, 4517749074603872116, 3448649611504356278, 5639082938289156423], NUM_VERTICES) == 1193151
