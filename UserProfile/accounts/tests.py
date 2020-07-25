from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserManager(TestCase):

    def test_create_user_method(self):
        User = get_user_model() #returns user model active in the project
        user = User.objects.create_user(email='sherlock@holmes.com', password='sherlocked') #creating a test user
        self.assertEqual(user.email, 'sherlock@holmes.com')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        try:
            #username = None for AbstractUser
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='sherlocked')
        
    def test_create_superuser_method(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('sherlock@superuser.com', 'sherlocked')
        self.assertEqual(admin_user.email, 'sherlock@superuser.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='sherlock@superuser.com', password='sherlocked', is_superuser=False)