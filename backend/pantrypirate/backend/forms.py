from .models import *
from django.forms import ModelForm, forms


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'method', 'author', 'meal_cat',
                   'diet_req']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['meal_cat'].required = False
        self.fields['diet_req'].required = False


class PantryIngredientForm(ModelForm):

    class Meta:
        model = PantryIngredient
        fields = ['expiry_date', 'user', 'ingredient']

    def __init__(self, *args, **kwargs):
        super(PantryIngredientForm, self).__init__(*args, **kwargs)
        self.fields['expiry_date'].required = False


class RecipeIngredientForm(ModelForm):

    class Meta:
        model = RecipeIngredient
        fields = ['adjective', 'unit', 'amount', 'ingredient', 'recipe']

    def __init__(self, *args, **kwargs):
        super(RecipeIngredientForm, self).__init__(*args, **kwargs)
        self.fields['adjective'].required = False
        self.fields['unit'].required = False
        self.fields['amount'].required = False

    def clean(self):
        cleaned_data = super(RecipeIngredientForm, self).clean()
        unit = cleaned_data.get('unit')
        amount = cleaned_data.get('amount')

        if (not unit and amount) or (not amount and unit):
            raise forms.ValidationError("Please fill both unit and amount or "
                                        "neither")


# note - currenty zero security (should fix this)
class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)


# note - currenty zero security (should fix this)
class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'category']

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)


# note - currenty zero security (should fix this)
class CategoryForm(ModelForm):

    class Meta:
        model = IngredientCategory
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(IngredientCategory, self).__init__(*args, **kwargs)

