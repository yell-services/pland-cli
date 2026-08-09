import pytest

from pland_cli._codegen.security import classify, draftable_for


@pytest.mark.parametrize("method,path,tag,expected", [
    # critical
    ("delete", "/salaries/{id}", "Salary", "critical"),
    ("post", "/salaries/releaseWithJob", "Salary", "critical"),
    ("post", "/timetracking/{id}/cancel", "Time Tracking", "critical"),
    ("delete", "/users/{id}", "Users", "critical"),
    ("post", "/users/{id}/generatePassword", "Users", "critical"),
    ("post", "/users/{id}/setEndDateForUserAndAllJobsOfUser", "Users", "critical"),
    ("delete", "/notification/v2/deleteAll", "Push Notifications", "critical"),
    ("post", "/tasks/delete", "Tasks", "critical"),
    ("delete", "/api_key/{keyId}", "API Keys", "critical"),
    ("post", "/account/change-password", "Authentication", "critical"),
    ("post", "/invoices/setToCanceled", "Invoice", "critical"),
    ("delete", "/documents/{id}", "Documents", "critical"),
    ("patch", "/documents/{id}", "Documents", "critical"),
    # confirm
    ("delete", "/absences/{id}", "Absences", "confirm"),
    ("patch", "/customers/{id}", "Customers", "confirm"),
    ("post", "/offers/send", "Offers", "confirm"),
    ("post", "/invoices/setFixed", "Invoice", "confirm"),
    ("patch", "/users/many", "Users", "confirm"),
    ("delete", "/payTypes/{id}", "Pay Types", "confirm"),
    # free
    ("post", "/invoices/", "Invoice", "free"),
    ("post", "/offers/preview", "Offers", "free"),
    ("delete", "/taxRates/{id}", "Tax Rates", "free"),
    ("post", "/timetracking/start", "Time Tracking", "free"),
    ("post", "/notification/v2/read", "Push Notifications", "free"),
    ("post", "/auth/login", "Authentication", "free"),
    ("post", "/salaries/objectExport", "Salary", "free"),
])
def test_classify(method, path, tag, expected):
    assert classify(method, path, tag) == expected

def test_draftable_only_for_draftable_deletes():
    assert draftable_for("delete", "/invoices/{id}", "Invoice") == "Invoice"
    assert draftable_for("delete", "/offers/{id}", "Offers") == "Offers"
    assert draftable_for("patch", "/invoices/{id}", "Invoice") is None
    assert draftable_for("delete", "/users/{id}", "Users") is None
