from datetime import date


def check_deadline(deadline_date):
    deadline = date.fromisoformat(deadline_date)
    today = date.today()

    if deadline < today:
        return "Overdue"
    elif deadline == today:
        return "Due Today"
    else:
        return "Upcoming"
