import random
import string
from datetime import datetime, timedelta


def generate_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date


def generate_future_date():
    future_date = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
    return future_date


def generate_past_date():
    past_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
    return past_date


def generate_random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choices(letters, k=length))


def generate_random_integer(min_value=1, max_value=500):
    return random.randint(min_value, max_value)
