def fizz_buzz(number):
    
    _validate_integer(number, "number")

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


def fizz_buzz_range(start=1, end=100):
    _validate_integer(start, "start")
    _validate_integer(end, "end")
    if start > end:
        raise ValueError("start must not be greater than end")

    return [fizz_buzz(number) for number in range(start, end + 1)]


def _validate_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")