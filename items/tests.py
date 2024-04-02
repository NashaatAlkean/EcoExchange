# from django.test import TestCase
# from .models import Items, City, Catagory,RequestsItems
# from users.models import User
# from .form import DonateItemForm
# from django.urls import reverse


# class ItemsModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser', password='12345')
#         self.catagory = Catagory.objects.create(name='Books')
#         self.city = City.objects.create(name='New York')
        
#         self.item = Items.objects.create(
#             user=self.user,
#             title='Test Item',
#             location='Test Location',
#             descreption='This is a test description.',
#             catagory=self.catagory,
#             city=self.city,
#             item_type='New',
#             is_approved=False
#         )
    
#     def test_items_creation(self):
#         self.assertTrue(isinstance(self.item, Items))
#         self.assertEqual(self.item.__str__(), 'Test Item')

# class DonateItemFormTest(TestCase):
#     def test_form_validity(self):
#         form_data = {'title': 'Test Item', 'location': 'Test Location', 'descreption': 'Test Description', 'item_type': 'New'}
#         form = DonateItemForm(data=form_data)
#         self.assertTrue(form.is_valid())

# class CreateItemViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.client.login(username='testuser', password='12345')
    
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/items/create_item/')
#         self.assertEqual(response.status_code, 200)
    
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('create-add'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'items/create_ad.html')


# class UpdateItemViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
#         self.city = City.objects.create(name="Chicago")
#         self.catagory = Catagory.objects.create(name="Books")
#         self.item = Items.objects.create(
#             user=self.user,
#             title="A Book",
#             location="Chicago",
#             descreption="A good read",
#             catagory=self.catagory,
#             city=self.city,
#             item_type="New",
#         )
#         self.update_url = reverse('update_ad', kwargs={'pk': self.item.pk})

#     def test_update_item_view_for_logged_in_user(self):
#         self.client.login(username='testuser', password='password')
#         response = self.client.post(self.update_url, {
#             'title': 'Updated Title',
#             'location': 'Updated Location',
#             'descreption': 'Updated Description',
#             'item_type': 'Like New',
#         })
#         self.item.refresh_from_db()
#         self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful update
#         self.assertEqual(self.item.title, 'Updated Title')

#     def test_redirect_if_not_logged_in(self):
#         response = self.client.get(self.update_url)
#         self.assertNotEqual(response.status_code, 200)  # Expecting a redirect or error because user is not logged in



# class RequestItemViewTest(TestCase):
#     def setUp(self):
#         # Create test users
#         self.user_seeker = User.objects.create_user(username='seekeruser', email='seeker@example.com', password='password', is_seeker=True)
#         self.user_donor = User.objects.create_user(username='donoruser', email='donor@example.com', password='password', is_donor=True)

#         # Create a category and city
#         self.catagory = Catagory.objects.create(name="Books")
#         self.city = City.objects.create(name="Chicago")

#         # Create an item
#         self.item = Items.objects.create(
#             user=self.user_donor,
#             title="A Book",
#             location="Chicago",
#             descreption="A good book",
#             catagory=self.catagory,
#             city=self.city,
#             item_type="New",
#         )

#         # Generate the URL for requesting an item
#         self.request_url = reverse('request-item', kwargs={'pk': self.item.pk})

#     def test_request_item(self):
#         # Log in as the seeker user
#         self.client.login(username='seekeruser', password='password')

#         # Make a GET request to the item request URL
#         response = self.client.get(self.request_url)

#         # Check that the request was processed successfully and redirects as expected
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect happens after a successful item request

#         # Verify that a RequestsItems entry was created for the seeker user and the specific item
#         self.assertTrue(RequestsItems.objects.filter(user=self.user_seeker, item=self.item).exists())



