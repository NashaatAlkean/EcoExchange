# from django.test import TestCase
# from .models import Conversation, ConversationMessage
# from django.contrib.auth import get_user_model
# from items.models import Items
# from .forms import ConversationMessageForm
# from django.urls import reverse


# User = get_user_model()

# class ConversationModelTest(TestCase):
#     def setUp(self):
#         # Setup test data
#         self.user1 = User.objects.create_user(username='user1', email='user1@example.com', password='testpass123')
#         self.user2 = User.objects.create_user(username='user2', email='user2@example.com', password='testpass123')
#         self.item = Items.objects.create(title="Test Item", user=self.user1)
#         self.conversation = Conversation.objects.create(item=self.item)
#         self.conversation.members.add(self.user1, self.user2)
#         self.message = ConversationMessage.objects.create(
#             conversation=self.conversation,
#             content='Hello World',
#             created_by=self.user1
#         )

#     def test_conversation_creation(self):
#         self.assertEqual(self.conversation.members.count(), 2)
#         self.assertIn(self.user1, self.conversation.members.all())

#     def test_message_creation(self):
#         self.assertEqual(self.message.content, 'Hello World')
#         self.assertEqual(self.message.created_by, self.user1)


# class ConversationMessageFormTest(TestCase):
#     def test_form_validity(self):
#         form_data = {'content': 'Test Message'}
#         form = ConversationMessageForm(data=form_data)
#         self.assertTrue(form.is_valid())

# class NewConversationViewTest(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_user(username='user1', email='user1@example.com', password='testpass123')
#         self.user2 = User.objects.create_user(username='user2', email='user2@example.com', password='testpass123')
#         self.client.login(username='user1', password='testpass123')
#         self.item = Items.objects.create(title="Test Item", user=self.user2)
    
#     def test_new_conversation_view(self):
#         response = self.client.get(reverse('conversation:new', args=[self.item.pk]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'conversation/new_conv.html')


# class InboxViewTest(TestCase):
#     def test_inbox_view_for_logged_in_user(self):
#         self.client.login(username='user1', password='testpass123')
#         response = self.client.get(reverse('conversation:inbox'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'conversation/inbox.html')


# class ConversationAccessTest(TestCase):
#     def test_inbox_view_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse('conversation:inbox'))
#         self.assertRedirects(response, f"{reverse('login')}?next={reverse('conversation:inbox')}")

#     def test_detail_view_redirect_if_not_logged_in(self):
#         url = reverse('conversation:detail', args=['1'])
#         response = self.client.get(url)
#         self.assertRedirects(response, f"{reverse('login')}?next={url}")

# class ConversationMessageCreationTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='user1', password='testpass123')
#         self.client.login(username='user1', password='testpass123')
#         self.item = Items.objects.create(title="Test Item", user=self.user)
#         self.conversation = Conversation.objects.create(item=self.item)
#         self.conversation.members.add(self.user)

#     def test_valid_form_submission_creates_message(self):
#         url = reverse('conversation:detail', args=[self.conversation.pk])
#         response = self.client.post(url, {'content': 'A new message'})
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(self.conversation.messages.filter(content='A new message').exists())

