"""is_base_64 package."""
from base64 import b64decode


def is_base_64(value: str) -> bool:
    """Check if a string is base64 encoded."""
    try:
        b64decode(value, validate=True)
        return True
    # pylint: disable=bare-except
    except:
        return False
