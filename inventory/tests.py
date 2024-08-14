from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()
class ProductTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testemail@mail.com",username="testuser", password="password")
        self.product = Product.objects.create(web_id="12", slug="Test-Content", name="Fake Product")

    def test_post_creation(self):
        product = Product.objects.get(web_id="12")
        self.assertEqual(product.slug, "Test-Content")
