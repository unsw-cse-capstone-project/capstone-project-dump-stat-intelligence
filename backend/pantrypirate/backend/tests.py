from django.test import TestCase, Client
from rest_framework.test import force_authenticate, APIClient
from .models import *
from .views import *
import json


# Create your tests here.
class UserTestCase(TestCase):

    def test_create_user(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user_data2 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.post('/user/', json.dumps(user_data1),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())
        user = c.post('/user/', json.dumps(user_data2),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data2.items())

    def test_get_user(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        c.post('/user/', json.dumps(user_data1),
               content_type='application/json')
        user = c.get('/user/1/')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())

    def test_get_users(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user_data2 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        c.post('/user/', json.dumps(user_data1),
               content_type='application/json')
        c.post('/user/', json.dumps(user_data2),
               content_type='application/json')
        users = c.get('/user/')
        self.assertGreaterEqual(json.loads(users.content)['results'][1].items(),
                                user_data1.items())
        self.assertGreaterEqual(json.loads(users.content)['results'][0].items(),
                                user_data2.items())

    def test_delete_user(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        c.post('/user/', json.dumps(user_data1),
               content_type='application/json')
        c.delete('/user/1/')
        user = c.get('/user/1/')
        self.assertContains(user, "Not found", status_code=404)

    def test_put_user(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        c.post('/user/', json.dumps(user_data1),
               content_type='application/json')
        user_data1 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.put('/user/1/', json.dumps(user_data1),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())


# Create your tests here.
class Ingredient(TestCase):
    def setUp(self) -> None:
        cat = IngredientCategory.objects.create(name='grain')
        cat = IngredientCategory.objects.create(name='vegetable')

    def test_create_ingredient1(self):
        c = Client()
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        ing = c.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_create_ingredient2(self):
        c = Client()
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'not_grain'}}
        ing = c.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_get_ingredient(self):
        c = Client()
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ing = c.get('/ingredients/potato/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_get_ingredients(self):
        c = Client()
        ingredient_data1 = {'name': 'potato', 'category': {'name': 'grain'}}
        ingredient_data2 = {'name': 'beef', 'category': {'name': 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data1),
               content_type='application/json')
        c.post('/ingredients/', json.dumps(ingredient_data2),
               content_type='application/json')
        ing = c.get('/ingredients/')
        self.assertGreaterEqual(json.loads(ing.content)['results'][1].items(),
                                ingredient_data1.items())
        self.assertGreaterEqual(json.loads(ing.content)['results'][0].items(),
                                ingredient_data2.items())

    def test_delete_ingredient(self):
        c = Client()
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        c.delete('/ingredients/potato/')
        ing = c.get('/ingredients/potato/')
        self.assertContains(ing, "Not found", status_code=404)

    def test_put_ingredient(self):
        c = Client()
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'vegetable'}}
        ing = c.put('/ingredients/potato/', json.dumps(ingredient_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())


# Create your tests here.
class Recipe(TestCase):
    def setUp(self) -> None:
        meal_cat = MealCategory.objects.create(name="lunch")
        meal_cat2 = MealCategory.objects.create(name="dinner")
        diet_req = DietaryRequirement.objects.create(name="vegan")
        diet_req = DietaryRequirement.objects.create(name="vegetarian")
        user = User.objects.create(username="Bob", email="Bob@gmail.com",
                                   password="Bob")
        user = User.objects.create(username="Tob", email="Tob@gmail.com",
                                   password="Tob")
        ingredient_cat = IngredientCategory.objects.create(name="vegetable")
        ingredient = IngredientSerializer(data={"name": "potato", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "pea", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()

    def test_create_recipe(self):
        c = Client()
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "potato"},
                            {"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'favourites':
                           [],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        ing = c.post('/recipes/', json.dumps(recipe_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"id": 1,
                                 "name": "Hot "
                                         "ham "
                                         "water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author":
                                     {"id": 1,
                                      "username": "Bob",
                                      "password": "Bob",
                                      "email": "Bob@gmail.com",
                                      "favourites": []},
                                 "meal_cat": [{
                                     "name": "dinner"}],
                                 "diet_req":
                                     [{
                                         "name": "vegan"}],
                                 "favourites": [],
                                 "ingredients":
                                     [{
                                         "adjective": "moldy",
                                         "unit": "g",
                                         "amount": "20",
                                         "recipe": 1,
                                         "ingredient": {
                                             "name": "potato",
                                             "category": {
                                                 "name": "vegetable"}}},
                                         {
                                             "adjective": "moldy",
                                             "unit": "g",
                                             "amount": "20",
                                             "recipe": 1,
                                             "ingredient": {
                                                 "name": "pea",
                                                 "category": {
                                                     "name": "vegetable"}}}]}.items())

    def test_get_recipe(self):
        c = Client()
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "potato"},
                            {"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'favourites':
                           [],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        ing = c.post('/recipes/', json.dumps(recipe_data),
                     content_type='application/json')
        ing = c.get('/recipes/1/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"id": 1,
                                 "name": "Hot "
                                         "ham "
                                         "water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author":
                                     {"id": 1,
                                      "username": "Bob",
                                      "password": "Bob",
                                      "email": "Bob@gmail.com",
                                      "favourites": []},
                                 "meal_cat": [{
                                     "name": "dinner"}],
                                 "diet_req":
                                     [{
                                         "name": "vegan"}],
                                 "favourites": [],
                                 "ingredients":
                                     [{
                                         "adjective": "moldy",
                                         "unit": "g",
                                         "amount": "20",
                                         "recipe": 1,
                                         "ingredient": {
                                             "name": "potato",
                                             "category": {
                                                 "name": "vegetable"}}},
                                         {
                                             "adjective": "moldy",
                                             "unit": "g",
                                             "amount": "20",
                                             "recipe": 1,
                                             "ingredient": {
                                                 "name": "pea",
                                                 "category": {
                                                     "name": "vegetable"}}}]}.items())

    def test_get_recipes(self):
        c = Client()
        recipe_data1 = {"name": "Hot ham water", "cook_time": "2 hours",
                        "method": "Put in water", "author": "1", "ingredients":
                            [{"adjective": "moldy", "unit": "g",
                              "amount": "20", "ingredient":
                                  "potato"},
                             {"adjective": "moldy", "unit": "g",
                              "amount": "20", "ingredient":
                                  "pea"}],
                        'favourites':
                            [],
                        'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        recipe_data2 = {"name": "Cold ham water", "cook_time": "2 hours",
                        "method": "Put in cold water", "author": "1",
                        "ingredients":
                            [{"adjective": "moldy", "unit": "g",
                              "amount": "20", "ingredient":
                                  "potato"}],
                        'favourites':
                            [],
                        'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        c.post('/recipes/', json.dumps(recipe_data1),
               content_type='application/json')
        c.post('/recipes/', json.dumps(recipe_data2),
               content_type='application/json')
        ing = c.get('/recipes/')
        self.assertGreaterEqual(json.loads(ing.content)['results'][1].items(),
                                {"id": 1,
                                 "name": "Hot "
                                         "ham "
                                         "water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author":
                                     {"id": 1,
                                      "username": "Bob",
                                      "password": "Bob",
                                      "email": "Bob@gmail.com",
                                      "favourites": []},
                                 "meal_cat": [{
                                     "name": "dinner"}],
                                 "diet_req":
                                     [{
                                         "name": "vegan"}],
                                 "favourites": [],
                                 "ingredients":
                                     [{
                                         "adjective": "moldy",
                                         "unit": "g",
                                         "amount": "20",
                                         "recipe": 1,
                                         "ingredient": {
                                             "name": "potato",
                                             "category": {
                                                 "name": "vegetable"}}},
                                         {
                                             "adjective": "moldy",
                                             "unit": "g",
                                             "amount": "20",
                                             "recipe": 1,
                                             "ingredient": {
                                                 "name": "pea",
                                                 "category": {
                                                     "name": "vegetable"}}}]}.items())
        self.assertGreaterEqual(json.loads(ing.content)['results'][0].items(),
                                {"id": 2,
                                 "name": "Cold "
                                         "ham "
                                         "water",
                                 "cook_time": "2 hours",
                                 "method": "Put in cold water",
                                 "author":
                                     {"id": 1,
                                      "username": "Bob",
                                      "password": "Bob",
                                      "email": "Bob@gmail.com",
                                      "favourites": []},
                                 "meal_cat": [{
                                     "name": "dinner"}],
                                 "diet_req":
                                     [{
                                         "name": "vegan"}],
                                 "favourites": [],
                                 "ingredients":
                                     [{
                                         "adjective": "moldy",
                                         "unit": "g",
                                         "amount": "20",
                                         "recipe": 2,
                                         "ingredient": {
                                             "name": "potato",
                                             "category": {
                                                 "name": "vegetable"}}}]}.items())

    def test_delete_recipe(self):
        c = Client()
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "potato"},
                            {"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'favourites':
                           [],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        c.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        c.delete('/recipes/1/')
        ing = c.get('/recipes/1/')
        self.assertContains(ing, "Not found", status_code=404)

    def test_put_recipe(self):
        c = Client()
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "10", "ingredient":
                                 "potato"}],
                       'favourites':
                           [],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        c.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        recipe_data = {"name": "Cold ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "2", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'favourites':
                           [],
                       'meal_cat': [{"name": "lunch"}, {"name": "dinner"}],
                       'diet_req': [{"name": "vegetarian"}]}
        ing = c.put('/recipes/1/', json.dumps(recipe_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"id": 1, "name": "Cold ham water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author": {"id": 2, "username": "Tob",
                                            "password": "Tob",
                                            "email": "Tob@gmail.com",
                                            "favourites": []},
                                 "meal_cat": [{"name": "dinner"},
                                              {"name": "lunch"}],
                                 "diet_req": [{"name": "vegetarian"}],
                                 "favourites": [], "ingredients": [
                                    {"adjective": "moldy", "unit": "g",
                                     "amount": "20", "recipe": 1,
                                     "ingredient": {"name": "pea", "category": {
                                         "name": "vegetable"}}}]}.items())


# Create your tests here.
class PantryIngredientTest(TestCase):
    def setUp(self) -> None:
        cat = IngredientCategory.objects.create(name='grain')
        cat = IngredientCategory.objects.create(name='vegetable')
        ingredient = IngredientSerializer(data={"name": "potato", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "pea", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        self.user1 = User.objects.create(username="Bob", email="Bob@gmail.com",
                                         password="Bob")
        self.user2 = User.objects.create(username="Tob", email="Tob@gmail.com",
                                         password="Tob")

    def test_create_pantry_ingredient1(self):
        c = Client()
        ingredient_data = {'expiry_date': '2020-06-20', 'user': "1",
                           "ingredient": "potato"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
                                          "password": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    def test_create_pantry_ingredient2(self):
        c = Client()
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "password": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    def test_get_pantry_ingredient1(self):
        c = Client()
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        ing = c.get('/user/pantry/1/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "password": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    def test_get_pantry_ingredients1(self):
        c = Client()
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        api_client = APIClient()
        api_client.force_authenticate(user=self.user1)
        response = api_client.get('/user/pantry/')
        self.assertEqual(json.loads(response.data),
            [{"expiry_date":
                  None,
              "user": {"id": 1,
                       "username": "Bob",
                       "password": "Bob",
                       "email": "Bob@gmail.com",
                       "favourites": []},
              "ingredient": {
                  "name": "pea",
                  "category": {
                      "name": "vegetable"}}},
             {
                 "expiry_date": None,
                 "user": {
                     "id": 1,
                     "username": "Bob",
                     "password": "Bob",
                     "email": "Bob@gmail.com",
                     "favourites": []},
                 "ingredient": {
                     "name": "potato",
                     "category": {
                         "name": "vegetable"}}}])

    def test_get_pantry_ingredients2(self):
        c = Client()
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        api_client = APIClient()
        api_client.force_authenticate(user=self.user2)
        response = api_client.get('/user/pantry/')
        self.assertGreaterEqual(json.loads(response.data), [])

    def test_delete_pantry_ingredient(self):
        c = Client()
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        c.delete('/user/pantry/1/')
        ing = c.get('/user/pantry/1/')
        self.assertContains(ing, "Not found", status_code=404)

    def test_put_ingredient(self):
        c = Client()
        ingredient_data = {'user': "1", "ingredient": "potato"}
        c.post('/user/pantry/', json.dumps(ingredient_data),
               content_type='application/json')
        ingredient_data = {'expiry_date': '2020-06-20',
                           'user': "1", "ingredient": "potato"}
        ing = c.put('/user/pantry/1/', json.dumps(ingredient_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
                                          "password": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())
