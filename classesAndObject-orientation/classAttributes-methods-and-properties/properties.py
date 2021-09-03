class ShippingContainer:
    
 @classmethod
 def create_empty(cls, owner_code, **kwargs):
    return cls(owner_code, contents=[], **kwargs)

@classmethod
def create_with_items(cls, owner_code, items):
    return cls(owner_code, contents=list(items))

@property 
def celsius(self):
    return self._celsius



# def __init__(self, owner_code, contents):
#     self.owner_code = owner_code
#     self.contents = contents
#     self.bic = self.make_bic_code(owner_code = owner_code,
#                                  serial=ShippingContainer._generate_serial())

class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too damn hot!!!")
            self.celsius = celsius
@celsius.setter

def celsius(self, value):
      if value > RefrigeratedShippingContainer.MAX_CELSIUS:
          raise ValueError("Temperature Too damn high!!!")           
      self._celsius = value 

@staticmethod
def _f_to_c(celsius):
    return celsius * 9/5 + 32
    
@staticmethod
def _c_to_f(fahrenheit):
    return (fahrenheit - 32) * 5/9

    