from django.test import TestCase
from .models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the user model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = User(username="user", owner_id=1, dob="1988-01-01")

    def test_model_can_create_a_user(self):
        """Test the user model can create a user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User(username="admin", dob="1988-01-01")
        user.save()

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Post user
        self.user_data = {
            "first_name": "f",
            "last_name": "l",
            "email": "fl@gmail.com",
            "username": "g",
            "password": "password123",
            "owner_id": "1",
            "dob": "1988-01-01",
            }
        self.response = self.client.post(
            reverse('user_create'),
            self.user_data,
            format="json")

    def test_api_can_create_a_user(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/users/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_user(self):
        """Test the api can get a given user."""
        user = User.objects.get(id=2)
        response = self.client.get('/users/', kwargs={'pk': user.id}, format="json")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    def test_api_can_update_user(self):
        """Test the api can update a given user."""
        user = User.objects.get(id=2)
        change_user = {'username': 'Something new'}
        res = self.client.put('/users/', change_user, kwargs={'pk': 1}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_user(self):
        """Test the api can delete a user."""
        user = User.objects.get(id=2)
        response = self.client.delete(
            reverse('user_details', kwargs={'pk': user.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)