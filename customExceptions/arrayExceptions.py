class ArrayInvalidSize(Exception):
    def __init__(self, *args: object, msg: str = "Invalid Array Size") -> None:
        super().__init__(*args, msg)

raise ArrayInvalidSize;