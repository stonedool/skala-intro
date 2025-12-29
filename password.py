# password.py
import re

def is_valid_password(password: str) -> bool:
    """
    조건:
    - 최소 6자리
    - 알파벳 1개 이상
    - 숫자 1개 이상
    - 특수문자 1개 이상
    """
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{6,}$'
    return bool(re.match(pattern, password))
