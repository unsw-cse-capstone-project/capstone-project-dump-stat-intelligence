from django.test import TestCase, Client
from rest_framework.test import force_authenticate, APIClient
from .models import *
from .views import *
import json


# Tests for the user login, logout, register and retrieve, put, list, delete
# functionality
class UserTestCase(TestCase):

    # Test checking users can be created and return correct contents
    def test_create_user(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user_data2 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1 = {'username': 'Bob', 'email' : 'save_a_piece@forme.com'}
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())
        user = c.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        user_data2 = {'username': 'Bob1', 'email' : 'save_a_piece@forme.com'}
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data2.items())
        user = User.objects.get(pk=1)
        self.assertIsNotNone(user)

    # Test checking that users can log in with their username and password
    # and have a token returned to frontend
    def test_login_user1(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1.pop('email')
        response = c.post('/user/login/', json.dumps(user_data1),
                       content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')

    # Test checking that incorrect username will make login unsuccessful
    def test_login_user2(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user_data1.pop('email')
        response = c.post('/user/login/', json.dumps(user_data1),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test checking that incorrect password will make login unsuccessful
    def test_login_user3(self):
        c = Client()
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user = c.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese1', 'email'
        : 'save_a_piece@forme.com'}
        user_data1.pop('email')
        response = c.post('/user/login/', json.dumps(user_data1),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test checking that logout destroys the token permission for the
    # previously logged in user
    def test_logout_user(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        response = api_client.post('/user/logout/')
        ingredient_data = {'user': "1", "ingredient": "potato"}
        r = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertEqual(response.status_code, 405)

    # Test checking that a user can retrieve the details of a user
    def test_get_user(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        user = api_client.get('/user/1/')
        user_data1 = {'username': 'Bob', 'email' : 'Bob@gmail.com'}
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())

    # Test checking that a user cannot access the full list of users
    def test_get_users(self):
        api_client1 = APIClient()
        user_data1 = {'username' : 'Bob1', 'password' : 'Bob', 'email':
            'Bob1@gmail.com'}
        user = api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1.pop('email')
        token = api_client1.post('/user/login/', json.dumps(user_data1),
               content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        api_client2 = APIClient()
        user_data2 = {'username': 'Bob2', 'password': 'extra_cheese', 'email'
        : 'Bob2@forme.com'}
        user = api_client2.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        users = api_client1.get('/user/')
        self.assertContains(users, text='', status_code=403)

    # Test checking that a user can delete a user (not yet implemented to
    # only allow deletion of self)
    def test_delete_user1(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        api_client.delete('/user/1/')
        user = api_client.get('/user/1/')
        self.assertContains(user, '', status_code=401)

    # Test checking that a user can delete only themselves
    def test_delete_user2(self):
        api_client1 = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        token = api_client1.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        api_client2 = APIClient()
        user_data1 = {'username' : 'Bob1', 'password' : 'Bob1', 'email':
            'Bob1@gmail.com'}
        token = api_client2.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        response = api_client2.delete('/user/1/')
        self.assertContains(response, '', status_code=401)
        user = api_client2.get('/user/1/')
        self.assertContains(user, '', status_code=200)
        response = api_client2.delete('/user/2/')
        user = api_client1.get('/user/2/')
        self.assertContains(user, '', status_code=404)

    # Test checking that a user can update a user's details (not yet
    # implemented to only allow update of self)
    def test_put_user1(self):
        api_client = APIClient()
        user_data = {'username' : 'Cob', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        user = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        user_data1 = {'username': 'Cob', 'password': 'Cob1', 'email'
        : 'Cob@gmail.com'}
        user = api_client.put('/user/1/', json.dumps(user_data1),
                     content_type='application/json')
        user_data1 = {'username': 'Cob', 'email'
        : 'Cob@gmail.com'}
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())
        api_client.post('/user/logout/')
        api_client1 = APIClient()
        user_data1 = {'username': 'Cob', 'password': 'Cob1'}
        token = api_client1.post('/user/login/', json.dumps(user_data1),
               content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        self.assertContains(token, '', status_code=200)
        response = api_client1.get('/user/1/')
        self.assertContains(response, '', status_code=200)

    # Test checking that a user can update a user's details (not yet
    # implemented to only allow update of self)
    def test_put_user2(self):
        api_client1 = APIClient()
        user_data = {'username' : 'Cob', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        token = api_client1.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        api_client2 = APIClient()
        user_data = {'username' : 'Tob', 'password' : 'Tob', 'email':
            'Tob@gmail.com'}
        token = api_client2.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        user_data = {'username' : 'Cob1', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        user = api_client2.put('/user/1/', json.dumps(user_data),
                     content_type='application/json')
        user_data.pop('password')
        # self.assertContains(user, '', status_code=401)
        response = api_client1.get('/user/1/')
        self.assertContains(response, '', status_code=200)


# Tests for ingredient create, retrieve, list, delete and put
class IngredientTest(TestCase):
    def setUp(self) -> None:
        cat = IngredientCategory.objects.create(name='grain')
        cat = IngredientCategory.objects.create(name='vegetable')
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')

    # Test that a user is able to create a new ingredient (necessary for
    # expansion of ingredient database)
    def test_create_ingredient1(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        ing = api_client.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a new ingredient can be made with a new category
    def test_create_ingredient2(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'not_grain'}}
        ing = api_client.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a user can retrieve a specific ingredient by name
    def test_get_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ing = api_client.get('/ingredients/potato/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a user can retrieve a list of all ingredients and their
    # categories
    def test_get_ingredients(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data1 = {'name': 'potato', 'category': {'name': 'grain'}}
        ingredient_data2 = {'name': 'beef', 'category': {'name': 'grain'}}
        api_client.post('/ingredients/', json.dumps(ingredient_data1),
               content_type='application/json')
        api_client.post('/ingredients/', json.dumps(ingredient_data2),
               content_type='application/json')
        ing = api_client.get('/ingredients/')
        self.assertGreaterEqual(json.loads(ing.content)['results'][1].items(),
                                ingredient_data1.items())
        self.assertGreaterEqual(json.loads(ing.content)['results'][0].items(),
                                ingredient_data2.items())

    # Test that a user can delete an ingredient type (probably should be
    # restricted to ones they've added)
    def test_delete_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        api_client.delete('/ingredients/potato/')
        ing = api_client.get('/ingredients/potato/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update an ingredient's category if misplaced
    def test_put_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'vegetable'}}
        ing = api_client.put('/ingredients/potato/', json.dumps(ingredient_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())


# Test for create, get, list, delete and put for recipes
class RecipeTest(TestCase):
    def setUp(self) -> None:
        meal_cat = MealCategory.objects.create(name="lunch")
        meal_cat2 = MealCategory.objects.create(name="dinner")
        diet_req = DietaryRequirement.objects.create(name="vegan")
        diet_req = DietaryRequirement.objects.create(name="vegetarian")
        self.api_client1 = APIClient()
        user_data1 = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user = self.api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1.pop('email')
        token = self.api_client1.post('/user/login/', json.dumps(user_data1),
               content_type='application/json')
        self.api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        self.api_client2 = APIClient()
        user_data2 = {'username' : 'Tob', 'password' : 'Tob', 'email':
            'Tob@gmail.com'}
        user = self.api_client2.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        user_data2.pop('email')
        token = self.api_client2.post('/user/login/', json.dumps(user_data2),
               content_type='application/json')
        self.api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_cat = IngredientCategory.objects.create(name="vegetable")
        ingredient = IngredientSerializer(data={"name": "potato", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name": "pea", "category":
            {"name": "vegetable"}})
        ingredient.is_valid()
        ingredient.save()

    # Test that a user can create a new recipe and the recipe details are
    # returned correctly
    def test_create_recipe(self):
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "potato"},
                            {"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        ing = self.api_client1.post('/recipes/', json.dumps(recipe_data),
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

    # Test that a user can retrieve a recipe (notably does not need to be
    # logged in)
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
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        ing = self.api_client1.post('/recipes/', json.dumps(recipe_data),
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

    # Test that a user can retrieve a list of recipes (notably does not need
    # to be logged in)
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
                        'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        recipe_data2 = {"name": "Cold ham water", "cook_time": "2 hours",
                        "method": "Put in cold water", "author": "1",
                        "ingredients":
                            [{"adjective": "moldy", "unit": "g",
                              "amount": "20", "ingredient":
                                  "potato"}],
                        'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        self.api_client1.post('/recipes/', json.dumps(recipe_data1),
               content_type='application/json')
        self.api_client1.post('/recipes/', json.dumps(recipe_data2),
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

    # Test that a user can delete a recipe (not yet implemented to restrict
    # to only recipes they've made)
    def test_delete_recipe(self):
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "potato"},
                            {"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        self.api_client1.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        self.api_client1.delete('/recipes/1/')
        ing = self.api_client1.get('/recipes/1/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update a recipe's details (not yet implemented to
    # restrict to recipes they've made)
    def test_put_recipe(self):
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "10", "ingredient":
                                 "potato"}],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        self.api_client1.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        recipe_data = {"name": "Cold ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "2", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'meal_cat': [{"name": "lunch"}, {"name": "dinner"}],
                       'diet_req': [{"name": "vegetarian"}]}
        ing = self.api_client1.put('/recipes/1/', json.dumps(recipe_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"id": 1, "name": "Cold ham water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author": {"id": 2, "username": "Tob",
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


# Tests for create, delete, put, retrieve and list for pantry ingredients
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
        c = Client()
        user_data = {'username' : 'Bob', 'email' : 'Bob@gmail.com',
                     'password' : 'Bob'}
        c.post('/user/register/', json.dumps(user_data),
               content_type='application/json')
        user_data = {'username' : 'Tob', 'email' : 'Tob@gmail.com',
                     'password' : 'Tob'}
        c.post('/user/register/', json.dumps(user_data),
               content_type='application/json')

    # Test that a user can create a pantry ingredient (notably needs to be
    # logged in as anonymous pantry is handled on frontend)
    def test_create_pantry_ingredient1(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        ingredient_data = {'expiry_date': '2020-06-20', 'user': '1',
                           'ingredient': 'potato'}
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                              content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user does not need to enter in expiry date when creating an
    # ingredient
    def test_create_pantry_ingredient2(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        ingredient_data = {'user': "1", "ingredient": "potato"}
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user can retrieve a pantry ingredient
    def test_get_pantry_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        ing = api_client.get('/user/pantry/1/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com",
                                          "favourites": []},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user can get a list of their pantry ingredients
    def test_get_pantry_ingredients1(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}
        ingredient_data3 = {'user': "1", "ingredient": "chick"}
        ingredient_data4 = {'user': "1", "ingredient": "x"}
        ingredient_data5 = {'user': "1", "ingredient": "z"}
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data3),
                     content_type='application/json')
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data4),
                     content_type='application/json')
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data5),
                     content_type='application/json')
        response = api_client.get('/user/pantry/')
        self.assertEqual(response.data,
            [
             {
                 "id" : 5,
                 "expiry_date": None,
                 "user": {
                     "id": 1,
                     "username": "Bob",
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
                     "email": "Bob@gmail.com",
                     "favourites": []},
                 "ingredient": {
                     "name": "x",
                     "category": {
                         "name": "zeta"}}}])

    # Test that a user cannot get a list of other user's pantry ingredients
    def test_get_pantry_ingredients2(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        response = api_client.get('/user/pantry/')
        self.assertGreaterEqual(response.data, [])

    # Test that a user can delete a pantry ingredient (not yet implemented to
    # restrict to user's pantry ingredients)
    def test_delete_pantry_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        api_client.delete('/user/pantry/1/')
        ing = api_client.get('/user/pantry/1/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update a pantry ingredient (not yet implemented to
    # restrict to user's pantry ingredient)
    def test_put_pantry_ingredient(self):
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        ingredient_data = {'user': "1", "ingredient": "potato"}
        api_client.post('/user/pantry/', json.dumps(ingredient_data),
               content_type='application/json')
        ingredient_data = {'expiry_date': '2020-06-20',
                           'user': "1", "ingredient": "potato"}
        ing = api_client.put('/user/pantry/1/', json.dumps(ingredient_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
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
        carrot = Ingredient(name="cgit checarrot", category=vegetable)
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