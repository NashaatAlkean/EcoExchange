from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from .form import RegisterUserForm
from unittest import mock
from django.test import RequestFactory
from unittest.mock import patch
from users.views import logout_user

User = get_user_model()

class SeekerRegistrationTestCase(TestCase):
    def test_register_seeker_get(self):
        response = self.client.get(reverse('register-seeker'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterUserForm)

    def test_register_seeker_post_success(self):
        self.assertEqual(User.objects.count(), 0)
         
         # Example for test_register_seeker_post_success, include all necessary fields
        response = self.client.post(reverse('register-seeker'), {
         'email': 'seeker@example.com',
         'password1': 'testpass123',  # Assuming the form splits password
         'password2': 'testpass123',  # Confirm password field
    # Include other mandatory fields your form expects
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

def test_register_donor_get(self):
    """
    בדיקת שיטת GET
    """
    response = self.client.get('/register-donor/')
    self.assertEqual(response.status_code, 200) #1
    self.assertTemplateUsed(response, 'users/register_donor.html') 
        
def test_register_donor_invalid_form(self):
    """
    בדיקת טופס לא תקין
    """
    data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
    response = self.client.post('/register-donor/', data=data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/register-donor/')
    self.assertContains(response, 'something went wrong')
def test_register_donor_save_error(self):
    """
    בדיקת יצירת משתמש עם שגיאה
    """
    # הדמיית שגיאה בעת שמירת משתמש
    def mock_save(self, *args, **kwargs):
        raise Exception('Save error')

    with mock.patch.object(User, 'save', mock_save):
        data = {'username': 'test_user', 'email': 'test@example.com',
                'password1': 'password123', 'password2': 'password123'}
        response = self.client.post('/register-donor/', data=data)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/register-donor/')
    self.assertContains(response, 'something went wrong')

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

# class LogoutUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_logout_user1(self):
        # Create a request instance
        request = self.factory.get('/logout/')

        # Patch the logout function with a mock
        with patch('myapp.views.logout') as mock_logout:
            # Call the logout_user function
            response = logout_user(request)

            # Check that the logout function is called with the correct arguments
            mock_logout.assert_called_once_with(request)

        # Check that the correct message is added to the request
        messages = get_messages(request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'your session has ended')

    def test_invalid_logout_request(self):
        # Make an invalid logout request (when user is not logged in)
        response = self.client.get('/logout/')

    # Assert the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')
        self.assertNotIn('_auth_user_id', self.client.session)
        
class LogoutUserTestCase(TestCase):
    def test_logout_user_clears_session(self):
        # Create a user and log them in
        user = User.objects.create(username='testuser')
        self.client.force_login(user)

        # Set some session data
        self.client.session['key1'] = 'value1'
        self.client.session['key2'] = 'value2'