from django.test import TestCase
from .models import *


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Bob",
                                         email="Potato17@gmail.com",
                                         password="4321")

    def test_print(self):
        assert(print(self.user) == "Bob")

    def test_deets(self):
        assert(self.user.name =="Bob")
        assert(self.user.email == "Potato17@gmail.com")
        assert(self.user.password == "4321")

