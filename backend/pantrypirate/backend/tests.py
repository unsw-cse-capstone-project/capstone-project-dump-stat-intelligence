from django.test import TestCase, Client
from .models import *
from .views import *
import json


# Create your tests here.
class UserTestCase(TestCase):

    def test_create_user(self):
        c = Client()
        user_data1 = {'username' : 'Bob', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        user_data2 = {'username' : 'Bob1', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        user = c.post('/users/', json.dumps(user_data1),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())
        user = c.post('/users/', json.dumps(user_data2),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data2.items())

    def test_get_user(self):
        c = Client()
        user_data1 = {'username' : 'Bob', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        c.post('/users/', json.dumps(user_data1),
                      content_type='application/json')
        user = c.get('/users/1/')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())

    def test_get_users(self):
        c = Client()
        user_data1 = {'username' : 'Bob', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        user_data2 = {'username' : 'Bob1', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        c.post('/users/', json.dumps(user_data1),
                      content_type='application/json')
        c.post('/users/', json.dumps(user_data2),
                      content_type='application/json')
        users = c.get('/users/')
        self.assertGreaterEqual(json.loads(users.content)['results'][1].items(),
                                user_data1.items())
        self.assertGreaterEqual(json.loads(users.content)['results'][0].items(),
                                user_data2.items())

    def test_delete_user(self):
        c = Client()
        user_data1 = {'username' : 'Bob', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        c.post('/users/', json.dumps(user_data1),
                      content_type='application/json')
        c.delete('/users/1/')
        user = c.get('/users/1/')
        self.assertContains(user, "Not found", status_code=404)

    def test_put_user(self):
        c = Client()
        user_data1 = {'username' : 'Bob', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        c.post('/users/', json.dumps(user_data1),
                      content_type='application/json')
        user_data1 = {'username' : 'Bob1', 'password' : 'extra_cheese', 'email'
                     : 'save_a_piece@forme.com'}
        user = c.put('/users/1/', json.dumps(user_data1),
                     content_type='application/json')
        self.assertGreaterEqual(json.loads(user.content).items(),
                                user_data1.items())


# Create your tests here.
class Ingredient(TestCase):
    def setUp(self) -> None:
        cat = IngredientCategory.objects.create(name = 'grain')
        cat = IngredientCategory.objects.create(name = 'vegetable')

    def test_create_ingredient1(self):
        c = Client()
        ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
        ing = c.post('/ingredients/', json.dumps(ingredient_data),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_create_ingredient2(self):
        c = Client()
        ingredient_data = {'name' : 'potato', 'category' : {'name' :
                                                                'not_grain'}}
        ing = c.post('/ingredients/', json.dumps(ingredient_data),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_get_ingredient(self):
        c = Client()
        ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
                      content_type='application/json')
        ing = c.get('/ingredients/potato/')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())

    def test_get_ingredients(self):
        c = Client()
        ingredient_data1 = {'name' : 'potato', 'category' : {'name' : 'grain'}}
        ingredient_data2 = {'name' : 'beef', 'category' : {'name' : 'grain'}}
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
        ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
                      content_type='application/json')
        c.delete('/ingredients/potato/')
        ing = c.get('/ingredients/potato/')
        self.assertContains(ing, "Not found", status_code=404)

    def test_put_ingredient(self):
        c = Client()
        ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
        c.post('/ingredients/', json.dumps(ingredient_data),
                      content_type='application/json')
        ingredient_data = {'name' : 'potato', 'category' : {'name' :
                                                                'vegetable'}}
        ing = c.put('/ingredients/potato/', json.dumps(ingredient_data),
                      content_type='application/json')
        self.assertGreaterEqual(json.loads(ing.content).items(),
                                ingredient_data.items())




# Create your tests here.
class Recipe(TestCase):
    def setUp(self) -> None:
        meal_cat = MealCategory.objects.create(name="Lunch")
        meal_cat2 = MealCategory.objects.create(name="Dinner")
        diet_req = DietaryRequirement.objects.create(name="Vegan")
        diet_req = DietaryRequirement.objects.create(name="Vegetarian")
        user = User.objects.create(username="Bob", email="Bob@gmail.com",
                                    password="Bob")
        ingredient_cat = IngredientCategory.objects.create(name="vegetable")
        ingredient = IngredientSerializer(data={"name" : "potato", "category" :
            {"name" : "vegetable"}})
        ingredient.is_valid()
        ingredient.save()
        ingredient = IngredientSerializer(data={"name" : "pea", "category" :
            {"name" : "vegetable"}})
        ingredient.is_valid()
        ingredient.save()

    def test_create_recipe(self):
        c = Client()
        recipe_data = {"name" : "Hot ham water", "cook_time" : "2 hours",
                   "method" : "Put in water", "author" : "1", "ingredients" :
                                  [], 'favourites' : [],
                       'meal_cat' : [{"name" : "dinner"}], 'diet_req' : []}
        ing = c.post('/recipes/', json.dumps(recipe_data),
                      content_type='application/json')
        print(ing.content)
        # self.assertGreaterEqual(json.loads(ing.content).items(),
        #                         recipe_data.items())

    # def test_create_ingredient2(self):
    #     c = Client()
    #     ingredient_data = {'name' : 'potato', 'category' : {'name' :
    #                                                             'not_grain'}}
    #     ing = c.post('/ingredients/', json.dumps(ingredient_data),
    #                   content_type='application/json')
    #     self.assertGreaterEqual(json.loads(ing.content).items(),
    #                             ingredient_data.items())
    #
    # def test_get_ingredient(self):
    #     c = Client()
    #     ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
    #     c.post('/ingredients/', json.dumps(ingredient_data),
    #                   content_type='application/json')
    #     ing = c.get('/ingredients/potato/')
    #     self.assertGreaterEqual(json.loads(ing.content).items(),
    #                             ingredient_data.items())
    #
    # def test_get_ingredients(self):
    #     c = Client()
    #     ingredient_data1 = {'name' : 'potato', 'category' : {'name' : 'grain'}}
    #     ingredient_data2 = {'name' : 'beef', 'category' : {'name' : 'grain'}}
    #     c.post('/ingredients/', json.dumps(ingredient_data1),
    #                   content_type='application/json')
    #     c.post('/ingredients/', json.dumps(ingredient_data2),
    #                   content_type='application/json')
    #     ing = c.get('/ingredients/')
    #     self.assertGreaterEqual(json.loads(ing.content)['results'][1].items(),
    #                             ingredient_data1.items())
    #     self.assertGreaterEqual(json.loads(ing.content)['results'][0].items(),
    #                             ingredient_data2.items())
    #
    # def test_delete_ingredient(self):
    #     c = Client()
    #     ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
    #     c.post('/ingredients/', json.dumps(ingredient_data),
    #                   content_type='application/json')
    #     c.delete('/ingredients/potato/')
    #     ing = c.get('/ingredients/potato/')
    #     self.assertContains(ing, "Not found", status_code=404)
    #
    # def test_put_ingredient(self):
    #     c = Client()
    #     ingredient_data = {'name' : 'potato', 'category' : {'name' : 'grain'}}
    #     c.post('/ingredients/', json.dumps(ingredient_data),
    #                   content_type='application/json')
    #     ingredient_data = {'name' : 'potato', 'category' : {'name' :
    #                                                             'vegetable'}}
    #     ing = c.put('/ingredients/potato/', json.dumps(ingredient_data),
    #                   content_type='application/json')
    #     self.assertGreaterEqual(json.loads(ing.content).items(),
    #                             ingredient_data.items())
# class RecipeTestCase(TestCase):
#     def setUp(self):
#         meal_cat = MealCategory.objects.create(name="Lunch")
#         meal_cat2 = MealCategory.objects.create(name="Dinner")
#         diet_req = DietaryRequirement.objects.create(name="Vegan")
#         diet_req = DietaryRequirement.objects.create(name="Vegetarian")
#         user = User.objects.create(username="Bob", email="Bob@gmail.com",
#                                     password="Bob")
#         ingredient_cat = IngredientCategory.objects.create(name="vegetable")
#         ingredient = IngredientSerializer(data={"name" : "potato", "category" :
#             "vegetable"})
#         ingredient.is_valid()
#         ingredient.save()
#         ingredient = IngredientSerializer(data={"name" : "pea", "category" : "vegetable"})
#         ingredient.is_valid()
#         ingredient.save()
#
#     def test_post_1(self):
#         recipe1 = {"name" : "Hot ham water", "cook_time" : "2 hours",
#                    "method" : "Put in water", "author" : "1", "ingredients" :
#                                   [{"adjective" : "moldy", "unit" : "g",
#                                     "amount" : "20", "recipe" : "1",
#                                     "ingredient" : "potato"},
#                                    {"adjective": "green", "unit": "g",
#                                     "amount": "20", "recipe": "1",
#                                     "ingredient": "pea"}]}
#         c = Client()
#         response = c.post('/recipe/', json.dumps(recipe1),
#                           content_type="application/json")
#         response = c.get('/recipe/1/')
#
#     def test_post_2(self):
#         recipe1 = {"recipe": {"name" : "Hot ham water", "cook_time" : "2 hours",
#                    "method" : "Put in water", "author" : "1", "ingredients" :
#                                   [{"adjective" : "moldy", "unit" : "g",
#                                     "amount" : "20", "recipe" : "1",
#                                     "ingredient" : "potato"},
#                                    {"adjective": "green", "unit" : "g",
#                                     "amount" : "20", "recipe": "1",
#                                     "ingredient": "pea"}]}}
#         c = Client()
#         response = c.post('/recipe/', json.dumps(recipe1),
#                           content_type="application/json")
#         response = c.get('/recipe/1/')
#         recipe1 = {"recipe": {"name" : "Cold ham water", "cook_time" : "2 "
#                                                                        "hours",
#                    "method" : "Put in water", "author" : "1", "ingredients" :
#                                   [{"adjective" : "moldy", "unit" : "g",
#                                     "amount" : "20", "recipe" : "1",
#                                     "ingredient" : "potato"},
#                                    {"adjective": "green", "unit" : "g",
#                                     "amount" : "20", "recipe": "1",
#                                     "ingredient": "pea"}]}}
#         response = c.put('/recipe/1/', json.dumps(recipe1),
#                          content_type="application/json")
#         response = c.delete('/recipe/1/')
#
#     def test_post_3(self):
#         recipe1 = { "recipe" : {"name" : "Hot ham water", "cook_time" : "2 " \
#                                                                        "hours",
#                    "method" : "Put in water", "author" : "1", "meal_cat" : [
#                 "Lunch", "Dinner"], "diet_req" : ["Vegan"], "ingredients" :
#                                   [{"adjective" : "moldy", "unit" : "g",
#                                     "amount" : "20", "recipe" : "1",
#                                     "ingredient" : "potato"},
#                                    {"unit" : "g",
#                                     "amount" : "20", "recipe": "1",
#                                     "ingredient": "pea"}]}}
#         c = Client()
#         response = c.post('/recipe/', json.dumps(recipe1),
#                           content_type="application/json")
#         response = c.get('/recipe/1/')
#
#
# # Create your tests here.
# class IngredientTestCase(TestCase):
#     def setUp(self):
#         ing_cat = IngredientCategory.objects.create(name = "vegetable")
#
#     def test_get_post_1(self):
#         ingredient_test = {"ingredient" : {"name" : "pea", "category" :
#             "vegetable"}}
#         c = Client()
#         response = c.post('/ingredients/', json.dumps(ingredient_test),
#                           content_type="application/json")
#         response = c.get('/ingredients/pea/')
#
#
# class PantryIngredientTestCase(TestCase):
#     def setUp(self):
#         ing_cat = IngredientCategory.objects.create(name = "vegetable")
#         ingredient = IngredientSerializer(data={"name" : "potato", "category" :
#         "vegetable"})
#         ingredient.is_valid()
#         ingredient.save()
#         user = User.objects.create(username="Bob", email="Bob@gmail.com",
#                                     password="Bob")
#
#     def test_get_post(self):
#         ingredient_test = {"ingredients" : {"expiry_date" :
#                                                 "2020-06-29",
#                                             "ingredient" : "potato",
#                                            "user" : "1"}}
#         c = Client()
#         response = c.post('/user/1/pantry/', json.dumps(ingredient_test),
#                           content_type="application/json")