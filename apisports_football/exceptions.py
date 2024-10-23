class ApiError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ApiKeyTypeError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
