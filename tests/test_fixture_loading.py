from tests.conftest import load_fixture


def test_salary_fixture_loads():
    data = load_fixture("salaries_object.json")
    assert isinstance(data, list)
    assert data[0]["_id"] == "s1"
    assert data[0]["user"]["general"]["firstName"] == "***"
