import pytest

@pytest.mark.smoke
def test_first_pgm():
    print(f"this is first pgm")

# @pytest.mark.xfail
def test_credcard1():
    print(f"pattern test runner1")

# @pytest.mark.skip
def test_credcard2():
    print(f"pattern test runner2")


