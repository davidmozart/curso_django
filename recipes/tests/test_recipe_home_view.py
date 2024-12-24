from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
    

class RecipeHomeViewTest(RecipeTestBase):

    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_satus_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEquals(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>NO RECIPE FOUND HERE!</h1>',
            response.content.decode('utf-8')
            )
    def test_recipe_home_view_returns_satus_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEquals(response.status_code, 200)
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(preparation_time=5)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('5 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)


    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published dont show"""
        #Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        
        self.assertIn(
            '<h1>NO RECIPE FOUND HERE!</h1>',
            response.content.decode('utf-8')
            )
