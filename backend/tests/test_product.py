import pytest
from app.catalog.product import Product


def test_product_without_name():
    with pytest.raises(ValueError):
        Product(
            name="",
            brand="Samsung",
            category="Smartphone"
        )


def test_create_product_successfully():
    product = Product(
        name="Galaxy S25",
        brand="Samsung",
        category="Smartphone",
        sku="SAM-GS25-256"
    )

    assert product.name == "Galaxy S25"
    assert product.brand == "Samsung"
    assert product.category == "Smartphone"
    assert product.sku == "SAM-GS25-256"


def test_create_product_without_sku():
    product = Product(
        name="Galaxy S25",
        brand="Samsung",
        category="Smartphone"
    )

    assert product.sku is None

def test_product_with_name_none():
    with pytest.raises(ValueError):
        Product(
            name=None,
            brand="Samsung",
            category="Smartphone"
        )


def test_product_with_numeric_sku():
    with pytest.raises(ValueError):
        Product(
            name="Galaxy S25",
            brand="Samsung",
            category="Smartphone",
            sku=12345
        )