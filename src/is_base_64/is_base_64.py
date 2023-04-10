from base64 import b64decode


def is_base_64(value: str) -> bool:
    try:
        b64decode(value, validate=True)
        return True
    except:
        return False
