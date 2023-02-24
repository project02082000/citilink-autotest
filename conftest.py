import pytest


@pytest.fixture(scope="module")
# @pytest.fixture(scope="function")
def set_up():
    print("\nTEST HAS BEEN STARTED\n")
    yield
    print("\nTEST HAS BEEN ENDED")