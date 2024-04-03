import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Report

User = get_user_model()
#- `setUp`: מכינה את הסביבה לבדיקות, כולל יצירת משתמשים ודיווח (ריפורט).
class ReportsTestCase(TestCase):
    def setUp(self):
        # Create a user and a superuser with unique emails
        self.user = User.objects.create_user(username='user', email='user@example.com', password='user1234')
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin1234')

        # Create a report
        self.report = Report.objects.create(
            title='Test Report',
            description='Description of Test Report',
            user=self.user
        )

        self.client = Client()
#- `test_report_issue_get`: בודקת אם דף הגשת דיווח נטען כראוי עבור משתמש רשום.
    def test_report_issue_get(self):
        self.client.login(username='user', password='user1234')
        response = self.client.get(reverse('report_issue'))
        self.assertEqual(response.status_code, 200)
#- `test_report_issue_post_invalid`: בודקת ששליחת טופס דיווח לא תקין (פרטים ריקים) מחזירה שגיאות טופס.
    def test_report_issue_post_invalid(self):
        self.client.login(username='user', password='user1234')
        response = self.client.post(reverse('report_issue'), {'title': '', 'description': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors)
#- `test_report_issue_post_valid`: בודקת ששליחת טופס דיווח תקין עם תמונה נתמך ומסתיים בהפניה.
    def test_report_issue_post_valid(self):
        self.client.login(username='user', password='user1234')
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
            img = SimpleUploadedFile(tmp.name, b'file_content', content_type='image/jpeg')
            response = self.client.post(reverse('report_issue'), {'title': 'New Report', 'description': 'New report description', 'image': img})
        self.assertEqual(response.status_code, 302)
#- `test_view_reports_superuser`: בודקת שמנהל מערכת יכול לראות את כל הדיווחים.
    def test_view_reports_superuser(self):
        self.client.login(username='admin', password='admin1234')
        response = self.client.get(reverse('view_reports'))
        self.assertEqual(response.status_code, 200)
#- `test_view_reports_non_superuser`: בודקת שמשתמש שאינו מנהל מערכת מופנה מדף צפייה בדיווחים.
    def test_view_reports_non_superuser(self):
        self.client.login(username='user', password='user1234')
        response = self.client.get(reverse('view_reports'))
        self.assertEqual(response.status_code, 302)
#- `test_delete_report_superuser`: בודקת שמנהל מערכת יכול למחוק דיווח.
    def test_delete_report_superuser(self):
        self.client.login(username='admin', password='admin1234')
        response = self.client.post(reverse('delete_report', args=[self.report.id]))
        self.assertEqual(response.status_code, 302)
#- `test_delete_report_non_superuser`: בודקת שמשתמש שאינו מנהל מערכת לא יכול למחוק דיווח דרך הממשק.
    def test_delete_report_non_superuser(self):
        self.client.login(username='user', password='user1234')
        response = self.client.post(reverse('delete_report', args=[self.report.id]))
        self.assertEqual(response.status_code, 302)
#- `test_resolve_report_superuser`: בודקת שמנהל מערכת יכול לסמן דיווח כפתור.
    def test_resolve_report_superuser(self):
        self.client.login(username='admin', password='admin1234')
        response = self.client.post(reverse('resolve_report', args=[self.report.id]))
        self.assertEqual(response.status_code, 302)
        self.report.refresh_from_db()
        self.assertTrue(self.report.resolved)
#- `test_resolve_report_non_superuser`: בודקת שמשתמש שאינו מנהל מערכת לא יכול לסמן דיווח כפתור.
    def test_resolve_report_non_superuser(self):
        self.client.login(username='user', password='user1234')
        response = self.client.post(reverse('resolve_report', args=[self.report.id]))
        self.assertEqual(response.status_code, 302)
#- `test_non_authenticated_access`: בודקת שמשתמש לא מאומת מופנה לדף הכניסה בניסיון גישה לדיווח.
    def test_non_authenticated_access(self):
        response = self.client.get(reverse('report_issue'))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('report_issue')}")

    # Additional tests designed to fail
#- `test_fail_to_resolve_report_without_login`: בודקת שלא ניתן לסמן דיווח כפתור בלי להיות מחובר, אמורה להיכשל.        
    def test_fail_to_resolve_report_without_login(self):
        response = self.client.post(reverse('resolve_report', args=[self.report.id]))
        self.assertEqual(response.status_code, 200)  # Expected to fail
#- `test_fail_to_create_report_with_duplicate_title`: בודקת שניסיון ליצור דיווח עם כותרת כפולה יכשל, כאשר היא אמורה להיכשל.
    def test_fail_to_create_report_with_duplicate_title(self):
        self.client.login(username='user', password='user1234')
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
            img = SimpleUploadedFile(tmp.name, b'file_content', content_type='image/jpeg')
            response = self.client.post(reverse('report_issue'), {'title': 'Test Report', 'description': 'Another description', 'image': img})
        self.assertEqual(response.status_code, 302)  # Expected to fail
