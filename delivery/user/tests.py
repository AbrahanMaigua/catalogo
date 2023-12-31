from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class UserManagersTests(TestCase):
    def test_create_user(self):
        user = get_user_model()
        user = user.objects.create(
            email='user@user.com',
            password='wood'
        )
        self.assertEqual(user.email, 'user@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            user.objects.create_user()
        with self.assertRaises(TypeError):
            user.objects.create_user(email="")
        with self.assertRaises(ValueError):
            user.objects.create_user(email="", password="foo")

    def test_create_user(self):
        admin_user = get_user_model()
        admin_user = admin_user.objects.create_superuser(
            email='admin@user.com',
            password='food'
        )
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            admin_user.objects.create_superuser(
                email="super@user.com", password="food", is_superuser=False)
