class Product:
    def __init__(self, name, brand, category, sku=None):

        self.name = name
        self.brand = brand
        self.category = category
        self.sku = sku

    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nome Inválido")

        self._name = value.strip()

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand (self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Marca Inválida")

        self._brand = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Categoria Inválida")

        self._category = value.strip()

    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("SKU Inválido")

        self._sku = value.strip() if value is not None else None

product = Product (
    name="Galaxy S25",
    brand="Samsung",
    category="Smartphone",
    sku="SAM-GS25-256"
)

product.name = "Galaxy S26"

print(product.name)
print("-------------------------------------")

try: 
    product.name = ""
except ValueError as error:
    print(f"Erro ao atualizar produto: {error}")


print(product.name)
print(product.brand)
print(product.category)
print(product.sku)