from django.test import TestCase, Client


class TestAllowedHosts(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_allowed_hosts(self):
        """Test allowed hosts in settings."""
        response = self.client.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/', HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)
