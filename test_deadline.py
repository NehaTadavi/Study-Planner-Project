
from datetime import date, timedelta
from deadline import check_deadline


def test_past_deadline():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    assert check_deadline(yesterday) == "Overdue"


def test_today_deadline():
    today = date.today().isoformat()
    assert check_deadline(today) == "Due Today"


def test_future_deadline():
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    assert check_deadline(tomorrow) == "Upcoming"
