from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = BlogPost.objects.create(title="Test Post", content="Test Content", author=self.user)

    def test_post_creation(self):
        post = BlogPost.objects.get(title="Test Post")
        self.assertEqual(post.content, "Test Content")
