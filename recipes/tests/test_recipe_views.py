from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.

# def test_the_paytest_is_ok(self):
#         variavel = '123456'
#         print('Olá mundo!')
#         assert 1 == 1, 'Um é igual a um'


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={ 'id': 1 }))
        self.assertIs(view.func, views.recipe)
    