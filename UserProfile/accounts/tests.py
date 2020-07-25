from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserManager(TestCase):

    def test_create_user_method(self):
        User = get_user_model() #returns user model active in the project
        #creating a test user
        user = User.objects.create_user(email='holmes@bbc.com',
                                        password='sherlocked',
                                        username='sHeRlOcK') 
        self.assertEqual(user.email, 'holmes@bbc.com')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEquals(user.username,'sHeRlOcK')
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='sherlock')
        
    def test_create_superuser_method(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='holmes@bbc.com',
                                                   password='sherlocked', 
                                                   username='sHeRlOcK')
        self.assertEqual(admin_user.email, 'holmes@bbc.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEquals(admin_user.username,'sHeRlOcK')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='holmes@bbc.com', password='sherlocked', is_superuser=False)