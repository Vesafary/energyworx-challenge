import json
from django.test import Client, RequestFactory, TestCase

from application.core.models import ShortUrl
from application.core.views import CreateView, ResolveView
from tests.mixins.views import ViewsMixin


class StatsTestCase(ViewsMixin, TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_shortcode(self):
        self.create_url()
        for _ in range(5):
            self.retrieve_url()

        response = self.client.get("/abc_12/stats")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("redirectCount"), 5)
        # TODO: Use freezegun to fix datetime for accurate tests
        self.assertIn("created", response.json())
        self.assertIn("lastRedirect", response.json())

    def test_invalid_shortcode(self):
        response = self.client.get("/abcdef")
        self.assertEqual(response.status_code, 404)
