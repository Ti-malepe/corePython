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
    
    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"
    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"    


    def __repr__(self):
        return f"position{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"            

    def __str__(self):
         return (
             f"{abs(self.latitude)} {self.latitude_hemisphere},"
            f"{abs(self.longitude_hemisphere)} {self.longitude}"            
         )
    
    def __format__(self, format_spec):
        components_format_spec = ".2f"
        prefix, dot, suffix, = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            components_format_spec = f".{num_decimal_places}f"  
         
        latitude = format(abs(self.latitude), components_format_spec)
        longitude = format(abs(self.longitude), components_format_spec)
        return (
             f"{abs(self.latitude)} {self.latitude_hemisphere},"
            f"{abs(self.longitude_hemisphere)} {self.longitude}"            
         )


class EarthPosition(Position):
    pass
class MarsPosition(Position):
     pass    
def typename(obj):
    return type(obj).__name__