from django.test import TestCase, Client
from .models import *
from .views import *
from .forms import *
import json


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
        ingredient_cat = IngredientCategory.objects.create(name="vegetable")
        ingredient = IngredientForm({"name" : "potato", "category" :
            "vegetable"})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientForm({"name" : "pea", "category" : "vegetable"})
        ingredient.is_valid()
        ingredient.save()

    def test_post_1(self):
        recipe1 = {"recipe": {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1", "ingredients" :
                                  [{"adjective" : "moldy", "unit" : "g",
                                    "amount" : "20", "recipe" : "1",
                                    "ingredient" : "potato"},
                                   {"adjective": "green", "unit": "g",
                                    "amount": "20", "recipe": "1",
                                    "ingredient": "pea"}]}}
        c = Client()
        response = c.post('/recipe/', json.dumps(recipe1),
                          content_type="application/json")
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0][
            'adjective'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0]['ingredient'])
        self.assertContains(response, recipe1['recipe']['ingredients'][1][
            'ingredient'])
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        print(response.content)
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0][
            'adjective'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0]['ingredient'])
        self.assertContains(response, recipe1['recipe']['ingredients'][1][
            'ingredient'])
        self.assertContains(response, 'Bob')

    def test_post_2(self):
        recipe1 = {"recipe": {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1", "ingredients" :
                                  [{"adjective" : "moldy", "unit" : "g",
                                    "amount" : "20", "recipe" : "1",
                                    "ingredient" : "potato"},
                                   {"adjective": "green", "unit" : "g",
                                    "amount" : "20", "recipe": "1",
                                    "ingredient": "pea"}]}}
        c = Client()
        response = c.post('/recipe/', json.dumps(recipe1),
                          content_type="application/json")
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0][
            'adjective'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0]['ingredient'])
        self.assertContains(response, recipe1['recipe']['ingredients'][1][
            'ingredient'])
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0][
            'adjective'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0]['ingredient'])
        self.assertContains(response, recipe1['recipe']['ingredients'][1][
            'ingredient'])
        self.assertContains(response, 'Bob')
        recipe1 = {"recipe": {"name" : "Cold ham water", "cook_time" : "2 "
                                                                       "hours",
                   "method" : "Put in water", "author" : "1", "ingredients" :
                                  [{"adjective" : "moldy", "unit" : "g",
                                    "amount" : "20", "recipe" : "1",
                                    "ingredient" : "potato"},
                                   {"adjective": "green", "unit" : "g",
                                    "amount" : "20", "recipe": "1",
                                    "ingredient": "pea"}]}}
        response = c.put('/recipe/1/', json.dumps(recipe1),
                         content_type="application/json")
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0][
            'adjective'])
        self.assertContains(response, recipe1['recipe']['ingredients'][0]['ingredient'])
        self.assertContains(response, recipe1['recipe']['ingredients'][1][
            'ingredient'])
        self.assertContains(response, 'Bob')
        response = c.delete('/recipe/1/')

    def test_post_3(self):
        recipe1 = { "recipe" : {"name" : "Hot ham water", "cook_time" : "2 " \
                                                                       "hours",
                   "method" : "Put in water", "author" : "1", "meal_cat" : [
                "Lunch", "Dinner"], "diet_req" : ["Vegan"], "ingredients" :
                                  [{"adjective" : "moldy", "unit" : "g",
                                    "amount" : "20", "recipe" : "1",
                                    "ingredient" : "potato"},
                                   {"unit" : "g",
                                    "amount" : "20", "recipe": "1",
                                    "ingredient": "pea"}]}}
        c = Client()
        response = c.post('/recipe/', json.dumps(recipe1),
                          content_type="application/json")
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        for item in recipe1['recipe']['meal_cat']:
            self.assertContains(response, item)
        for item in recipe1['recipe']['diet_req']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')
        response = c.get('/recipe/1/')
        self.assertContains(response, recipe1['recipe']['name'])
        self.assertContains(response, recipe1['recipe']['cook_time'])
        self.assertContains(response, recipe1['recipe']['method'])
        for item in recipe1['recipe']['meal_cat']:
            self.assertContains(response, item)
        for item in recipe1['recipe']['diet_req']:
            self.assertContains(response, item)
        self.assertContains(response, 'Bob')


# Create your tests here.
class IngredientTestCase(TestCase):
    def setUp(self):
        ing_cat = IngredientCategory.objects.create(name = "vegetable")

    def test_get_post_1(self):
        ingredient_test = {"ingredient" : {"name" : "pea", "category" :
            "vegetable"}}
        c = Client()
        response = c.post('/ingredients/', json.dumps(ingredient_test),
                          content_type="application/json")
        self.assertContains(response, "pea")
        self.assertContains(response, "vegetable")
        response = c.get('/ingredients/pea/')
        self.assertContains(response, "pea")
        self.assertContains(response, "vegetable")


# Create your tests here.
class PantryIngredientTestCase(TestCase):
    def setUp(self):
        ing_cat = IngredientCategory.objects.create(name = "vegetable")
        ingredient = IngredientForm({"name" : "potato", "category" :
        "vegetable"})
        ingredient.is_valid()
        ingredient.save()
        user = User.objects.create(name="Bob", email="Bob@gmail.com",
                                    password="Bob")

    def test_get_post(self):
        ingredient_test = {"ingredients" : {"expiry_date" :
                                                "2020-06-29",
                                            "ingredient" : "potato",
                                           "user" : "1"}}
        c = Client()
        response = c.post('/user/1/pantry/', json.dumps(ingredient_test),
                          content_type="application/json")
        self.assertContains(response, "potato")
        self.assertContains(response, "vegetable")