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
        
class LoginUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user@example.com', email='user@example.com', password='testpass123', is_active=True)

    def test_login_user_post_success(self):
        response = self.client.post(reverse('login'), {
            'email': 'user@example.com',
            'password': 'testpass123',
        })
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_user_post_fail(self):
        response = self.client.post(reverse('login'), {
            'email': 'user@example.com',
            'password': 'wrongpass',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        
        self.assertIn('something went wrong', str(messages[0]))
    def test_login_user_invalid_credentials(self):
    #בדיקת נתוני כניסה לא תקינים
        data = {'email': 'invalid@email.com', 'password': 'wrongpassword'}
        response = self.client.post('/login/', data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')
        self.assertContains(response, 'somthing went wrong')
    def test_login_user_inactive_user(self): 
    #בדיקת נתוני כניסה תקינים, משתמש לא פעיל
        user = User.objects.create_user('test_user', 'test@example.com', 'password123')
        user.is_active = False
        user.save()
        
        
    def test_login_user_valid_credentials(self):
    
    #בדיקת נתוני כניסה תקינים, הפניה לדף ראשי
    
      user = User.objects.create_user('test_user', 'test@example.com', 'password123')
      data = {'email': 'test@example.com', 'password': 'password123'}
      response = self.client.post('/login/', data=data)
      self.assertEqual(response.status_code, 302)
      self.assertRedirects(response, '/dashboard/')

    # בדיקת כניסת המשתמש
      self.assertTrue(self.client.login(username='test_user', password='password123'))



class LogoutUserTestCase(TestCase):
    def test_logout_user(self):
        self.client.login(username='user@example.com', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('your session has ended', str(messages[0]))
