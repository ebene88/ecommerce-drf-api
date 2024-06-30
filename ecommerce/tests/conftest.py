from pytest_factoryboy import register
import pytest
from rest_framework.test import APIClient
from .factories import CategoryFactory, BrandFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)


@pytest.fixture
def api_client():
    return APIClient
