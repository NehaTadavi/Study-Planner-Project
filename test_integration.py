
from assignment import validate_assignment
from deadline import check_deadline


def test_valid_assignment_with_upcoming_deadline():
    assert validate_assignment("OS Assignment", "Operating Systems") is True
    assert check_deadline("2099-12-31") == "Upcoming"


def test_invalid_assignment_with_upcoming_deadline():
    assert validate_assignment("", "Operating Systems") is False
    assert check_deadline("2099-12-31") == "Upcoming"


def test_valid_assignment_with_overdue_deadline():
    assert validate_assignment("DBMS Assignment", "DBMS") is True
    assert check_deadline("2000-01-01") == "Overdue"