# class ItemApprovalViewTest(TestCase):
#     def setUp(self):
#         # No need to instantiate Client, use self.client provided by TestCase
#         # Create a superuser for testing
#         self.superuser = User.objects.create_superuser('adminuser', 'admin@example.com', 'password')
#         self.user = User.objects.create_user('regularuser', 'user@example.com', 'password')
#         self.approval_url = reverse('item_approval')  # Ensure this URL name matches your urls.py

#     def test_access_for_superuser(self):
#         # Log in as the superuser
#         self.client.login(username='adminuser', password='password')
#         response = self.client.get(self.approval_url)
#         self.assertEqual(response.status_code, 200)

#     def test_redirect_for_regular_user(self):
#         # Log in as a regular user
#         self.client.login(username='regularuser', password='password')
#         response = self.client.get(self.approval_url)
#         # Expecting a redirect or permission denied response
#         self.assertNotEqual(response.status_code, 200)



# class ManageItemsViewTest(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_user('user1', email='user1@example.com', password='12345')
#         self.user2 = User.objects.create_user('user2', email='user2@example.com', password='12345')
#         self.client.login(username='user1', password='12345')

#         city = City.objects.create(name="Springfield")
#         catagory = Catagory.objects.create(name="Furniture")

#         Items.objects.create(title="Chair", user=self.user1, location="Here", descreption="A nice chair.", catagory=catagory, city=city, item_type="New")
#         Items.objects.create(title="Table", user=self.user2, location="There", descreption="A sturdy table.", catagory=catagory, city=city, item_type="Good")

#     def test_items_listed_for_user(self):
#         response = self.client.get(reverse('manage-items'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Chair")
#         self.assertNotContains(response, "Table")


# class ApproveItemViewTest(TestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
#         self.user = User.objects.create_user('user', 'user@example.com', 'userpass')
#         self.city = City.objects.create(name="Gotham")
#         self.catagory = Catagory.objects.create(name="Books")
#         self.item = Items.objects.create(title="Rare Book", user=self.user, location="Gotham Library", descreption="A very rare book.", catagory=self.catagory, city=self.city, item_type="New", is_approved=False)
#         self.approve_url = reverse('approve_item', kwargs={'item_id': self.item.id})

#     def test_approve_item_as_superuser(self):
#         self.client.login(username='admin', password='adminpass')
#         response = self.client.post(self.approve_url)
#         self.item.refresh_from_db()
#         self.assertTrue(self.item.is_approved)
#         self.assertEqual(response.status_code, 302)  # Redirect after approval

#     def test_approve_item_as_regular_user(self):
#         self.client.login(username='user', password='userpass')
#         response = self.client.post(self.approve_url)
#         self.item.refresh_from_db()
#         self.assertFalse(self.item.is_approved)
#         self.assertNotEqual(response.status_code, 302)  # Expecting failure or forbidden access


# class DeclineItemViewTest(TestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
#         self.user = User.objects.create_user('user', 'user@example.com', 'userpass')
#         self.city = City.objects.create(name="Metropolis")
#         self.catagory = Catagory.objects.create(name="Electronics")
#         self.item = Items.objects.create(title="Old Phone", user=self.user, location="Downtown", descreption="An old mobile phone.", catagory=self.catagory, city=self.city, item_type="Acceptable", is_approved=False)
#         self.decline_url = reverse('decline_item', kwargs={'item_id': self.item.id})

#     def test_decline_item_as_superuser(self):
#         self.client.login(username='admin', password='adminpass')
#         response = self.client.post(self.decline_url)
#         self.assertFalse(Items.objects.filter(id=self.item.id).exists())
#         self.assertEqual(response.status_code, 302)  # Redirect after decline

#     def test_decline_item_as_regular_user(self):
#         self.client.login(username='user', password='userpass')
#         response = self.client.post(self.decline_url)
#         self.assertTrue(Items.objects.filter(id=self.item.id).exists())
#         self.assertNotEqual(response.status_code, 302)  # Expecting failure or forbidden access



