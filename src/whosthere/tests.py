from django.test import TestCase

class WhosThereTestCase(TestCase):

    def test_upload_page_returns_401(self):
        response = self.client.post('/update/')
        self.assertEqual(response.status_code, 401)
