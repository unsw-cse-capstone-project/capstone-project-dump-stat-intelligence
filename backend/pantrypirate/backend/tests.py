from django.test import TestCase, Client
from .models import *
from .views import *
from .forms import *


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Bob",
                                         email="Potato17@gmail.com",
                                         password="4321")

    def test_deets(self):
        assert(self.user.name == "Bob")
        assert(self.user.email == "Potato17@gmail.com")
        assert(self.user.password == "4321")


class RecipeTestCase(TestCase):
    def setUp(self):
        meal_cat = MealCategory.objects.create(name="Lunch")
        meal_cat2 = MealCategory.objects.create(name="Dinner")
        diet_req = DietaryRequirement.objects.create(name="Vegan")
        diet_req = DietaryRequirement.objects.create(name="Vegetarian")
        user = User.objects.create(name="Bob", email="Bob@gmail.com",
                                    password="Bob")

    def test_post_1(self):
        recipe1 = {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1"}
        c = Client()
        response = c.post('/recipe/', recipe1)
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        self.assertContains(response, 'Bob')

    def test_post_2(self):
        recipe1 = {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1", "meal_cat" : [
                "Lunch", "Dinner"]}
        c = Client()
        response = c.post('/recipe/', recipe1)
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        for item in recipe1['meal_cat']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        for item in recipe1['meal_cat']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')

    def test_post_3(self):
        recipe1 = {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1", "meal_cat" : [
                "Lunch", "Dinner"], "diet_req" : ["Vegan"]}
        c = Client()
        response = c.post('/recipe/', recipe1)
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        for item in recipe1['meal_cat']:
            self.assertContains(response, item)
        for item in recipe1['diet_req']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        self.assertContains(response, recipe1['name'])
        self.assertContains(response, recipe1['cook_time'])
        self.assertContains(response, recipe1['method'])
        for item in recipe1['meal_cat']:
            self.assertContains(response, item)
        for item in recipe1['diet_req']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')



