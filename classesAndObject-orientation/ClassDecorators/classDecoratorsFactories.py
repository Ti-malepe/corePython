from typing_extensions import runtime


class Itinerary:
    @classmethod
    def from_location(cls, *locations):
        return cls (locations)

    def __init__(self, locations):
        self._location = list(locations)    

    def __str__(self):
        return "\n".join(location.name for location in self._locations)    

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    def add(self, location):
        self._location.append(location)

    def remove(self, name):
        removal_indexes = [index for index, location in enumerate(self._locations)
                      if location.name == name
            ]        
        for index in reversed(removal_indexes):
            del self._location[index]

    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._location ):
            if location.name == name:
                stop = index + 1
        self._location = self._location[:stop]

    def postcondition(predicate):

        def function_decorators(f):   

            # @functools.wraps(f)
            def wrapper(self, *args, **kwargs):
                results = f(self, *args, **kwargs)
                if not predicate(self):
                    raise RuntimeError(
                        f"post-condition {predicate.__name__}not"
                        f"maintained for{self!r}"
                    )
                return results
            return wrapper
        return function_decorators

