from typing import ItemsView


class SimpleList:
    def __init__(self, items):
        self.__items = list(items)

    def add(self, item):
        self.__items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self.__items.sort()

    def __len__(self):
        return len(self.__items)
    def __repr__(self):

        return f'{type (self).__name__}({self.__items!r})'
                            
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)                    
        self.sort()