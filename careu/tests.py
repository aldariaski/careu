# from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, LiveServerTestCase, tag, Client
from django.urls import reverse


#from .views import views

class UserTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view()
        response = self.client.get(reverse('careu:team-base'))
        self.assertEqual(response.status_code, 200)