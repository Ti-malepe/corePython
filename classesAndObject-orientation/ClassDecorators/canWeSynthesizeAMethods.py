class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self.name    

    @property
    def position(self):
        return self._position

#     def __repr__(self):
#         return f"{typename(self)(name={self.name}, position={self.position})}"    

#     def __str__(self):
#         return self.name    

# hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
# stockholm = Location("stockholm", EarthPosition(59.33, 18.06))
# rotterdam = Location("rotterdam", EarthPosition(51.96, 4.47))
# maracaibo = Location("maracaibo", EarthPosition(10.65, -71.65))
# cape_town = Location("cape_town", EarthPosition(-33.93, 18.42))