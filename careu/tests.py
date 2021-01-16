'''module to test'''
from http import HTTPStatus
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .models import Profile

class UserTestAndOtherView(TestCase):
    '''user test case dan beberapa view'''
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
            'username':'jacob123',
            'password1':'top_secret',
            'password2':'top_secret'
        }

        self.login_user = {
            'username': 'jacob123',
            'password': 'top_secret'
        }

        self.login_user_invalid = {
            'username': ''
        }

    def test_details(self):
        ''' Create an instance of a GET request.'''
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

        response = self.client.get(reverse('chat-base'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('journal-create'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        '''test register user'''
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
        counting = Profile.objects.all().count() # pylint: disable=no-member
        self.assertEqual(counting,1)

        # check current state berhasil melakukan otentikasi dari user yang baru di daftarkan
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


    def test_login(self):
        '''test untuk login'''
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        counting = Profile.objects.all().count()# pylint: disable=no-member
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

    def test_logout(self):
        '''test untuk logout'''
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.post(self.register_url, data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_profile(self):
        '''test bisa lihat profile'''
        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        counting = Profile.objects.all().count() # pylint: disable=no-member
        self.assertEqual(counting,1)

        response = self.client.get('/profile/jacob123/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_view(self):
        '''test post view'''
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_post(self):
        '''test create post'''
        response = self.client.post(self.register_url,data = self.user)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        counting = Profile.objects.all().count() # pylint: disable=no-member
        self.assertEqual(counting,1)

        response = self.client.post('/post/new/',data = {'title':'mantap', 'content': 'iya mantap'})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_ajax_password(self):
        '''test create post'''
        response = self.client.get('/validate_password/?password1=asdasd&password2=asdasd')
        self.assertEqual(response.status_code,HTTPStatus.OK)

        response = self.client.get('/validate_password/?password1=asdasdas&password2=asdasdas')
        self.assertEqual(response.status_code,HTTPStatus.OK)

    def test_ajax_username(self):
        '''test create post'''
        response = self.client.get('/validate_username/?username=fauziridwan1709')
        self.assertEqual(response.status_code,HTTPStatus.OK)

        response = self.client.get('/validate_username/?username=fa12')
        self.assertEqual(response.status_code,HTTPStatus.OK)
