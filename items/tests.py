from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Items
from django.contrib.auth import get_user_model  # Import get_user_model
from .form import DonateItemForm 


User = get_user_model()  # Get the custom user model
class ItemViewsTestCase(TestCase):
    def setUp(self):
        # Create a user. Adjust this part if 'is_donor' is managed differently in your application.
        self.user = User.objects.create_user(username='donor', email='donor@example.com', password='password')
        # If 'is_donor' is an attribute of a user profile or a custom user model, ensure it's set properly here.
        # Example for a custom user model or user profile:
        # self.user.profile.is_donor = True
        # self.user.profile.save()

        self.client.login(username='donor', password='password')

        # Create an item for update tests.
        self.item = Items.objects.create(title="Sample Item", user=self.user)

    def test_create_item_view_get(self):
        response = self.client.get(reverse('create-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/create_ad.html')

    def test_create_item_view_post_success(self):
        form_data = {'title': 'New Item', 'description': 'Description of the new item'}
        response = self.client.post(reverse('create-add'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Items.objects.filter(title='New Item').exists())
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('New item has been published..', messages)

    def test_create_item_view_post_failure(self):
        form_data = {}  # Insufficient data
        response = self.client.post(reverse('create-add'), form_data)
        self.assertEqual(response.status_code, 302)  # Assuming redirect on failure
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('something went wrong', messages)  # Adjust based on your actual error message

    def test_update_item_view_get(self):
        response = self.client.get(reverse('update_ad', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/update_ad.html')

    def test_update_item_view_post_success(self):
        form_data = {'title': 'Updated Item', 'description': 'Updated description'}
        response = self.client.post(reverse('update_ad', kwargs={'pk': self.item.pk}), form_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, 'Updated Item')
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Your items info has updated.', messages)



class CreateItemTestCase_AI(TestCase):
    def test_valid_form_submission(self):
        # Simulate a valid form submission
        form_data = {
            'user': 'your_user',  # Replace with an actual user
            'title': 'Test Item',
            'description': 'This is a test item description.',
            # Add other form fields as needed
        }
        response = self.client.post('/create-item/', data=form_data)
        self.assertEqual(response.status_code, 302)  # Check if it redirects
        # Add more assertions to verify the expected behavior

class CreateItemTestCase(TestCase):
    def test_invalid_form_submission(self):
        # Simulate an invalid form submission
        form_data = {
            'user': 'your_user',  # Replace with an actual user
            'title': '',  # Empty title
            'description': 'This is an invalid test item description.',
            # Add other form fields as needed
        }
        response = self.client.post('/create-item/', data=form_data)
        self.assertEqual(response.status_code, 200)  # Check if it stays on the same page
        # Add more assertions to verify error messages or other behavior

class CreateItemTestCase(TestCase):
    def test_non_donor_user(self):
        # Simulate a non-donor user
        response = self.client.get('/create-item/')
        self.assertEqual(response.status_code, 302)  # Check if it redirects
        # Add more assertions to verify the expected behavior


