from uuid import UUID
from mongoengine.errors import ValidationError


def is_valid_uuid4(value: str) -> bool:
    try:
        UUID(value, version=4)
        return True
    except:
        return False
