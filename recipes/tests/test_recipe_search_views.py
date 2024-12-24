from .test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.

# def test_the_paytest_is_ok(self):
#         variavel = '123456'
#         print('Olá mundo!')
#         assert 1 == 1, 'Um é igual a um'


class RecipeSearchViewsTest(RecipeTestBase):

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)
        #self.assertEqual(url, '/recipes/search/')

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
    
    def test_recipe_search_raises_404_if_not_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'search for &quot;&lt;teste&gt; | &quot',
            response.content.decode('utf-8')
        )
    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe 1'
        title2 = 'This is recipe 2'

        recipe1 = self.make_recipe(
            slug ='one-tt-1', title=title1, author_data={'username': 'one'}
        )
        recipe2 = self.make_recipe(
            slug ='two', title=title2, author_data={'username': 'two'}
        )

        search_url = reverse('recipes:search')

        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])