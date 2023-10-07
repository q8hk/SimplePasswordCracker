import itertools
import random
from typing import Callable, Iterable, Optional

def generate_random_numerical_password(length: int) -> str:
    """Generate a random numerical password of the given length."""
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def guesses_generator(length: int) -> Iterable[str]:
    """Generate all possible numerical combinations of a given length."""
    yield from ("".join(digits) for digits in itertools.product("0123456789", repeat=length))

def crack_password(length: int, oracle: Callable[[str], bool]) -> Optional[str]:
    """Crack a password of the given length using the provided oracle function."""
    for guess in guesses_generator(length):
        if oracle(guess):
            return guess
    return None

if __name__ == "__main__":
    difficulty = 4  # Adjust the difficulty level here
    print(f"The difficulty (number of digits) is set to {difficulty}")
    
    password = generate_random_numerical_password(difficulty)
    print(f"The password to crack is {password!r}")
    
    password_oracle = lambda guess: guess == password  # Password oracle function
    if match := crack_password(difficulty, password_oracle):
        print("Cracked!")
    else:
        print("Error, not found")

