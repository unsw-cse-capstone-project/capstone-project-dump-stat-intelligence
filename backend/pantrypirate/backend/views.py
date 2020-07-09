from rest_framework import viewsets, generics, views
from rest_framework.authentication import TokenAuthentication, authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from rest_framework.views import Response, Http404
import urllib.parse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer


class UserLogin(views.APIView):
    queryset = User.objects.all().order_by("-id")
    permission_classes = (AllowAny, )
    serializer_class = LoginUser
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginUser(data=data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'],
                                password=serializer.data['password'])
            if not user:
                return Response({'error' : 'Invalid credentials'}, status=Http404)
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=200)

        return Response(serializer.errors, status=400)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all().order_by("-id")
    serializer_class = CreateUser
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json)
        return Response(serializer.errors, status=Http404)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by("name")
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        # looks like: meal=dinner+lunch&diet=vegan&limit=10&offset=21
        # print(request.GET.get('meal'))

        string = urllib.parse.parse_qs(request.META['QUERY_STRING'],
                                       keep_blank_values=True)
        # print(string)
        if not string:
            queryset = Recipe.objects.all().order_by('name')
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        meals = string['meal'][0].split()
        diets = string['diet'][0].split()
        running_list = string['ingredients'][0].split()
        # print(running_list)

        recipes = Recipe.objects.none()
        for item in running_list:
            # print(item)
            pIngredient = PantryIngredient.objects.get(pk=item)
            ingredient = pIngredient.ingredient
            for rec_ingredient in RecipeIngredient.objects.filter(
                    ingredient=ingredient):
                name = rec_ingredient.recipe
                recipes |= Recipe.objects.filter(name=name)

        f = recipes.distinct()

        # filter by dietary requirement (AND relationship)
        if len(diets) != 0:
            for requirement in diets:
                f = f.filter(diet_req__pk=requirement)

        # filter by meal category (OR relationship)
        e = Recipe.objects.none()
        if len(meals) != 0:
            for category in meals:
                e |= f.filter(meal_cat__pk=category)

        else:
            e = f  # if no meal categories specified, return all recipes

        # remove duplicates
        e = e.distinct()

        # temporarily returning list of matching recipe names
        lst = []
        for it in e:
            lst.append(it.name)

        return Response(lst)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


class PantryIngredientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PantryIngredient.objects.all()
    serializer_class = PantryIngredientSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = PantryIngredient.objects.filter(
                user=request.user).order_by('ingredient__category__name',
                'ingredient__name')
            # print(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Http404