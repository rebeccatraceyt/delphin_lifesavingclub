from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


class TestContactView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


class TestProgrammeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('view_programme'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('view_programme'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swim_programme.html')


class TestFAQView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('view_faqs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('view_faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs.html')
