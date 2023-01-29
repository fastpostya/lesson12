import pytest
from utils.arrs import get, my_slice


@pytest.fixture
def coll_get1():
    return ([1, 2, 3], 1, "test")

    # assert arrs.get([], 0,"test") == "test"
    # assert arrs.get([], -1, "test") == "test"
    # assert arrs.get([], -1) == None



def test_get(coll_get1):
    assert get(coll_get1) == 2



