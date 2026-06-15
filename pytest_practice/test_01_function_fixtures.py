import pytest

@pytest.fixture()
def setup():
    print("This is function setup")
    return "pass"
    # yield
    # print("This is function teardown")

def test_a(setup):
    print("A")
    assert setup == "pass"

def test_b(setup):
    print("B")