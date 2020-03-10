import pytest
import os
from spirit.reader.reader import Reader


@pytest.fixture
def reader():
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    # result has at least 2 snapshots and maybe more bytes
    path_to_file = os.path.join(current_directory, "result.mind.gz")
    return Reader(path_to_file)


def test_user_data(reader):
    assert reader.user_id == 42
    assert reader.gender == 0


def test_snapshot_data(reader):
    snapshot = reader._read_next_snapshot()
    assert snapshot.feelings.exhaustion == 0
    assert snapshot.color_image[4][5][2] == 99

