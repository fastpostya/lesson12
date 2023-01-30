import pytest
from utils.arrs import get, my_slice

@pytest.fixture
def coll_list():
    return [1, 2, 3]

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def text():
    return "test"

@pytest.fixture
def big_list():
    return [1, 2, 3, 2, 8]

@pytest.fixture
def little_list():
    return [1, 2, 3, 4]
def test_get(coll_list, empty_list, text):
    assert get(coll_list, 1, text) == 2
    assert get(empty_list, 0, text) == text
    assert get(empty_list, -1, text) == text
    assert get(empty_list, -5) is None

def test_slice(coll_list, empty_list, big_list, little_list):
    assert my_slice(little_list, 1, 3) == [2, 3]
    assert my_slice(coll_list, 1) == [2, 3]
    assert my_slice(big_list, 1, -1) == [2, 3, 2]
    assert my_slice(big_list, -3, -1) == [3, 2]
    assert my_slice(coll_list, 4, 6) == empty_list
    assert my_slice(little_list, 3, 1) == empty_list
    assert my_slice(empty_list, 1, 1) == empty_list
    assert my_slice(big_list, -6, -1) == [1, 2, 3, 2]



