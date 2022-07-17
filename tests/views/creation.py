import json
from django.test import Client, TestCase

from application.core.views import CreateView


class CreationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_without_shortcode(self):
        body = {
            "url": "http://www.energyworx.com"
        }

        response = self.client.post("/shorten", body, content_type='application/json')
        self.assertEqual(len(response.json().get("shortcode")), 6)
        self.assertEqual(response.status_code, 201)

    def test_with_shortcode(self):
        body = {
            "url": "http://www.energyworx.com",
            "shortcode": "abc_12"
        }

        response = self.client.post("/shorten", body, content_type='application/json')
        self.assertEqual(response.json().get("shortcode"), "abc_12")
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_shortcode(self):
        cases = [
            "abc_1",
            "abc_123",
            "abc!23",
        ]

        for case in cases:
            body = {
                "url": "http://www.energyworx.com",
                "shortcode": case
            }

            response = self.client.post("/shorten", body, content_type='application/json')
            self.assertEqual(response.status_code, 412)
    
    def test_duplicate_shortcode(self):
        body = {
            "url": "http://www.energyworx.com",
            "shortcode": "abc_12"
        }

        response = self.client.post("/shorten", body, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post("/shorten", body, content_type='application/json')
        self.assertEqual(response.status_code, 409)
