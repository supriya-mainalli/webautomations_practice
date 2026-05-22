import pytest

# @pytest.mark.usefixtures("data_load")
class TestDemo3:

    def test_func01(self, data_load):
        print(data_load)

    def test_cross_browser(self, cross_browser):
        for item in cross_browser:
            print(item)