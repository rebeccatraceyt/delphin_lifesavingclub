from django.test import TestCase
from .models import (
    SwimCategory,
    SwimProgramme,
    FAQ,
)

# ------ Swim Categories ------


class TestSwimCategoryModel(TestCase):
    """Test Swim Category Model"""

    def test_swim_category_model(self):
        # Create Test Swim Category
        swim_category = SwimCategory(name='Test Swim Category')

        # Save Test Category
        swim_category.save()

        # check that Field == Value
        self.assertEqual(swim_category.name, "Test Swim Category")

    def test_swim_category_as_string(self):
        swim_category = SwimCategory(name='test')
        swim_category.save()
        self.assertEqual('test', str(swim_category))


# ------ Swim Programme ------


class TestSwimProgrammeModel(TestCase):
    """Test Swim Programme Model"""

    def test_swim_programme_model(self):
        # Create Test Category
        category = SwimCategory(name='Test Swim Category')

        # Create Test Programme
        swim_programme = SwimProgramme(name='Test Programme',
                                       description='Test desc',
                                       age='10 years',)

        # Save Test Programme
        swim_programme.category_id = category.id
        swim_programme.save()

        # check that Field == Value
        self.assertEqual(swim_programme.name, "Test Programme")
        self.assertEqual(swim_programme.description, "Test desc")
        self.assertEqual(swim_programme.age, "10 years")
        self.assertEqual(swim_programme.category_id, category.id)


# ------ FAQs ------


class TestFAQModel(TestCase):
    """Test FAQs Model"""

    def test_faq_model(self):
        # Create Test FAQ
        faq = FAQ(question='Test Question',
                  answer='Test Answer',)

        # Save Test FAQ
        faq.save()

        # check that Field == Value
        self.assertEqual(faq.question, "Test Question")
        self.assertEqual(faq.answer, "Test Answer")
