import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be running first")
    yield
    print("I will be running at the last of all the testcases")

# @pytest.fixture(scope = "class")
@pytest.fixture()
def data_load():
    return ['supriya', 'mainalli']

@pytest.fixture()
def cross_browser():
    return [("chrome", "supriya"), ("Firefox"), ("IE")]