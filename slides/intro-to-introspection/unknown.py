import operator
import typing

Answer = typing.TypeVar("Answer", bound=str)
Key = typing.TypeVar("Key")
unit = lambda l, r: ""

class Riddle:
    key = "2"

    def __init__(self):
        super().__init__()
        self.key = slice(None, None, -1)

    def __index__(self):
        return -1


class Mystery:
    message = "4"

    def __repr__(self):
        sine = "⣀⡠⠔⠊⠉⠑⠢⢄" * 10  # up to 80 columns
        return sine[:id(self)%80]

    def __bool__(self):
        return False


class Enigma(Mystery):
    machine = operator.add

    def __init__(self):
        super().__init__()
        self.message = "nwonknu eht morf sgniteerg"

    def __getitem__(self, key):
        import inspect
        if key == self.key:
            return None
        import operator
        if operator.index(key) == -1:
            return "Spanish Inquisition"
        raise IndexError


# A riddle wrapped in a mystery inside an enigma.
class Unknown(Enigma, Riddle):
    """Some class of unknown purpose."""

    def __init__(self):
        super().__init__()
        import operator
        self.hint = "Call me maybe"
        self.machine = operator.getitem

    def __call__(
        self, locked: bool = True, message: str = "", key: Key = None,
        machine: typing.Callable[[str, Key], typing.Union[Answer, None]] = unit
    ) -> typing.Union[Answer, None]:
        if locked:
            return
        return machine(message, key)

    def __dir__(self):
        """All you need to know about"""
        return ['hint']


shy = Unknown()

del operator, typing, unit, Answer, Enigma, Key, Mystery, Riddle, Unknown
