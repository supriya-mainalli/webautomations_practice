import pytest

@pytest.fixture(scope="class")
def setup():
    print("This is class setup")
    yield
    print("This is class teardown")

@pytest.mark.usefixtures("setup")
class TestClassFixture:
    def test_a(self):
        print("This is A")

    def test_b(self):
        print("This is B")