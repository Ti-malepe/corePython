# import iso6346

class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # @staticmethod
    # def _make_bic_code(owner_code,serial):
    #     return iso6346.create(
    #         owner_code = owner_code,
    #         serial = str(serial).zfill(6)
    #     ) 

    @classmethod
    # def __init__(self,owner_code, length_ft, contents, **kwargs):
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code,length_ft, contents =[], **kwargs)
    @classmethod
    def create_with_items(cls, owner_code,length_ft, items, **kwargs):
        return cls(owner_code,length_ft, contents=list(items), **kwargs)

    def __init__(self,owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(owner_code=owner_code,
                                   serial = ShippingContainer._generate_serial())         
    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
      
