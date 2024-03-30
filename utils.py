def validate_positive_number(number: [int, float]):
    if isinstance(number, (int, float)) and number > 0:
        return
    else:
        raise InvalidArgumentError(number, "Invalid Argument")

    # valid_type = isinstance(number, (float, int)) #and not isinstance(number, bool)
    #
    # if not valid_type:
    #     raise InvalidArgumentError(number, f"Invalid Type: Accepted types are {int}, {float}")
    #
    # if number < 0:
    #     raise InvalidArgumentError(number, "Number must be positive")


def validate_non_empty_string(string: str):
    valid_type = isinstance(string, str)

    if not valid_type:
        raise InvalidArgumentError(string, f"Invalid Type: Accepted types are {type(string)}")

    if string == "":
        raise InvalidArgumentError(string, "String must not be empty")


class InvalidArgumentError(Exception):
    def __init__(self, arg, msg):
        super().__init__(
                f'The `{arg}` (type `{type(arg)}`) is invalid. {msg}')


