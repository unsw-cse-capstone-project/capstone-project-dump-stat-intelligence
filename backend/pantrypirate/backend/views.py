from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import Q
from .serializers import *
from .models import *
from .forms import *
import json
import urllib.parse

# Extract list of dict values
def extract_values(x, key):
    out = []
    for y in x:
        out.append(y.get(key))
    return out


# Recipe view
def recipe(request, recipe_id=None):
    if request.method == 'GET':

        # Extract recipe with id and serialise
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404("Recipe does not exist")
        serializer = RecipeSerializer(instance=recipe)

        # Take serialise dump and extract out name fields for meal category and
        # dietary requirements
        data = serializer.data
        data["author"] = recipe.author.name
        data["meal_cat"] = extract_values(data["meal_cat"], "name")
        data["diet_req"] = extract_values(data["diet_req"], "name")
        data["favourites"] = extract_values(data["favourites"], "name")
        data = {"recipe" : data}

        return JsonResponse(data)

    if request.method == 'DELETE':
        # Try to delete recipe
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404("Recipe does not exist")
        recipe.delete()

        return HttpResponse()

    if request.method == 'POST':
        try:
            recipe = RecipeForm(json.loads(request.body)['recipe'])
        except RuntimeError as error:
            raise error
        recipe.is_valid()
        recipe = recipe.save()
        serializer = RecipeSerializer(instance=recipe)

        # Take serialise dump and extract out name fields for meal category and
        # dietary requirements
        data = serializer.data
        data["author"] = recipe.author.name
        data["meal_cat"] = extract_values(data["meal_cat"], "name")
        data["diet_req"] = extract_values(data["diet_req"], "name")
        data["favourites"] = extract_values(data["favourites"], "name")
        data = {"recipe" : data}

        return JsonResponse(data)

# Work in progress - currently filters all recipes by meal category and diet reqs
# Search for recipes
def search(request, search_terms):
    # looks like: meal=dinner+lunch&diet=vegan&limit=10&offset=21 

    string = urllib.parse.parse_qs(search_terms, keep_blank_values=True)
    meals = string['meal'][0].split()
    diets = string['diet'][0].split()

    f = Recipe.objects.all()

    # filter by dietary requirement (AND relationship)
    if len(diets) != 0:
        for requirement in diets:
            f = f.filter(diet_req__pk=requirement)

    # filter by meal category (OR relationship)
    e = Recipe.objects.none()
    if len(meals) != 0:
        for category in meals:
            e |= f.filter(meal_cat__pk=category)

    else: e = f # if no meal categories specified, return all recipes

    # remove duplicates
    e = e.distinct()
    
    # temporarily returning list of matching recipe names
    lst = []
    for it in e:
        lst.append(it.name)

    return JsonResponse({"Matches": lst})

# User profiles
def user(request, user_id=None):

    if request.method == 'GET':

        # Extract user with given id
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        
        # get info from user profile 
        # vars returns a dictionary of the attributes
        # (pop first element, state info)
        details = (vars(user))
        details.pop("_state")

        return JsonResponse(details)

    if request.method == 'POST':
        try:
            user = UserForm(request.body)
        except RuntimeError as error:
            raise error

        user.is_valid()
        user = user.save()
        return JsonResponse({"id" : user.id})


# User pantry
def pantry(request, user_id=None):

    if request.method == 'GET':

        # return nested dictionary, looks like:
        #    pantry_contents = { 'item1': {'category': category, 'expiry': date},
        #                        'item2': {'category': category, 'expiry': date}}

        pantry_contents = {}
        items = PantryIngredient.objects.filter(user__pk=user_id)

        for item in items:
            new_dict = {}
            new_dict["category"] = item.ingredient.category.name
            new_dict["expiry_date"] = item.expiry_date

            pantry_contents[item.ingredient.name] = new_dict

        return JsonResponse(pantry_contents)