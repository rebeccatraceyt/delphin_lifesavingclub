from django.test import TestCase, Client


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
