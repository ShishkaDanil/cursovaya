from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from autoapp.models import Car

class AddCarViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.car = Car.objects.create(make='Ford', model='Mustang', year='1967', owner=self.user)

    def test_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('add_car'))
        self.assertEqual(response.status_code, 200)
