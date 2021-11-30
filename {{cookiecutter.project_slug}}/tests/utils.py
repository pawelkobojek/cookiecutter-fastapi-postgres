import random
import string

def random_string() -> str:
    return "".join(random.choices(string.ascii_letters, k=random.randint(1, 33)))
