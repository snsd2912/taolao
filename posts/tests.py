from django.test import TestCase
from django.template.defaultfilters import slugify
from posts.models import Post


class ModelsTestCase(TestCase):
    def test_post_has_slug(self):
        """Posts are given slugs correctly when saving"""
        post = Post.objects.create(name="My first post")

        post.content = "John Doe"
        post.save()
        self.assertEqual(post.slug, slugify(post.name))
