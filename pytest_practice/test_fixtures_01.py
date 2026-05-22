import pytest

@pytest.mark.usefixtures("setup")
class TestDemofixtures:

    def test_fixtures_firstpgm(self):
        print("I will be running after setups1")

    def test_fixtures_pgm2(self):
        print("I will be running after pgm2")

    def test_fixtures_pgm3(self):
        print("I will be running after pgm3")