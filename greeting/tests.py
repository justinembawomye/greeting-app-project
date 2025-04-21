from django.test import TestCase, Client
from django.urls import reverse

class GreetingTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")
        self.assertTemplateUsed(response, "index.html")


class GreetingFunctionalityTest(TestCase):
    def test_greeting(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')