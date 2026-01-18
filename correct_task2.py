# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
from typing import Iterable
import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email.strip()))

def count_valid_emails(emails: Iterable[str]) -> int:
    if not emails:
        return 0

    return sum(
        1 for email in emails
        if isinstance(email, str) and is_valid_email(email)
    )
