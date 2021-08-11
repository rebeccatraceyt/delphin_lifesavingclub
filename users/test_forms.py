from django.test import TestCase
from .forms import ProfileForm


class TestProfileRegistrationForm(TestCase):
    """Test User Profile Form for registration """

    def test_a_valid_registration(self):
        """ Test User registration form """

        form = ProfileForm({'email': 'test@gmail.com',
                            'username': 'test',
                            'password1': '!Testpassword2',
                            'password2': '!Testpassword2', })
        self.assertTrue(form.is_valid())
