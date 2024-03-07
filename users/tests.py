from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from .form import RegisterUserForm

User = get_user_model()

class SeekerRegistrationTestCase(TestCase):
    def test_register_seeker_get(self):
        response = self.client.get(reverse('register-seeker'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterUserForm)

    def test_register_seeker_post_success(self):
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(reverse('register-seeker'), {
            'email': 'seeker@example.com',
            'password': 'testpass123',
            # Include other fields your form may require
        })
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertTrue(user.is_seeker)
        self.assertEqual(user.username, user.email)
        self.assertRedirects(response, reverse('login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('Your account has been created', str(messages[0]))

    def test_register_seeker_post_fail(self):
        response = self.client.post(reverse('register-seeker'), {})
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertEqual(User.objects.count(), 0)

class DonorRegistrationTestCase(TestCase):

    def test_register_donor_get(self):
        response = self.client.get(reverse('register-donor'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterUserForm)

    def test_register_donor_post_success(self):
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(reverse('register-donor'), {
            'email': 'donor@example.com',
            'password1': 'testpass123',  # Assuming you are using a form that splits password into two fields
            'password2': 'testpass123',
            # Include other fields your form may require
        })
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertTrue(user.is_donor)
        self.assertEqual(user.username, user.email)
        self.assertRedirects(response, reverse('login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('Your account has been created, please login', str(messages[0]))

    def test_register_donor_post_fail(self):
        response = self.client.post(reverse('register-donor'), {
            # Submit form with missing or invalid data
            'email': 'donor@example.com',  # Missing password fields for instance
        })
        self.assertFormError(response, 'form', 'password1', 'This field is required.')  # Assuming password validation
        self.assertEqual(User.objects.count(), 0)
