# from django.test import TestCase
from unittest import TestCase
from django.test import TestCase as DjangoTestcase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse


class AutorRegisterForUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your E-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_field_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)


    @parameterized.expand([
        ('username', 'Username'),
        ('email', 'E-mail'),
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('password', 'Password'),
        ('password2', 'Password2'),
    ])

    def test_field_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)

class AutorRegisterForIntegrationTest(DjangoTestcase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'email': 'email@anyemail.com',
            'first_name': 'first',
            'last_name': 'last',
            'password': 'Str0ngPassword1',
            'password2': 'Str0ngPassword1',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('username', 'This field must not be empty'),
        ('email', 'E-mail is required'),
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name'),
        ('password', 'Password must not be empty'),
        ('password2', 'Please, repeat your password'),
    ])

    def test_fields_can_not_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))