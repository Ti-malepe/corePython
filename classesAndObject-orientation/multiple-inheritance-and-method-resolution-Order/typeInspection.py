from Simple_List import SimpleList

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError('IntList only support integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)
                    