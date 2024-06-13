class BadRequestException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnauthorizedException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
