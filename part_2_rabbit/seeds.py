import random
from faker import Faker
from typing import List

from src.models import User

def seed_users(n: int = 20) -> List[User]:
    users = []
    for _ in range(n):
        users.append(
            User(
                fullname = fake.name(),
                email = fake.email()
            )
        )
    return users