class ShippingContainer:
    
    next_serial = 1337
    
    @classmethod
    def _generate_serial(cls):
        results = cls.next_serial
        cls.next_serial += 1
        return results
    # @staticmethod
    # def _make_bic_code(owner_code, serial):
    #     return iso6346.create(
    #         owner_code = owner_code,
    #         serial = str(serial).zfill(6)
    #     )    
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))
    

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

    