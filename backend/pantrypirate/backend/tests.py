from django.test import TestCase, Client
from rest_framework.test import force_authenticate, APIClient
from .models import *
from .views import *
import json


# Tests for the user login, logout, register and retrieve, put, list, delete
# functionality
class UserTestCase(TestCase):

    # Test checking users can be created and return correct contents
    def test_create_user1(self):
        # Create testing client and expected responses
        c = Client()
        expected_response = {'id' : '1'}

        # Data for an account
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}

        # Request registration and check response is expected
        response = c.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1 = {'username': 'Bob', 'email' : 'save_a_piece@forme.com'}
        self.assertGreaterEqual(json.loads(response.content).items(),
                                user_data1.items())

        # Check user exists with correct details
        user = User.objects.get(pk=1)
        self.assertIsNotNone(user)

    # Test checking users cannot create account if logged in
    def test_create_user2(self):
        # Create testing client and expected responses
        api_client = APIClient()
        expected_response = {'id': 1}

        # Data for the two accounts
        user_data1 = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        user_data2 = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece1@forme.com'}

        # Request registration and check response is expected
        token = api_client.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        self.assertGreaterEqual(json.loads(token.content).items(),
                                expected_response.items())

        # Attempt to register again and verify not allowed
        response = api_client.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        self.assertContains(response, '', status_code=401)

    # Test checking that users can log in with their username and password
    # and have a token returned to frontend
    def test_login_user1(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account
        user_data = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}

        # Register account but do not authorise
        _ = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')

        # Log in and authorise
        token = api_client.post('/user/login/', json.dumps(user_data),
                       content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Test authorisation successful
        self.assertEqual(token.status_code, 200)
        self.assertContains(token, '1')
        self.assertIsNotNone(json.loads(token.content)['token'])

    # Test checking that incorrect username will make login unsuccessful
    def test_login_user2(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account
        user_data = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        wrong_login = {'username': 'Bob1', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}

        # Register account but do not authorise
        _ = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')

        # Attempt to log in with wrong details
        response = api_client.post('/user/login/', json.dumps(wrong_login),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test checking that incorrect password will make login unsuccessful
    def test_login_user3(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account
        user_data = {'username': 'Bob', 'password': 'extra_cheese', 'email'
        : 'save_a_piece@forme.com'}
        wrong_login = {'username': 'Bob', 'password': 'extra_cheese1', 'email'
        : 'save_a_piece@forme.com'}

        # Register account but do not authorise
        _ = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')

        # Attempt to log in with wrong details
        response = api_client.post('/user/login/', json.dumps(wrong_login),
                       content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test checking that logout destroys the token permission for the
    # previously logged in user
    def test_logout_user(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        ingredient_data = {'user': "1", "ingredient": "potato"}

        # Register account and log in
        _ = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        user_data.pop('email')
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to log out and verify permissions revoked
        _ = api_client.post('/user/logout/')
        response = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test checking that a user can retrieve the details of a user
    def test_get_user(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        test_data = {'username': 'Bob', 'email' : 'Bob@gmail.com'}

        # Register account and log in
        token = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Fetch user instance and check data is correct
        user = api_client.get('/user/1/')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                test_data.items())

    # Test checking that a user cannot access the full list of users
    def test_get_users(self):
        # Create testing client
        api_client1 = APIClient()

        # Data for the account and testing
        user_data1 = {'username' : 'Bob1', 'password' : 'Bob', 'email':
            'Bob1@gmail.com'}
        token = api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Fetch user instances and check access forbidden
        users = api_client1.get('/user/')
        self.assertContains(users, text='', status_code=403)

    # Test checking that a user can delete a user
    def test_delete_user1(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        token = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Delete user instance and verify deleted/logged out
        response = api_client.delete('/user/1/')
        self.assertContains(response, '', status_code=204)
        user = api_client.get('/user/1/')
        self.assertContains(user, '', status_code=401)

    # Test checking that a user can delete only themselves
    def test_delete_user2(self):
        # Create testing clients
        api_client1 = APIClient()
        api_client2 = APIClient()

        # Data for the accounts and testing
        user_data1 = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user_data2 = {'username' : 'Bob1', 'password' : 'Bob1', 'email':
            'Bob1@gmail.com'}

        # Register and log in users
        token = api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        token = api_client2.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to delete other user and verify forbidden
        response = api_client2.delete('/user/1/')
        self.assertContains(response, '', status_code=401)

        # Verify user still exists
        user = api_client2.get('/user/1/')
        self.assertContains(user, '', status_code=200)

        # Attempt to delete self
        _ = api_client2.delete('/user/2/')

        # Verify user does not exist
        user = api_client1.get('/user/2/')
        self.assertContains(user, '', status_code=404)

    # Test checking that a user can update a user's details
    def test_put_user1(self):
        # Create testing clients
        api_client = APIClient()
        api_client1 = APIClient()

        # Data for the accounts and testing
        user_data = {'username' : 'Cob', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        change_data = {'username': 'Cob1', 'password': 'Cob', 'email'
        : 'Cob@gmail.com'}
        test_data = {'username': 'Cob1', 'email'
        : 'Cob@gmail.com'}
        new_user_data = {'username': 'Cob1', 'password': 'Cob'}

        # Register and log in user
        token = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to change details and verify returned are correct
        user = api_client.put('/user/1/', json.dumps(change_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                test_data.items())

        # Log user out and log in again and verify they are logged in
        api_client.post('/user/logout/')
        token = api_client1.post('/user/login/', json.dumps(new_user_data),
               content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        self.assertContains(token, '', status_code=200)

        # Attempt to retrieve user details and verify they are correct
        response = api_client1.get('/user/1/')
        self.assertContains(response, '', status_code=200)
        self.assertGreaterEqual(json.loads(response.content).items(),
                                test_data.items())

    # Test checking that a user can only update their details
    def test_put_user2(self):
        # Create testing clients
        api_client1 = APIClient()
        api_client2 = APIClient()

        # Data for the accounts and testing
        user_data1 = {'username' : 'Cob', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        user_data2 = {'username' : 'Tob', 'password' : 'Tob', 'email':
            'Tob@gmail.com'}
        change_data1 = {'username' : 'Cob1', 'password' : 'Cob', 'email':
            'Cob@gmail.com'}
        test_data1 = {'username' : 'Cob', 'email': 'Cob@gmail.com'}
        test_data2 = {'username' : 'Cob1', 'email': 'Cob@gmail.com'}

        # Register and log in users
        token = api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        token = api_client2.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to change another user's details and verify forbidden
        user = api_client2.put('/user/1/', json.dumps(change_data1),
                     content_type='application/json')
        self.assertContains(user, '', status_code=401)

        # Get own user details and verify they aren't changed
        response = api_client1.get('/user/1/')
        self.assertContains(response, '', status_code=200)
        self.assertGreaterEqual(json.loads(response.content).items(),
                                test_data1.items())

        # Attempt to change own data
        _ = api_client1.put('/user/1/', json.dumps(change_data1),
                     content_type='application/json')
        response = api_client1.get('/user/1/')
        self.assertGreaterEqual(json.loads(response.content).items(),
                                test_data2.items())


class IngredientCategoryTest(TestCase):
    # Test that ingredient categories can contain spaces
    def test_create_ingredient_category(self):
        _ = IngredientCategory.objects.create(name='spices and seasoning')
        cat = IngredientCategory.objects.filter(name='spices and seasoning')
        if not cat:
            self.assertIsNone(1)


# Tests for ingredient create, retrieve, list, delete and put
class IngredientTest(TestCase):
    def setUp(self) -> None:
        # Create ingredient categories to allow ingredient creation
        _ = IngredientCategory.objects.create(name='grain')
        _ = IngredientCategory.objects.create(name='vegetable')
        _ = IngredientCategory.objects.create(name='not vegetable')

        # Create user for testing purposes
        api_client = APIClient()
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        _ = api_client.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        _ = api_client.post('/user/logout/')

    # Test that a user is able to create a new ingredient (necessary for
    # expansion of ingredient database)
    def test_create_ingredient1(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create ingredient and verify the return is correct
        ing = api_client.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a new ingredient can be made with a new category
    def test_create_ingredient2(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'not_grain'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create ingredient and verify the return is correct
        ing = api_client.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a new ingredient can be made with an old category with a
    # space in it
    def test_create_ingredient3(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name':
                                                              'not vegetable'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create ingredient and verify the return is correct
        ing = api_client.post('/ingredients/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a user can retrieve a specific ingredient by name
    def test_get_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and retrieve ingredient and verify the return is
        # correct
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ing = api_client.get('/ingredients/potato/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    # Test that a user can retrieve a list of all ingredients and their
    # categories
    def test_get_ingredients(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data1 = {'name': 'potato', 'category': {'name': 'grain'}}
        ingredient_data2 = {'name': 'beef', 'category': {'name': 'grain'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and retrieve ingredients and verify the return is
        # correct
        api_client.post('/ingredients/', json.dumps(ingredient_data1),
               content_type='application/json')
        api_client.post('/ingredients/', json.dumps(ingredient_data2),
               content_type='application/json')
        ing = api_client.get('/ingredients/')
        self.assertGreaterEqual(json.loads(ing.content)[1].items(),
                                ingredient_data1.items())
        self.assertGreaterEqual(json.loads(ing.content)[0].items(),
                                ingredient_data2.items())

    # Test that a user can delete an ingredient type (probably should be
    # restricted to ones they've added)
    def test_delete_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create, delete retrieve ingredients and verify there is
        # no ingredient
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        api_client.delete('/ingredients/potato/')
        ing = api_client.get('/ingredients/potato/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update an ingredient's category if misplaced
    def test_put_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'name': 'potato', 'category': {'name': 'grain'}}
        update_data = {'name': 'potato', 'category': {'name':
                                                              'vegetable'}}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and update an ingredient and verify return is
        # correct
        api_client.post('/ingredients/', json.dumps(ingredient_data),
               content_type='application/json')
        ing = api_client.put('/ingredients/potato/', json.dumps(update_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                update_data.items())


# Test for create, get, list, delete and put for recipes
class RecipeTest(TestCase):
    def setUp(self) -> None:
        # Create meal categories and dietary requirements
        _ = MealCategory.objects.create(name="lunch")
        _ = MealCategory.objects.create(name="dinner")
        _ = DietaryRequirement.objects.create(name="vegan")
        _ = DietaryRequirement.objects.create(name="vegetarian")

        # Create two users
        self.api_client1 = APIClient()
        self.api_client2 = APIClient()

        user_data1 = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}
        user_data2 = {'username' : 'Tob', 'password' : 'Tob', 'email':
            'Tob@gmail.com'}

        token = self.api_client1.post('/user/register/', json.dumps(user_data1),
                      content_type='application/json')
        self.api_client1.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])
        token = self.api_client2.post('/user/register/', json.dumps(user_data2),
                      content_type='application/json')
        self.api_client2.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Create ingredient category
        _ = IngredientCategory.objects.create(name="vegetable")

        # Create ingredients
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
        # Data for recipe
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

        # Attempt to create the recipe
        ing = self.api_client1.post('/recipes/', json.dumps(recipe_data),
                     content_type='application/json')

        # Verify that the return matches the input
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
                  "email": "Bob@gmail.com"},
             "meal_cat": [{
                 "name": "dinner"}],
             "diet_req":
                 [{
                     "name": "vegan"}],
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
        # Data for recipe
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

        # Attempt to create and get the recipe
        _ = self.api_client1.post('/recipes/', json.dumps(recipe_data),
                     content_type='application/json')
        ing = self.api_client1.get('/recipes/1/')

        # Verify that the return matches the input
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
                  "email": "Bob@gmail.com"},
             "image_URL": None,
             "meal_cat": [{
                 "name": "dinner"}],
             "diet_req":
                 [{
                     "name": "vegan"}],
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
        # Data for recipes
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

        # Attempt to create and get the recipes
        self.api_client1.post('/recipes/', json.dumps(recipe_data1),
               content_type='application/json')
        self.api_client1.post('/recipes/', json.dumps(recipe_data2),
               content_type='application/json')
        ing = self.api_client1.get('/recipes/')

        # Verify that the return matches the input
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
                  "email": "Bob@gmail.com"},
             "image_URL": None,
             "meal_cat": [{
                 "name": "dinner"}],
             "diet_req":
                 [{
                     "name": "vegan"}],
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
                  "email": "Bob@gmail.com"},
             "image_URL": None,
             "meal_cat": [{
                 "name": "dinner"}],
             "diet_req":
                 [{
                     "name": "vegan"}],
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
        # Data for recipes
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

        # Attempt to create and delete a recipe
        self.api_client1.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        self.api_client1.delete('/recipes/1/')
        ing = self.api_client1.get('/recipes/1/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update a recipe's details (not yet implemented to
    # restrict to recipes they've made)
    def test_put_recipe(self):
        # Data for recipes
        recipe_data = {"name": "Hot ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "1", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "10", "ingredient":
                                 "potato"}],
                       'meal_cat': [{"name": "dinner"}], 'diet_req': [{
                "name": "vegan"}]}
        change_data = {"name": "Cold ham water", "cook_time": "2 hours",
                       "method": "Put in water", "author": "2", "ingredients":
                           [{"adjective": "moldy", "unit": "g",
                             "amount": "20", "ingredient":
                                 "pea"}],
                       'meal_cat': [{"name": "lunch"}, {"name": "dinner"}],
                       'diet_req': [{"name": "vegetarian"}]}

        # Attempt to create and change the recipes and verify current output
        self.api_client1.post('/recipes/', json.dumps(recipe_data),
               content_type='application/json')
        ing = self.api_client1.put('/recipes/1/', json.dumps(change_data),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"id": 1, "name": "Cold ham water",
                                 "cook_time": "2 hours",
                                 "method": "Put in water",
                                 "author": {"id": 2, "username": "Tob",
                                            "email": "Tob@gmail.com"},
                                 "image_URL": None,
                                 "meal_cat": [{"name": "dinner"},
                                              {"name": "lunch"}],
                                 "diet_req": [{"name": "vegetarian"}],
                                 "ingredients": [
                                     {"adjective": "moldy", "unit": "g",
                                      "amount": "20", "recipe": 1,
                                      "ingredient": {"name": "pea",
                                                     "category": {
                                                         "name": "vegetable"}}}]}.items())


# Tests for create, delete, put, retrieve and list for pantry ingredients
class PantryIngredientTest(TestCase):
    def setUp(self) -> None:
        # Create ingredient categories
        _ = IngredientCategory.objects.create(name='grain')
        _ = IngredientCategory.objects.create(name='vegetable')
        _ = IngredientCategory.objects.create(name='alpha')
        _ = IngredientCategory.objects.create(name='zeta')

        # Create ingredients
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

        # Create users
        c = Client()
        user_data = {'username' : 'Bob', 'email' : 'Bob@gmail.com',
                     'password' : 'Bob'}
        c.post('/user/register/', json.dumps(user_data),
               content_type='application/json')
        c.post('/user/logout/')
        user_data = {'username' : 'Tob', 'email' : 'Tob@gmail.com',
                     'password' : 'Tob'}
        c.post('/user/register/', json.dumps(user_data),
               content_type='application/json')
        c.post('/user/logout/')

    # Test that a user can create a pantry ingredient (notably needs to be
    # logged in as anonymous pantry is handled on frontend)
    def test_create_pantry_ingredient1(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'expiry_date': '2020-06-20', 'user': '1',
                           'ingredient': 'potato'}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create an ingredient and verify output is correct
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                              content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com"},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user does not need to enter in expiry date when creating an
    # ingredient
    def test_create_pantry_ingredient2(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'user': "1", "ingredient": "potato"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create an ingredient and verify output is correct
        ing = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com"},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user can retrieve a pantry ingredient
    def test_get_pantry_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'user': "1", "ingredient": "potato"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and retrieve an ingredient and verify output is
        # correct
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        ing = api_client.get('/user/pantry/1/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": None,
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com"},
                                 "ingredient": {"name": "potato", "category": {
                                     "name": "vegetable"}}}.items())

    # Test that a user can get a list of their pantry ingredients
    def test_get_pantry_ingredients1(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}
        ingredient_data3 = {'user': "1", "ingredient": "chick"}
        ingredient_data4 = {'user': "1", "ingredient": "x"}
        ingredient_data5 = {'user': "1", "ingredient": "z"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and retrieves ingredients and verify output is
        # correct
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data3),
                     content_type='application/json')
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data4),
                     content_type='application/json')
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data5),
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
                     "email": "Bob@gmail.com"},
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
                     "email": "Bob@gmail.com"},
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
                          "email": "Bob@gmail.com"},
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
                     "email": "Bob@gmail.com"},
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
                     "email": "Bob@gmail.com"},
                 "ingredient": {
                     "name": "x",
                     "category": {
                         "name": "zeta"}}}])

    # Test that a user cannot get a list of other user's pantry ingredients
    def test_get_pantry_ingredients2(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data1 = {'user': "1", "ingredient": "potato"}
        ingredient_data2 = {'user': "1", "ingredient": "pea"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create ingredients and retrieve
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data1),
                     content_type='application/json')
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data2),
                     content_type='application/json')
        response = api_client.get('/user/pantry/')
        self.assertGreaterEqual(response.data, [])

    # Test that a user can delete a pantry ingredient (not yet implemented to
    # restrict to user's pantry ingredients)
    def test_delete_pantry_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'user': "1", "ingredient": "potato"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and delete an ingredient
        _ = api_client.post('/user/pantry/', json.dumps(ingredient_data),
                     content_type='application/json')
        api_client.delete('/user/pantry/1/')
        ing = api_client.get('/user/pantry/1/')
        self.assertContains(ing, "Not found", status_code=404)

    # Test that a user can update a pantry ingredient (not yet implemented to
    # restrict to user's pantry ingredient)
    def test_put_pantry_ingredient(self):
        # Create testing client
        api_client = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob'}
        ingredient_data = {'user': "1", "ingredient": "potato"}
        ingredient_data1 = {'expiry_date': '2020-06-20',
                           'user': "1", "ingredient": "potato"}

        # Log in and authorise user
        token = api_client.post('/user/login/', json.dumps(user_data),
               content_type='application/json')
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to create and update an ingredient
        api_client.post('/user/pantry/', json.dumps(ingredient_data),
               content_type='application/json')
        ing = api_client.put('/user/pantry/1/', json.dumps(ingredient_data1),
                    content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                {"expiry_date": "2020-06-20",
                                 "user": {"id": 1, "username": "Bob",
                                          "email": "Bob@gmail.com"},
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
        self.c = APIClient()
        user_data = {'username' : 'Jess', 'email' : 'jess@gmail.com', 'password' : '1111'}
        user = self.c.post('/user/register/', json.dumps(user_data), content_type='application/json')
        user_data.pop('email')      
        token = self.c.post('/user/login/', json.dumps(user_data), content_type='application/json')
        self.c.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        user = User.objects.get(pk=1)

        # set up recipes
        fruit_salad = Recipe(name="Fruit salad", cook_time="30 minutes", method="Yummy yummy", author=user)
        fruit_salad.save()
        fruit_salad.meal_cat.add(breakfast)
        fruit_salad.diet_req.add(vegan)
        fruit_salad.diet_req.add(dairy_free)

        garden_salad = Recipe(name="Garden salad", cook_time="30 minutes", method="Crunch crunch", author=user)
        garden_salad.save()
        garden_salad.meal_cat.add(lunch)
        garden_salad.diet_req.add(vegan)
        garden_salad.diet_req.add(dairy_free)

        mixed_salad = Recipe(name="Mixed salad", cook_time="30 minutes", method="Yummy crunch?", author=user)
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
        lemon = Ingredient(name="lemon", category=vegetable)
        lemon.save()

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

    # test with some matching ingredients in running list, should order by percentage
    def test_search1(self):

        response = self.c.get('/recipes/?ingredients=apple,pear,carrot&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 
                                
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"suggestion" : "tomato"}] 

        self.assertEqual(json.loads(response.content), expected_response)

    # test with some matching ingredients in running list, should order by name (% is equal)
    def test_search2(self):

        response = self.c.get('/recipes/?ingredients=carrot&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]}, 
                                
                            {"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["apple"]},
                            
                            {"suggestion" : "tomato"}] 

        self.assertEqual(json.loads(response.content), expected_response)

    # expand meal_cat filter to include all recipes
    def test_search3(self):
        self.maxDiff = None

        response = self.c.get('/recipes/?ingredients=apple,carrot&meal=dinner+lunch+breakfast&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 
                                
                            {"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["pear"]},
                            
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"suggestion" : "pear"}] 

        self.assertEqual(json.loads(response.content), expected_response)

    # test ingredient suggestion, should return most common missing ingredient
    def test_search4(self):

        # add new recipe with tomato
        recipe_data = {"name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "tomato"},
                            {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "ingredient": "lemon"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}

        post = self.c.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        response = self.c.get('/recipes/?ingredients=apple,carrot,lemon&meal=dinner+lunch+breakfast&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 
                                
                            {"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["pear"]},
                            
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"recipe": 
                                {"id": 4, "name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "cups", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}},
                                    {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "lemon", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"suggestion" : "tomato"}] 

        self.assertEqual(json.loads(response.content), expected_response)


    # test ingredient suggestion, should return ingredient from pantry since user is logged in
    def test_search5(self):

        # add things to pantry
        ingredient_data1 = {'user': "1", "ingredient": "apple"}
        ingredient_data2 = {'user': "1", "ingredient": "pear"}
        ingredient_data3 = {'user': "1", "ingredient": "carrot"}
        ingredient_data4 = {'user': "1", "ingredient": "lemon"}
        
        self.c.post('/user/pantry/', json.dumps(ingredient_data1), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data2), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data3), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data4), content_type='application/json')

        # add new recipe with tomato
        recipe_data = {"name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "tomato"},
                            {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "ingredient": "lemon"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}

        post = self.c.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        response = self.c.get('/recipes/?ingredients=apple,carrot,lemon&meal=dinner+lunch+breakfast&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 
                                
                            {"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["pear"]},
                            
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"recipe": 
                                {"id": 4, "name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "cups", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}},
                                    {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "lemon", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.5, 
                            "missing_ing": ["tomato"]},
                            
                            {"suggestion" : "pear"}] 

        self.assertEqual(json.loads(response.content), expected_response)

    # test search returns all recipes when no filters applied
    def test_search6(self):

        # empty search string
        response = self.c.get('/recipes/?ingredients=&meal=&diet=&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 0.0, 
                            "missing_ing": ["apple", "pear"]}, 
                                
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.0, 
                            "missing_ing": ["tomato", "carrot"]},
                            
                            {"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"},
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 0.0, 
                            "missing_ing": ["apple", "carrot"]},
                            
                            {"suggestion" : "apple"}] 

        self.assertEqual(json.loads(response.content), expected_response)

    # make sure search will always return a suggested ingredient, or empty string as last case
    def test_search7(self):

        # add things to pantry
        ingredient_data1 = {'user': "1", "ingredient": "apple"}
        ingredient_data2 = {'user': "1", "ingredient": "pear"}
        ingredient_data3 = {'user': "1", "ingredient": "carrot"}
        ingredient_data4 = {'user': "1", "ingredient": "tomato"}
        
        self.c.post('/user/pantry/', json.dumps(ingredient_data1), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data2), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data3), content_type='application/json')
        self.c.post('/user/pantry/', json.dumps(ingredient_data4), content_type='application/json')

        response = self.c.get('/recipes/?ingredients=apple,tomato,pear,carrot&meal=dinner+lunch+breakfast&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []},
                            
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []},

                            {"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 
                            
                            {"suggestion" : "lemon"}] 

        self.assertEqual(json.loads(response.content), expected_response)

        # now check empty string
        # add recipe with lemon
        recipe_data = {"name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "tomato"},
                            {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "ingredient": "lemon"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}

        post = self.c.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        ingredient_data5 = {'user': "1", "ingredient": "lemon"}
        self.c.post('/user/pantry/', json.dumps(ingredient_data5), content_type='application/json')

        response = self.c.get('/recipes/?ingredients=apple,tomato,pear,carrot,lemon&meal=dinner+lunch+breakfast&diet=vegan&limit=10&offset=0/',
                         content_type="application/json")

        expected_response = [{"recipe": 
                                {"id": 1, "name": "Fruit salad", "cook_time": "30 minutes", "method": "Yummy yummy", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "breakfast"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 1, 
                                        "ingredient": {"name": "pear", "category": {"name": "fruit"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []},
                            
                            {"recipe": 
                                {"id": 2, "name": "Garden salad", "cook_time": "30 minutes", "method": "Crunch crunch", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 2, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []},

                            {"recipe": 
                                {"id": 3, "name": "Mixed salad", "cook_time": "30 minutes", "method": "Yummy crunch?", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "apple", "category": {"name": "fruit"}}}, 
                                    {"adjective": "chopped", "unit": "whole", "amount": "3", "recipe": 3, 
                                        "ingredient": {"name": "carrot", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []}, 

                            {"recipe": 
                                {"id": 4, "name": "Tomato salad", "cook_time": "20 minutes", "method": "Chop tomatoes", 
                                "author": {"id": 1, "username": "Jess", "email": "jess@gmail.com"}, 
                                "image_URL": None,
                                "meal_cat": [{"name": "lunch"}], "diet_req": [{"name": "dairy-free"}, {"name": "vegan"}], 
                                "ingredients": 
                                    [{"adjective": "chopped", "unit": "cups", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "tomato", "category": {"name": "vegetable"}}}, 
                                    {"adjective": "juiced", "unit": "Tbsp", "amount": "2", "recipe": 4, 
                                        "ingredient": {"name": "lemon", "category": {"name": "vegetable"}}}]}, 
                            "match_percentage": 1.0, 
                            "missing_ing": []},
                            
                            {"suggestion" : ""}] 

        self.assertEqual(json.loads(response.content), expected_response)


# Testing search metadata
class MetaSearchTestCase(TestCase):
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
        fruit_salad = Recipe(name="Fruit salad", cook_time="30 minutes",
                             method="Yummy yummy", author=jess)
        fruit_salad.save()
        fruit_salad.meal_cat.add(breakfast)
        fruit_salad.diet_req.add(vegan)
        fruit_salad.diet_req.add(dairy_free)

        garden_salad = Recipe(name="Garden salad", cook_time="30 minutes",
                              method="Crunch crunch", author=jess)
        garden_salad.save()
        garden_salad.meal_cat.add(lunch)
        garden_salad.diet_req.add(vegan)
        garden_salad.diet_req.add(dairy_free)

        mixed_salad = Recipe(name="Mixed salad", cook_time="30 minutes",
                             method="Yummy crunch?", author=jess)
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
        potato = Ingredient(name="potato", category=vegetable)
        potato.save()

        r_apple = RecipeIngredient(adjective="chopped", unit="whole",
                                   amount="3", ingredient=apple,
                                   recipe=fruit_salad)
        r_apple.save()
        r_pear = RecipeIngredient(adjective="chopped", unit="whole", amount="3",
                                  ingredient=pear, recipe=fruit_salad)
        r_pear.save()

        r_tomato = RecipeIngredient(adjective="chopped", unit="whole",
                                    amount="3", ingredient=tomato,
                                    recipe=garden_salad)
        r_tomato.save()
        r_carrot = RecipeIngredient(adjective="chopped", unit="whole",
                                    amount="3", ingredient=carrot,
                                    recipe=garden_salad)
        r_carrot.save()

        r_mixed_apple = RecipeIngredient(adjective="chopped", unit="whole",
                                         amount="3", ingredient=apple,
                                         recipe=mixed_salad)
        r_mixed_apple.save()
        r_mixed_carrot = RecipeIngredient(adjective="chopped", unit="whole",
                                          amount="3", ingredient=carrot,
                                          recipe=mixed_salad)
        r_mixed_carrot.save()

        # make pantry ingredients
        p_apple = PantryIngredient(expiry_date="2020-07-29", user=jess,
                                   ingredient=apple)
        p_apple.save()
        p_pear = PantryIngredient(expiry_date="2020-07-29", user=jess,
                                  ingredient=pear)
        p_pear.save()
        p_carrot = PantryIngredient(expiry_date="2020-07-29", user=jess,
                                    ingredient=carrot)
        p_carrot.save()
        p_tomato = PantryIngredient(expiry_date="2020-07-29", user=jess,
                                    ingredient=tomato)
        p_tomato.save()

    # Test that a full match creates a new MetaSearch object with value 0
    def test_meta_search1(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=apple,carrot&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 0)
        self.assertEqual(json.loads(response.content)['search'], 'apple|carrot')

    # Test that a full match gets an old MetaSearch object with value 0
    def test_meta_search2(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=apple,carrot&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=apple,carrot&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 0)
        self.assertEqual(json.loads(response.content)['search'], 'apple|carrot')

    # Test that no full match creates a new MetaSearch object with value 1
    def test_meta_search3(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=carrot&meal=dinner+lunch&diet=vegan&limit=10'
            '&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 1)
        self.assertEqual(json.loads(response.content)['search'], 'carrot')

    # Test that no full match update an old MetaSearch object with value + 1
    def test_meta_search4(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=carrot&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=carrot&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 2)
        self.assertEqual(json.loads(response.content)['search'], 'carrot')

    # Test that meta search returns highest reference count
    def test_meta_search5(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=carrot&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=pear&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=pear&meal=dinner+lunch&diet=vegan&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 2)
        self.assertEqual(json.loads(response.content)['search'], 'pear')

    # Test that references cannot go below zero
    def test_meta_search6(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=carrot&meal=&diet=&limit=10&offset=0/',
            content_type="application/json")

        # Create recipe simulating user doing so
        author = User.objects.get(username='Jess')
        carrot_rec = Recipe(name="Carrot", cook_time="30 minutes",
                             method="Carrotty", author=author)
        carrot_rec.save()

        carrot = Ingredient.objects.get(name="carrot")
        r_carrot = RecipeIngredient(adjective="chopped", unit="whole",
                                    amount="3", ingredient=carrot,
                                    recipe=carrot_rec)
        r_carrot.save()

        response = c.get(
            '/recipes/?ingredients=carrot&meal=&diet=&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=carrot&meal=&diet=&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 0)
        self.assertEqual(json.loads(response.content)['search'], 'carrot')

    # Test that different running list order does not create new meta
    # searches for same query
    def test_meta_search7(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=carrot,potato&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        response = c.get(
            '/recipes/?ingredients=potato,carrot&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        # Create recipe simulating user doing so
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 2)
        self.assertEqual(json.loads(response.content)['search'],
                         'carrot|potato')

    # Test that an empty string in query is ignored
    def test_meta_search8(self):
        # Create testing client
        c = APIClient()

        # Data for the account and testing
        user_data = {'username' : 'Bob', 'password' : 'Bob', 'email':
            'Bob@gmail.com'}

        # Log in and authorise user
        token = c.post('/user/register/', json.dumps(user_data),
                      content_type='application/json')
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.data[
            'token'])

        # Attempt to get some recipes
        response = c.get(
            '/recipes/?ingredients=&meal=dinner+lunch&diet=vegan'
            '&limit=10&offset=0/',
            content_type="application/json")

        # Verify that the metadata was updated appropriately
        response = c.get('/meta/')

        self.assertEqual(json.loads(response.content)['references'], 0)


# Tests for displaying a user's added recipes
class MyRecipesTest(TestCase):
    def setUp(self) -> None:
        # set up meal categories and dietary requirements
        breakfast = MealCategory.objects.create(name="breakfast")
        lunch = MealCategory.objects.create(name="lunch")
        dessert = MealCategory.objects.create(name="dessert")
        vegan = DietaryRequirement.objects.create(name="vegan")
        dairy_free = DietaryRequirement.objects.create(name="dairy-free")

        # set up users
        self.c1 = APIClient()
        user_data = {'username' : 'jess', 'email' : 'jess@gmail.com', 'password' : '1111'}
        user = self.c1.post('/user/register/', json.dumps(user_data), content_type='application/json')
        user_data.pop('email')      
        token = self.c1.post('/user/login/', json.dumps(user_data), content_type='application/json')
        self.c1.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        self.c2 = APIClient()
        user_data = {'username' : 'reece', 'email' : 'reece@gmail.com', 'password' : '2222'}
        user = self.c2.post('/user/register/', json.dumps(user_data), content_type='application/json')
        user_data.pop('email')      
        token = self.c2.post('/user/login/', json.dumps(user_data), content_type='application/json')
        self.c2.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])  

        # set up recipe ingredients
        fruit = IngredientCategory.objects.create(name="fruit")
        fruit.save()

        ingredient = IngredientSerializer(data={"name": "apple", "category": {"name": "fruit"}})
        ingredient.is_valid()
        ingredient.save()

        ingredient = IngredientSerializer(data={"name": "pear", "category": {"name": "fruit"}})
        ingredient.is_valid()
        ingredient.save()

    # tests that users recipes are correctly returned
    def test_my_recipes1(self):
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}

        post = self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')
        response = self.c1.get('/user/myrecipes/')

        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]}]  

        self.assertEqual(json.loads(response.content), expected_response)

    # tests that user can't view other users' added recipes
    def test_my_recipes2(self):
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        post = self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        recipe_data = {"name": "Chopped apple", "cook_time": "20 minutes", "method": "Crunch", "author": "2", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        post = self.c2.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        # get recipes for user 1
        response = self.c1.get('/user/myrecipes/')
        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]}]  

        self.assertEqual(json.loads(response.content), expected_response)

        # get recipes for user 2
        response = self.c2.get('/user/myrecipes/')     
        expected_response = [{'id': 2, 'name': 'Chopped apple', 'cook_time': '20 minutes', 'method': 'Crunch', 
                                'author': {'id': 2, 'username': 'reece', 'email': 'reece@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 2, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}]}]

        self.assertEqual(json.loads(response.content), expected_response)



class CookbookTest(TestCase):
    def setUp(self) -> None:
        # set up meal categories and dietary requirements
        breakfast = MealCategory.objects.create(name="breakfast")
        lunch = MealCategory.objects.create(name="lunch")
        dessert = MealCategory.objects.create(name="dessert")
        vegan = DietaryRequirement.objects.create(name="vegan")
        dairy_free = DietaryRequirement.objects.create(name="dairy-free")

        # set up users
        self.c1 = APIClient()
        user_data = {'username' : 'jess', 'email' : 'jess@gmail.com', 'password' : '1111'}
        user = self.c1.post('/user/register/', json.dumps(user_data), content_type='application/json')
        user_data.pop('email')
        token = self.c1.post('/user/login/', json.dumps(user_data), content_type='application/json')
        self.c1.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        self.c2 = APIClient()
        user_data = {'username' : 'reece', 'email' : 'reece@gmail.com', 'password' : '2222'}
        user = self.c2.post('/user/register/', json.dumps(user_data), content_type='application/json')
        user_data.pop('email')
        token = self.c2.post('/user/login/', json.dumps(user_data), content_type='application/json')
        self.c2.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        # set up recipe ingredients
        fruit = IngredientCategory.objects.create(name="fruit")
        fruit.save()

        ingredient = IngredientSerializer(data={"name": "apple", "category": {"name": "fruit"}})
        ingredient.is_valid()
        ingredient.save()

        ingredient = IngredientSerializer(data={"name": "pear", "category": {"name": "fruit"}})
        ingredient.is_valid()
        ingredient.save()

    # test adding recipes to cookbook
    def test_cookbook1(self):
        # enter recipe data
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1",
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}],
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        recipe_data = {"name": "Chopped apple", "cook_time": "20 minutes", "method": "Crunch", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        # add to user 2's favourites
        self.c2.post('/user/cookbook/', json.dumps({"id" : "1"}), content_type='application/json')
        self.c2.post('/user/cookbook/', json.dumps({"id" : "2"}), content_type='application/json')

        response = self.c2.get('/user/cookbook/')

        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]},
                                                 
                            {'id': 2, 'name': 'Chopped apple', 'cook_time': '20 minutes', 'method': 'Crunch', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 2, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}]}]  

        self.assertEqual(json.loads(response.content), expected_response)

    # test deleting recipes from cookbook
    def test_cookbook2(self):
        # enter recipe data
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1",
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}],
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        recipe_data = {"name": "Chopped apple", "cook_time": "20 minutes", "method": "Crunch", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        # add to user 2's favourites
        self.c2.post('/user/cookbook/', json.dumps({"id" : "1"}), content_type='application/json')
        self.c2.post('/user/cookbook/', json.dumps({"id" : "2"}), content_type='application/json')

        response = self.c2.get('/user/cookbook/')

        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]},
                                                 
                            {'id': 2, 'name': 'Chopped apple', 'cook_time': '20 minutes', 'method': 'Crunch', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 2, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}]}]  

        self.assertEqual(json.loads(response.content), expected_response)

        # delete first recipe from cookbook
        self.c2.delete('/user/cookbook/1/')

        response = self.c2.get('/user/cookbook/')

        expected_response = [{'id': 2, 'name': 'Chopped apple', 'cook_time': '20 minutes', 'method': 'Crunch', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 2, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}]}]  

        self.assertEqual(json.loads(response.content), expected_response)

        # delete other recipe
        self.c2.delete('/user/cookbook/2/')

        response = self.c2.get('/user/cookbook/')
        expected_response = []

        self.assertEqual(json.loads(response.content), expected_response)


        # make sure recipes can be added again
        self.c2.post('/user/cookbook/', json.dumps({"id" : "1"}), content_type='application/json')

        response = self.c2.get('/user/cookbook/')
        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]}]

        self.assertEqual(json.loads(response.content), expected_response)

    # test that users can't access other users' cookbooks
    def test_cookbook3(self):
        # enter recipe data
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1",
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}],
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        recipe_data = {"name": "Chopped apple", "cook_time": "20 minutes", "method": "Crunch", "author": "1", 
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"}],
                       "meal_cat": [{"name": "lunch"}], 
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        # add to user 2's favourites
        self.c2.post('/user/cookbook/', json.dumps({"id" : "1"}), content_type='application/json')
        self.c2.post('/user/cookbook/', json.dumps({"id" : "2"}), content_type='application/json')

        response = self.c1.get('/user/cookbook/')
        expected_response = []   

        self.assertEqual(json.loads(response.content), expected_response)

    # test that users can add their own recipes to cookbook
    def test_cookbook4(self):
        # enter recipe data
        recipe_data = {"name": "Fruit salad", "cook_time": "20 minutes", "method": "Yummy yummy", "author": "1",
                        "ingredients":
                           [{"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "apple"},
                            {"adjective": "chopped", "unit": "cups", "amount": "2", "ingredient": "pear"}],
                       "meal_cat": [{"name": "lunch"}],
                       "diet_req": [{"name": "vegan"}, {"name": "dairy-free"}]}
        self.c1.post('/recipes/', json.dumps(recipe_data), content_type='application/json')

        # add to user 1's favourites
        self.c1.post('/user/cookbook/', json.dumps({"id" : "1"}), content_type='application/json')

        response = self.c1.get('/user/cookbook/')
        expected_response = [{'id': 1, 'name': 'Fruit salad', 'cook_time': '20 minutes', 'method': 'Yummy yummy', 
                                'author': {'id': 1, 'username': 'jess', 'email': 'jess@gmail.com'},
                                "image_URL": None,
                                'meal_cat': [{'name': 'lunch'}], 'diet_req': [{'name': 'dairy-free'}, {'name': 'vegan'}], 
                                'ingredients': 
                                    [{'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'apple', 'category': {'name': 'fruit'}}}, 
                                    {'adjective': 'chopped', 'unit': 'cups', 'amount': '2', 'recipe': 1, 
                                        'ingredient': {'name': 'pear', 'category': {'name': 'fruit'}}}]}]

        self.assertEqual(json.loads(response.content), expected_response)



    
