import pytest
import pytest_rerunfailures

@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True, False])