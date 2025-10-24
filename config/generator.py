import random
import string
from datetime import datetime

def generate_unique_email():
    """Генерация уникального email для тестов"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"test_{timestamp}_{random_str}@test.com"