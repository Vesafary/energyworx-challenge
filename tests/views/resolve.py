import json
from django.test import Client, RequestFactory, TestCase

from application.core.models import ShortUrl
from application.core.views import CreateView, ResolveView
from tests.mixins.views import ViewsMixin


class ResolveTestCase(ViewsMixin, TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_shortcode(self):
        self.create_url()

        response = self.client.get("/abc_12")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get("Location"), "http://www.energyworx.com")

    def test_invalid_shortcode(self):
        response = self.client.get("/abcdef")
        self.assertEqual(response.status_code, 404)
