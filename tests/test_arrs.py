from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([], -1) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 2, 8], 1, -1) == [2, 3, 2]
    assert arrs.my_slice([1, 2, 3, 2, 8], -3, -1) == [3, 2]
    assert arrs.my_slice([1, 2, 3], 4, 6) == []
    assert arrs.my_slice([1, 2, 3, 4], 3, 1) == []
    assert arrs.my_slice([], 1, 1) == []
    assert arrs.my_slice([1, 2, 3, 2, 8], -6, -1) == [1, 2, 3, 2]
