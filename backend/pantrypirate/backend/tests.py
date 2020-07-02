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
class IngredientTest(TestCase):
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
class RecipeTest(TestCase):
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
        self.assertGreaterEqual(json.loads(ing.content)[1].items(),
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
        self.assertGreaterEqual(json.loads(ing.content)[0].items(),
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
        cat = IngredientCategory.objects.create(name='alpha')
        cat = IngredientCategory.objects.create(name='zeta')
        ingredient = IngredientSerializer(data={"name": "potato", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "pea", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "chick", "category":
            {"name": "grain"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "x", "category":
            {"name": "zeta"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "z", "category":
            {"name": "alpha"}})
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

    def test_get_pantry_ingredient(self):
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
        ingredient_data3 = {'user': "1", "ingredient": "chick"}
        ingredient_data4 = {'user': "1", "ingredient": "x"}
        ingredient_data5 = {'user': "1", "ingredient": "z"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data3),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data4),
                     content_type='application/json')
        ing = c.post('/user/pantry/', json.dumps(ingredient_data5),
                     content_type='application/json')
        api_client = APIClient()
        api_client.force_authenticate(user=self.user1)
        response = api_client.get('/user/pantry/')
        self.assertEqual(response.data,
            [
             {
                 "id" : 5,
                 "expiry_date": None,
                 "user": {
                     "id": 1,
                     "username": "Bob",
                     "password": "Bob",
                     "email": "Bob@gmail.com",
                     "favourites": []},
                 "ingredient": {
                     "name": "z",
                     "category": {
                         "name": "alpha"}}},
             {
                 "id" : 3,
                 "expiry_date": None,
                 "user": {
                     "id": 1,
                     "username": "Bob",
                     "password": "Bob",
                     "email": "Bob@gmail.com",
                     "favourites": []},
                 "ingredient": {
                     "name": "chick",
                     "category": {
                         "name": "grain"}}},
             {
                 "id" : 2,
                 "expiry_date":
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
                 "id" : 1,
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
                         "name": "vegetable"}}},
             {
                 "id" : 4,
                 "expiry_date": None,
                 "user": {
                     "id": 1,
                     "username": "Bob",
                     "password": "Bob",
                     "email": "Bob@gmail.com",
                     "favourites": []},
                 "ingredient": {
                     "name": "x",
                     "category": {
                         "name": "zeta"}}}])

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
        self.assertGreaterEqual(response.data, [])

    def test_delete_pantry_ingredient(self):
        c = Client()
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = c.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        c.delete('/user/pantry/1/')
        ing = c.get('/user/pantry/1/')
        self.assertContains(ing, "Not found", status_code=404)

    def test_put_pantry_ingredient(self):
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


# Testing searching
class SearchTestCase(TestCase):
    def setUp(self):

        # set up meal categories and dietary requirements
        breakfast = MealCategory.objects.create(name="breakfast")
        lunch = MealCategory.objects.create(name="lunch")
        dessert = MealCategory.objects.create(name="dessert")
        vegan = DietaryRequirement.objects.create(name="vegan")
        dairy_free = DietaryRequirement.objects.create(name="dairy-free")

        # set up user
        jess = User.objects.create(username="Jess", email="jess@gmail.com",
                                   password="1234")

        # set up recipes
        fruit_salad = Recipe(name="Fruit salad", cook_time="30 minutes", method="Yummy yummy", author=jess)
        fruit_salad.save()
        fruit_salad.meal_cat.add(breakfast)
        fruit_salad.diet_req.add(vegan)
        fruit_salad.diet_req.add(dairy_free)

        garden_salad = Recipe(name="Garden salad", cook_time="30 minutes", method="Crunch crunch", author=jess)
        garden_salad.save()
        garden_salad.meal_cat.add(lunch)
        garden_salad.diet_req.add(vegan)
        garden_salad.diet_req.add(dairy_free)

        mixed_salad = Recipe(name="Mixed salad", cook_time="30 minutes", method="Yummy crunch?", author=jess)
        mixed_salad.save()
        mixed_salad.meal_cat.add(lunch)
        mixed_salad.diet_req.add(vegan)
        mixed_salad.diet_req.add(dairy_free)

        # set up recipe ingredients
        fruit = IngredientCategory.objects.create(name="fruit")
        fruit.save()
        apple = Ingredient(name="apple", category=fruit)
        apple.save()
        pear = Ingredient(name="pear", category=fruit)
        pear.save()

        vegetable = IngredientCategory.objects.create(name="vegetable")
        vegetable.save()
        tomato = Ingredient(name="tomato", category=vegetable)
        tomato.save()
        carrot = Ingredient(name="carrot", category=vegetable)
        carrot.save()

        r_apple = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=apple, recipe=fruit_salad)
        r_apple.save()
        r_pear = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=pear, recipe=fruit_salad)
        r_pear.save()

        r_tomato = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=tomato, recipe=garden_salad)
        r_tomato.save()
        r_carrot = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=carrot, recipe=garden_salad)
        r_carrot.save()

        r_mixed_apple = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=apple, recipe=mixed_salad)
        r_mixed_apple.save()
        r_mixed_carrot = RecipeIngredient(adjective="chopped", unit="whole", amount="3", ingredient=carrot, recipe=mixed_salad)
        r_mixed_carrot.save()

        # make pantry ingredients
        p_apple = PantryIngredient(expiry_date="2020-07-29", user=jess, ingredient=apple)
        p_apple.save()
        p_pear = PantryIngredient(expiry_date="2020-07-29", user=jess, ingredient=pear)
        p_pear.save()
        p_carrot = PantryIngredient(expiry_date="2020-07-29", user=jess, ingredient=carrot)
        p_carrot.save()
        p_tomato = PantryIngredient(expiry_date="2020-07-29", user=jess, ingredient=tomato) # WON'T add tomato to running list
        p_tomato.save()

    def test_search(self):
        c = Client()

        # extract pantry items
        p_apple = PantryIngredient.objects.get(pk=1)
        p_pear = PantryIngredient.objects.get(pk=2)
        p_carrot = PantryIngredient.objects.get(pk=3)

        running_list = {p_apple.ingredient.name : p_apple.pk, p_pear.ingredient.name : p_pear.pk, p_carrot.ingredient.name : p_carrot.pk}

        response = c.get('/recipes/?ingredients=1+2+3&meal=dinner+lunch&diet=vegan&limit=10&offset=21/',
                         header=json.dumps(running_list),
                         content_type="application/json")
        expected_response = ['Garden salad', 'Mixed salad']
        self.assertEqual(json.loads(response.content), expected_response)