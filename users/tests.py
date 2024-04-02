from django.http import HttpResponseRedirect
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from .views import register_seeker,register_donor,login_user, update_user, user_list, delete_users
from django.test import RequestFactory
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage


User = get_user_model()

# class RegisterSeekerTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_register_seeker_post_valid(self):
#         request = self.factory.post(reverse('register-seeker'), {
#             'email': 'testuser@example.com',
#             'password1': 'testpassword',
#             'password2': 'testpassword',
            
#             'full_name': 'Test User',
#             'address': 'Test Address',
#             'mobile': '1234567890',
#             'bio': 'This is a test bio.',
#         })
#         request.session = {}
#         setattr(request, 'session', 'session')
#         messages = FallbackStorage(request)
#         setattr(request, '_messages', messages)
#         response = register_seeker(request)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertEqual(response.url, reverse('login'))  # Redirects to login page
#         # Check if success message is set
#         storage = get_messages(request)
#         self.assertEqual(list(storage)[0].message, 'Your account has been created...')
#         # Check if user and profile are created
#         self.assertTrue(get_user_model().objects.filter(email='testuser@example.com').exists())
#         self.assertTrue(Profile.objects.filter(user__email='testuser@example.com').exists())
  
#     def test_register_seeker_post_invalid(self):
#         request = self.factory.post(reverse('register-seeker'), {
#             # Missing or invalid form data
#         })
#         request.session = {}
#         setattr(request, 'session', 'session')
#         messages = FallbackStorage(request)
#         setattr(request, '_messages', messages)
#         response = register_seeker(request)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertEqual(response.url, reverse('register-seeker'))  # Redirects back to registration page
#         # Check if warning message is set
#         storage = get_messages(request)
#         self.assertEqual(list(storage)[0].message, 'something went wrong')

#     def test_register_seeker_get(self):
#         # Use test client to perform a GET request
#         response = self.client.get(reverse('register-seeker'))
#         self.assertEqual(response.status_code, 200)  # Successful GET request
#         self.assertTemplateUsed(response, 'users/register_seeker.html')  # Correct template used





# class RegisterDonorTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_register_donor_post_valid(self):
#         request = self.factory.post(reverse('register-donor'), {
#             'email': 'testuser@example.com',
#             'password1': 'testpassword',
#             'password2': 'testpassword',

#             'full_name': 'Test User',
#             'address': 'Test Address',
#             'mobile': '1234567890',
#             'bio': 'This is a test bio.',

#         })
#         request.session = {}
#         setattr(request, 'session', 'session')
#         messages = FallbackStorage(request)
#         setattr(request, '_messages', messages)
#         response = register_donor(request)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertEqual(response.url, reverse('login'))  # Redirects to login page
#         # Check if success message is set
#         storage = get_messages(request)
#         self.assertEqual(list(storage)[0].message, 'Your account has been created, please login')
#         # Check if user and profile are created
#         self.assertTrue(get_user_model().objects.filter(email='testuser@example.com').exists())

#     def test_register_donor_post_invalid(self):
#         request = self.factory.post(reverse('register-donor'), {
#             # Missing or invalid form data
#         })
#         request.session = {}
#         setattr(request, 'session', 'session')
#         messages = FallbackStorage(request)
#         setattr(request, '_messages', messages)
#         response = register_donor(request)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertEqual(response.url, reverse('register-donor'))  # Redirects back to registration page
#         # Check if warning message is set
#         storage = get_messages(request)
#         self.assertEqual(list(storage)[0].message, 'Something went wrong')

#     def test_register_donor_get(self):
#         # Use test client to perform a GET request
#         response = self.client.get(reverse('register-donor'))
#         self.assertEqual(response.status_code, 200)  # Successful GET request
#         self.assertTemplateUsed(response, 'users/register_donor.html')  # Correct template used


# class LoginUserTestCase(TestCase):
#     def setUp(self):
#         self.username = 'testuser'
#         self.password = 'testpassword'
#         self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

#     def test_login_user_post_valid(self):
#         # Use create_user method to create a user
#         user = User.objects.create_user(
#             username='testuser@example.com',
#             email='testuser@example.com',
#             password='testpassword')

#         # Use self.client.post for POST request
#         response = self.client.post(reverse('login'), {
#             'email': 'testuser@example.com',
#             'password': 'testpassword',
#         })
#         self.assertEqual(response.url, reverse('home'))  # Redirects to home page


#     def test_login_user_post_invalid(self):
#         # Simulate a POST request to the login view with invalid credentials
#         response = self.client.post(reverse('login'),
#                                      {'email': 'test@example.com', 'password': 'wrongpassword'})
        
#         # Ensure that the redirection goes to the login page
#         self.assertEqual(response.url, reverse('login'))

#         # Ensure that the user is not logged in
#         self.assertFalse('_auth_user_id' in self.client.session)




# class LogoutUserTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser',
#                                               email='test@example.com',
#                                                 password='testpassword')

#     def test_logout_user(self):
#         # Log in the user
#         self.client.login(username='testuser', password='testpassword')

#         # Make a GET request to the logout view
#         response = self.client.get(reverse('logout'))

#         # Ensure that the response is a redirect
#         self.assertEqual(response.status_code, 302)
        
#         # Ensure that the redirection goes to the home page
#         self.assertEqual(response.url, reverse('home'))

#         # Ensure that the user is logged out
#         self.assertNotIn('_auth_user_id', self.client.session)

