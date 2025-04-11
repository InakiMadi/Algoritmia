from Python.Grid.src.GridOrder import Grid

def test_ordered_grid_challenge():
    grid = Grid(['ebacd','fghij','olmkn','trpqs','xywuv'])
    assert grid.grid_challenge() == "YES"

def test_unordered_grid_challenge():
    grid = Grid(['bcd','aem','abc'])
    assert grid.grid_challenge() == "NO"