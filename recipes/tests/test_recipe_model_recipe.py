from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized
class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe =  self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_default(self):
        recipe = Recipe(
            title= 'Recipe title',
            description= 'Recipe Description',
            slug= 'recipe-slug',
            preparation_time=10,
            preparation_time_unit = 'Minutos',
            servings=5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe Preparation Steps',
            category=self.make_category(name='Test Default Category'),
            user=self.make_author(username='newuser'),
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not false'
            )
    
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is published is not false'
            )
        
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
                            str(self.recipe), 
                            needed,
                            msg='Recipe string representation'\
                                 f' must be "{needed}" recipe title'\
                                 f' but "{str(self.recipe)}" was received'
                        )