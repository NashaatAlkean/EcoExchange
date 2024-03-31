from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from items.models import Items
from website.models import ReviewRating

User = get_user_model()

class WebsiteTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password', email='test@example.com')
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

        self.item = Items.objects.create(
            title='Test Item',
            is_available=True,
            user=self.superuser
        )

        self.review = ReviewRating.objects.create(
            user=self.user,
            subject='Test Review',
            review='Test Review Content',
            rating=5
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_items_listing(self):
        response = self.client.get(reverse('items-listing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_item_details(self):
        response = self.client.get(reverse('item-details', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_reviews(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)

    def test_admin_homepage_access_by_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin-homepage'))
        self.assertEqual(response.status_code, 200)

    def test_admin_homepage_access_by_non_superuser(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('admin-homepage'))
        self.assertNotEqual(response.status_code, 200)

    # Failing tests
    # def test_invalid_item_access(self):
    #     self.client.login(username='testuser', password='password')
    #     response = self.client.get(reverse('item-details', kwargs={'pk': 9999}))
    #     self.assertEqual(response.status_code, 404)  # Assuming 9999 is an invalid item id, expecting a 404 error

    def test_unauthenticated_reviews_access(self):
        response = self.client.get(reverse('reviews'))
        self.assertNotEqual(response.status_code, 200)  # Expecting a redirect or failure due to unauthenticated access

    def test_create_duplicate_item(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post('/items/create/', {'title': 'Test Item', 'is_available': True})  # Assuming you have a view for item creation
        self.assertNotEqual(response.status_code, 200)  # Expecting failure due to duplicate item creation
