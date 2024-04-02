from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import CommentForm, ProfilePicForm, NewsForm, SignUpForm


class TestProfilePicForm(TestCase):
    def test_form_is_valid(self):
        with open("/workspace/NewsStories/media/images/face.jpg", "rb") as f:
            image_data = f.read()
        image = SimpleUploadedFile("default_profile_pic.png", image_data, content_type="image/png")
        form_data = {
            'profile_image': image, 
            'profile_bio':'Test bio', 
            'website_link':'Test website', 
            'facebook_link':'facebook link', 
            'instagram_link':'instagram link'
        }
        profilepic_form = ProfilePicForm(data=form_data, files=form_data)
        self.assertTrue(profilepic_form.is_valid(), msg="Form is invalid")


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
    
    def test_username_is_required(self):
        signup_form = SignUpForm({
            'username':'',
            'email':'sophie@test.com',
            'first_name':'Sophie',
            'last_name':'Carr',
            'password1':'Thisisatest',
            'password2':'Thisisatest',
            })
        self.assertFalse(signup_form.is_valid(), msg="username not provided, but form is valid")

    def test_email_is_required(self):
        signup_form = SignUpForm({
            'username':'Sophie',
            'email':'',
            'first_name':'Sophie',
            'last_name':'Carr',
            'password1':'Thisisatest',
            'password2':'Thisisatest',
            })
        self.assertFalse(signup_form.is_valid(), msg="email not provided, but form is valid")

    def test_firstname_is_required(self):
        signup_form = SignUpForm({
            'username':'Sophie',
            'email':'sophie@test.com',
            'first_name':'',
            'last_name':'Carr',
            'password1':'Thisisatest',
            'password2':'Thisisatest',
            })
        self.assertFalse(signup_form.is_valid(), msg="first name not provided, but form is valid")

    def test_lastname_is_required(self):
        signup_form = SignUpForm({
            'username':'Sophie',
            'email':'sophie@test.com',
            'first_name':'Sophie',
            'last_name':'',
            'password1':'Thisisatest',
            'password2':'Thisisatest',
            })
        self.assertFalse(signup_form.is_valid(), msg="last name not provided, but form is valid")

    def test_password_is_required(self):
        signup_form = SignUpForm({
            'username':'',
            'email':'sophie@test.com',
            'first_name':'Sophie',
            'last_name':'Carr',
            'password1':'',
            'password2':'',
            })
        self.assertFalse(signup_form.is_valid(), msg="password not provided, but form is valid")

    def test_password_is_required(self):
        signup_form = SignUpForm({
            'username':'',
            'email':'sophie@test.com',
            'first_name':'Sophie',
            'last_name':'Carr',
            'password1':'Thisisatest',
            'password2':'Thisisatest2',
            })
        self.assertFalse(signup_form.is_valid(), msg="passwords do not match, but form is valid")