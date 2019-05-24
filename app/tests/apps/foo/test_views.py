# third-party imports
from django.test import TestCase as DjangoTestCase
from rest_framework.test import APIClient


class FooViewTestCase(DjangoTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_verify_with_get_request(self):
        url = "/foo"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