#         # Ensure that the logout message is displayed
#         storage = get_messages(response.wsgi_request)
#         self.assertEqual(list(storage)[0].message, 'Your session has ended')

#     def test_logout_user_not_logged_in(self):
#         # Make a GET request to the logout view without logging in
#         response = self.client.get(reverse('logout'))

#         # Ensure that the response is a redirect
#         self.assertEqual(response.status_code, 302)
        
#         # Ensure that the redirection goes to the home page
#         self.assertEqual(response.url, reverse('home'))

#         # Ensure that the user is not logged in
#         self.assertNotIn('_auth_user_id', self.client.session)



# class UserListTestCase(TestCase):
#     def setUp(self):
#         # Create a superuser and a regular user
#         self.superuser = get_user_model().objects.create_superuser(
#             username='admin', email='admin@example.com', password='adminpassword')
#         self.user = get_user_model().objects.create_user(
#             username='user', email='user@example.com', password='userpassword')

#         # Create a test client
#         self.client = Client()

#     def test_non_superuser_redirect(self):
#         # Log in the regular user
#         self.client.login(username='user', password='userpassword')

#         # Make a GET request to the user_list view
#         response = self.client.get(reverse('user_list'))

#         # Ensure that the response is a redirect to the home page
#         self.assertRedirects(response, reverse('home'))

#     def test_superuser_user_list(self):
#         # Log in the superuser
#         self.client.login(username='admin', password='adminpassword')

#         # Make a GET request to the user_list view
#         response = self.client.get(reverse('user_list'))

#         # Ensure that the response status code is 200
#         self.assertEqual(response.status_code, 200)

#         # Ensure that the correct template is used
#         self.assertTemplateUsed(response, 'dashboard\\adminUsersList.html')

#         # Ensure that the response contains the non-superuser user
#         self.assertIn(self.user, response.context['users'])



# class DeleteUsersTestCase(TestCase):
#     def setUp(self):
#         # Create a superuser and a regular user
#         self.superuser = get_user_model().objects.create_superuser(username='admin',
#                                                                     email='admin@example.com',
#                                                                       password='adminpassword')
#         self.user = get_user_model().objects.create_user(username='user',
#                                                           email='user@example.com',
#                                                             password='userpassword')

#         # Create a test client
#         self.client = Client()

#     def test_non_superuser_redirect(self):
#         # Log in the non-superuser
#         self.client.login(username='user', password='userpassword')

#         # Create a POST request with a non-superuser
#         response = self.client.post(reverse('delete_users'))

#         # Ensure that the response status code is 302 (redirect)
#         self.assertEqual(response.status_code, 302)


#     def test_superuser_delete_users(self):
#         # Log in the superuser
#         self.client.login(username='admin', password='adminpassword')

#         # Make a POST request to delete_users with user_ids parameter
#         response = self.client.post(reverse('delete_users'), {'user_ids': [self.user.id]})

#         # Ensure that the response is a redirect to the user list page
#         self.assertRedirects(response, reverse('user_list'))

#         # Ensure that the specified user is deleted
#         self.assertFalse(User.objects.filter(id=self.user.id).exists())


# class ProfileViewTestCase(TestCase):
#     def setUp(self):
#         # Create a superuser and a regular user
#         self.superuser = get_user_model().objects.create_superuser(username='admin',
#                                                                     email='admin@example.com',
#                                                                       password='adminpassword')
#         self.user = get_user_model().objects.create_user(username='user',
#                                                           email='user@example.com',
#                                                             password='userpassword')

#         # Create a test client
#         self.client = Client()

#         # Create a Profile object for the regular user if it doesn't already exist
#         if not Profile.objects.filter(user=self.user).exists():
#             self.profile = Profile.objects.create(user=self.user, full_name='Test User',
#                                                    address='Test Address',
#                                                      mobile='1234567890', bio='Test Bio')

#     def test_authenticated_user(self):
#         # Log in the regular user
#         self.client.login(username='user', password='userpassword')

#         # Ensure that the Profile object exists for the regular user
#         if not hasattr(self, 'profile'):
#             self.profile = Profile.objects.get(user=self.user)

#         # Make a GET request to the profile page
#         response = self.client.get(reverse('profile', kwargs={'pk': self.profile.pk}))

#         # Ensure that the response status code is 200
#         self.assertEqual(response.status_code, 200)

#         # Ensure that the correct template is used
#         self.assertTemplateUsed(response, 'users/profile.html')

#         # Ensure that the profile is passed to the template context
#         self.assertEqual(response.context['profile'], self.profile)




# class UpdateUserTestCase(TestCase):
#     def setUp(self):
#         # Create a test user
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='password123'
#         )

#         # Create a test client
#         self.client = Client()

#     def test_unauthenticated_user_update(self):
#         # Make a GET request without logging in
#         response = self.client.get(reverse('update_user'))

#         # Ensure that the response is a redirect to the dashboard
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('dashboard'))


class UpdateProfileTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.client = Client()

    def test_authenticated_user_update_profile(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Make a POST request to update the profile
        response = self.client.post(reverse('update_profile'), {
            'full_name': 'Updated Name',
            'address': 'Updated Address',
            'mobile': '1234567890',
            'bio': 'Updated Bio',
        })

        # Ensure that the response is a redirect to the dashboard
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('dashboard'))

    def test_unauthenticated_user_update_profile(self):
        # Make a GET request to update the profile without logging in
        response = self.client.get(reverse('update_profile'))

        # Ensure that the response is a redirect to the dashboard
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('dashboard'))