from django.test import TestCase
from .forms import CommentForm, NewsForm, SignUpForm


class TestNewsForm(TestCase):
    def test_form_is_valid(self):
        news_form = NewsForm({
            'title':'Test Title',
            'summary':'Test Summary',
            'body':'Test Body' 
        })
        self.assertTrue(news_form.is_valid(), msg="Form is invalid")

    def test_title_is_required(self):
        news_form = NewsForm({
            'title':'',
            'summary':'Test Summary',
            'body':'Test Body' 
        })
        self.assertFalse(news_form.is_valid(), msg="Title not provided, but form is valid")

    def test_summary_is_requred(self):
        news_form = NewsForm({
            'title':'Test Title',
            'summary':'',
            'body':'Test Body' 
        })
        self.assertFalse(news_form.is_valid(), msg="Summary not provided, but form is valid")

    def test_form_body_is_required(self):
        news_form = NewsForm({
            'title':'Test Title',
            'summary':'Test Summary',
            'body':'' 
        })
        self.assertFalse(news_form.is_valid(), msg="Body not provided, but form is valid")


class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        comment_form = CommentForm({'comment_body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")
    
    def test_form_is_invalid(self):
        comment_form = CommentForm({'comment_body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestSignUpForm(TestCase):
    def test_form_is_valid(self):
        signup_form = SignUpForm({
            'username':'Sophie',
            'email':'sophie@test.com',
            'first_name':'Sophie',
            'last_name':'Carr',
            'password1':'Thisisatest',
            'password2':'Thisisatest',
            })
        self.assertTrue(signup_form.is_valid(), msg="Form is invalid")
    
    def test_form_is_invalid(self):
        signup_form = SignUpForm({
            'email': '',
            'first_name': 'Sophie',
            'second_name':'Carr'
            })
        self.assertFalse(signup_form.is_valid(), msg="Form is valid")