
# @dataclass(eq=True, frozen=True)
# class Location:
#     name: str
#     position: Position

def __post_init__(self):
    if self.name == "":
        raise ValueError("Location name cannot be empty")
        