from django.test import TestCase
from django.urls import reverse


class LoginAppValantiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url_login = reverse('nucleo:login')
        cls.url_inicio = reverse('nucleo:inicio')
        cls.user = 'django'
        cls.password = 'django19asdasd'

    def test_login_true(self):
        response = self.client.post(
            self.url_login, {
                'username': self.user,
                'password': self.password
            }
        )
        # a = response.url
        self.assertEquals(response.status_code, 200)
        self.assertIn('app_nucleo/inicio.html', response.template_name)
