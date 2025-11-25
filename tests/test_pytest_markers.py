import pytest


# @pytest.mark.smoke
# def test_smoke_case():
#     assert 1 + 1 == 2
#
#
# @pytest.mark.regression
# def test_regression_case():
#     assert 2 * 2 == 4


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass
