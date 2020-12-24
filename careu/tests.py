# from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, LiveServerTestCase, tag, Client
from django.urls import reverse
from http import HTTPStatus
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile

class UserTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.register_url = ('/register/')
        self.login_url = '/login/'
        self.logout_url = '/logout/'

        # test exist user
        User.objects.create_user(
            username='alreadyexist', password='top_secret')
        self.user = {
            'username':'jacob',
            'password1':'top_secret',
            'password2':'top_secret'
        }

        self.login_user = {
            'username': 'jacob',
            'password': 'top_secret'
        }

        self.login_user_invalid = {
            'username': ''
        }

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view()#
        response = self.client.get(reverse('team-base'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('home-base'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('journal-base'))
        self.assertEqual(response.status_code, 200)

        #response = self.client.get(reverse('logout_view'))
        #self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('chat-base'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('journal-create'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        data = {
            'username':'jacob',
            'password1':'top_secret'
        }

        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # test untuk user yang sudah ada yaaa
        response = self.client.post(self.register_url,data = data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # register
        self.client.post(self.register_url,data = self.user)
        counting = Profile.objects.all().count()
        self.assertEqual(counting,1)

        # check current state berhasil melakukan otentikasi dari user yang baru di daftarkan
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        counting = Profile.objects.all().count()
        self.assertEqual(counting,1)

        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        self.client.logout()
        response = self.client.post(self.login_url, self.login_user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # invalid username and password
        self.client.logout()
        response = self.client.post(self.login_url, {'aneh':'aneh'})
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # user = User.objects.get(username='jacob')
        # self.assertTrue(self.user.is_authenticated)

    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        
        response = self.client.post(self.register_url, data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
    
    def test_profile(self):
        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        counting = Profile.objects.all().count()
        self.assertEqual(counting,1)

        response = self.client.get('/profile/jacob/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_view(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_post(self):
        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        counting = Profile.objects.all().count()
        self.assertEqual(counting,1)

        response = self.client.post('/post/new/',data = {'title':'mantap', 'content': 'iya mantap'})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # coverage run manage.py test