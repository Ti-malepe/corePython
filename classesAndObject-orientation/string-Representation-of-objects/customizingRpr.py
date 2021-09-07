class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out range")    

        self.latitude = latitude
        self.longitude = longitude


    @property
    def latitude(self):
        return self._latitude

    @property 
    def longitude(self):
        return self._longitude    

    def __repr__(self):
        return f"position{type(self)}(latitude={self.latitude}, longitude={self.longitude})"            
class EarthPosition(Position):
    pass
class MarsPosition(Position):
     pass    
def typename(obj):
    return type(obj).__name__