from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import News

class TestNewsDetail(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.news = News(title="News title", user=self.user,
                         summary="News excerpt",
                         body="News content")
        self.news.save()

    def test_render_news_display_page_with_comment_form(self):
        response = self.client.get(reverse(
            'news_display', args=[self]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"News title", response.content)
        self.assertIn(b"News content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)