# # class DonateItemFormSubmissionTest(TestCase):
# #     def setUp(self):
# #         self.user = User.objects.create_user(username='donor', email='donor@example.com', password='testpass')
# #         self.client.login(username='donor', password='testpass')
# #         self.city = City.objects.create(name="Example City")
# #         self.catagory = Catagory.objects.create(name="General")

# #     def test_donate_item_form_submission(self):
# #         url = reverse('create-add')  # Adjust the URL name as needed
# #         with open('media\images\2021-11-29_1.png', 'rb') as file:
# #             data = {
# #                 'title': 'Test Item',
# #                 'location': 'Test Location',
# #                 'descreption': 'Test Description',
# #                 'catagory': self.catagory.pk,
# #                 'city': self.city.pk,
# #                 'item_type': 'New',
# #                 'image': SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')
# #             }
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, 302)  # Assuming redirection after successful form submission
# #         self.assertTrue(Items.objects.exists())  # Verify that an item has been created

# class CityModelTest(TestCase):
#     def setUp(self):
#         City.objects.create(name="Gotham")

#     def test_string_representation(self):
#         city = City.objects.get(name="Gotham")
#         self.assertEqual(str(city), "Gotham")

# class CatagoryModelTest(TestCase):
#     def setUp(self):
#         Catagory.objects.create(name="Electronics")

#     def test_string_representation(self):
#         catagory = Catagory.objects.get(name="Electronics")
#         self.assertEqual(str(catagory), "Electronics")


# class DonateItemFormTest(TestCase):
#     def test_form_validation_for_missing_fields(self):
#         form = DonateItemForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertIn('title', form.errors) 


# class UpdateItemAccessTest(TestCase):
#     def setUp(self):
#         self.owner = User.objects.create_user('owner', 'owner@example.com', 'testpass')
#         self.other_user = User.objects.create_user('other', 'other@example.com', 'testpass')
#         self.item = Items.objects.create(user=self.owner, title="Sample Item", location="Location", descreption="Description")
#         self.update_url = reverse('update_ad', args=[self.item.id])

#     def test_access_denied_to_non_owner(self):
#         self.client.login(username='other', password='testpass')
#         response = self.client.get(self.update_url)
#         self.assertEqual(response.status_code, 403)  # Or another appropriate response code

#     def test_access_granted_to_owner(self):
#         self.client.login(username='owner', password='testpass')
#         response = self.client.get(self.update_url)
#         self.assertEqual(response.status_code, 200)

# class ItemApprovalSuperuserTest(TestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('superuser', 'super@example.com', 'superpass')
#         self.regular_user = User.objects.create_user('user', 'user@example.com', 'userpass')
#         self.approval_url = reverse('item_approval')

#     def test_access_denied_to_regular_user(self):
#         self.client.login(username='user', password='userpass')
#         response = self.client.get(self.approval_url)
#         self.assertNotEqual(response.status_code, 200)

#     def test_access_granted_to_superuser(self):
#         self.client.login(username='superuser', password='superpass')
#         response = self.client.get(self.approval_url)
#         self.assertEqual(response.status_code, 200)

# class ItemsDeletionTest(TestCase):
#     def setUp(self):
#         user = User.objects.create_user(username='testuser', password='12345')
#         item = Items.objects.create(title="Sample Item", user=user, descreption="A sample item for testing.")
#         RequestsItems.objects.create(user=user, item=item, status='Pending')

#     def test_cascade_delete(self):
#         self.assertEqual(Items.objects.count(), 1)
#         self.assertEqual(RequestsItems.objects.count(), 1)

#         item = Items.objects.get(title="Sample Item")
#         item.delete()

#         self.assertEqual(Items.objects.count(), 0)
#         self.assertEqual(RequestsItems.objects.count(), 0)


# class FormSubmissionRedirectTest(TestCase):
#     def test_form_submission_redirect(self):
#         response = self.client.post('/your-form-url/', {'field1': 'value1', 'field2': 'value2'})
#         self.assertRedirects(response, '/your-expected-redirect-url/')


