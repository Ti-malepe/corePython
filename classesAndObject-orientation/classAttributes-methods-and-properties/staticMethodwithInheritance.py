class RefriratedShippingContainer(shippingContainer):
  @staticmethod
  def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6)
            category="R"

        )