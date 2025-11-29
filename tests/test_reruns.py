import random
import pytest


PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert random.choice([False, True])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([False, True])

    def test_rerun_2(self):
        assert random.choice([False, True])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([False, True])
