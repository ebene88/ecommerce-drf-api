import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        obj = category_factory()
        assert obj.__str__() == "category_8"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        obj = brand_factory()
        assert obj.__str__() == "brand_8"


class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory()
        assert obj.__str__() == "product_4"
