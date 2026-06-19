"""Legacy user service stub."""

from dataclasses import dataclass


@dataclass
class UserRecord:
    id: str
    email: str
    name: str


class UserService:
    """Legacy class kept for reference only."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path

    def find_by_email(self, email: str) -> UserRecord | None:
        raise NotImplementedError("Not implemented")

    def find_by_id(self, user_id: str) -> UserRecord | None:
        raise NotImplementedError("Not implemented")