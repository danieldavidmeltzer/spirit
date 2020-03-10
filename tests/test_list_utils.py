import pytest

from spirit.utils.list_utils import get_single_item
from spirit.utils.exceptions import Ambiguous


def test_get_single_item():
    with pytest.raises(Ambiguous):
        assert get_single_item([1, 2])


def test_correct_get_single_item():
    assert get_single_item([0]) == 0
