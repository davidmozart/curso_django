from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
# Create your tests here.

# def test_the_paytest_is_ok(self):
#         variavel = '123456'
#         print('Olá mundo!')
#         assert 1 == 1, 'Um é igual a um'


class RecipeURLsTest(TestCase):
    def test_recipes_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipes_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={ 'category_id': 1 })
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipes_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={ 'id': 1 })
        self.assertEqual(url, '/recipes/1/')

    def test_recipes_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
        # self.fail(url)

# RED   GREN REFACTOR

