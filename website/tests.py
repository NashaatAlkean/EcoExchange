from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from items.models import Items
from website.models import ReviewRating

User = get_user_model()

class WebsiteTestCase(TestCase):
    def setUp(self):#- `setUp`: פונקציה שמופעלת לפני כל טסט כדי להכין את הסביבה, כולל יצירת משתמשים ואובייקטים לטסטים.
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
#- `test_home_view`: בודקת את דף הבית של האתר ומוודאת שהוא נטען בהצלחה.
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
#- `test_items_listing`: בודקת את הדף שמציג את רשימת הפריטים ומוודאת שהוא כולל את הפריט שנוצר בהכנה.
    def test_items_listing(self):
        response = self.client.get(reverse('items-listing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')
#- `test_item_details`: בודקת את דף פרטי הפריט ומוודאת שהוא מציג את הפרטים נכונה.
    def test_item_details(self):
        response = self.client.get(reverse('item-details', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')
#- `test_reviews`: בודקת שמשתמש רשום יכול לגשת לדף הביקורות.
    def test_reviews(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
#- `test_admin_homepage_access_by_superuser`: בודקת שמנהל מערכת יכול לגשת לדף הבית של האדמין.
    def test_admin_homepage_access_by_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin-homepage'))
        self.assertEqual(response.status_code, 200)
#- `test_admin_homepage_access_by_non_superuser`: בודקת שמשתמש שאינו מנהל מערכת אינו יכול לגשת לדף הבית של האדמין.
    def test_admin_homepage_access_by_non_superuser(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('admin-homepage'))
        self.assertNotEqual(response.status_code, 200)
#- `test_unauthenticated_reviews_access`: בודקת שמשתמש שאינו מאומת אינו יכול לגשת לדף הביקורות.
    def test_unauthenticated_reviews_access(self):
        response = self.client.get(reverse('reviews'))
        self.assertNotEqual(response.status_code, 200)  # Expecting a redirect or failure due to unauthenticated access
#- `test_create_duplicate_item`: בודקת שלא ניתן ליצור פריט כפול במערכת.
    def test_create_duplicate_item(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post('/items/create/', {'title': 'Test Item', 'is_available': True})  # Assuming you have a view for item creation
        self.assertNotEqual(response.status_code, 200)  # Expecting failure due to duplicate item creation

