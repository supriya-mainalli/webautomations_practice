import pytest

from pytest_practice.conftest import setup


@pytest.mark.usefixtures("setup")
class TestDemo002:
    def test_001(self):
        print(f"I will be test 001")

    def test_002(self):
        print(f"I will be test 002")

    def test_003(self):
        print(f"I will be test 003")