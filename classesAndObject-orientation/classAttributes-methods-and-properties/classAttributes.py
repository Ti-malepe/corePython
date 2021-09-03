class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1         

class MyClass:

    b = "on class"

    def __init__(self):
        self.a = "on instance"
        print(self.a)
        print(MyClass.b)
        self.a = "re-bound"  
        