from assignment import validate_assignment


def test_valid_assignment():
    assert validate_assignment("OS Assignment", "Operating Systems") is True


def test_empty_title():
    assert validate_assignment("", "Operating Systems") is False


def test_empty_subject():
    assert validate_assignment("OS Assignment", "") is False
