from .models import *
from django.forms import ModelForm


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'method', 'author', 'meal_cat',
                   'diet_req']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['meal_cat'].required = False
        self.fields['diet_req'].required = False

# note - currenty zero security (should fix this)
class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)