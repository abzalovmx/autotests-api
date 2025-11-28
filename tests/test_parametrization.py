import pytest
from _pytest.fixtures import SubRequest


def test_number_1():
    assert 1 > 0


def test_number_2():
    assert 2 > 0


def test_number_3():
    assert 3 > 0


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", ((1, 1), (2, 4), (3, 9)))
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ("macos", "linux", "windows", "debian"))
@pytest.mark.parametrize("host", ("localhost", "dev", "stable", "prod"))
def test_multiplication_of_numbers(os, host):
    assert True


@pytest.fixture(params=("localhost", "dev", "stable", "prod"))
def host(request: SubRequest) -> str:
    return request.param


def test_hosts(host: str):
    print(f"Running test on: {host}")


@pytest.mark.parametrize("user", ("Alice", "Bob"))
class TestOperations:
    def test_user_with_operation(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operation(self, user: str):
        print(f"User without operations: {user}")


users = {
    "+99800000": "Ali",
    "+99899077": "Vali",
    "+99899011": "Toshmat"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass
