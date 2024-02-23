from django.urls import reverse, resolve

from rest_framework import status

from rest_framework.test import APIRequestFactory, APITestCase

class CarrersViewSetTests(APITestCase):
    # CORE - COMMON
    def setUp(self):
        # this is used by other tests
        self.client.post(reverse('carrers-list'), data={'username': '@testuser', 'title': 'something', 'content': 'test content'})
    # OK - PASSING
    def test_carrers_list_get(self):
        url = reverse('carrers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # OK - PASSING
    def test_carrers_create_post(self):
        url = reverse('carrers-list')
        response = self.client.post(url, data={'username': '@testuser', 'title': 'something', 'content': 'test content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # OK - PASSING
    def test_carrers_retrieve_get(self):
        # First we create the item
        self.setUp
        # For this kind of test we're using APIRequestFactory, less buggy
        factory = APIRequestFactory()
        # Then we check if the item exists through api get method
        url = reverse('carrers-detail', kwargs={'pk': '1'})
        sol = resolve(url)
        view = sol.func
        request = factory.get(url, kwargs={'pk': '1'})
        response = view(request, pk=1)
        response.render()
        # We check if the status code first match the test behavior
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Then we check the api response content
        self.assertEqual(response.data['username'], '@testuser')
        self.assertEqual(response.data['id'], 1)
    # OK - PASSING
    def test_carrers_update_put(self):
        self.setUp
        # For this kind of test we're using APIRequestFactory, less buggy
        factory = APIRequestFactory()
        # Then we check if the item exists through api get method
        url = reverse('carrers-detail', kwargs={'pk': '1'})
        sol = resolve(url)
        view = sol.func
        # We're changing the entire resource then we're using the HTTP PUT method
        request = factory.put(url, kwargs={'pk': '1'}, data={'username': 'newusername', 'title': 'some new tilte', 'content': 'some new content'})
        response = view(request, pk=1)
        response.render()
        # We check if the status code first match the test behavior
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Then we check the api response content
        self.assertEqual(response.data['title'], 'some new tilte')
        self.assertEqual(response.data['content'], 'some new content')
        # We also check if the username is not being changed
        self.assertEqual(response.data['username'], '@testuser')
    # OK - PASSING
    def test_carrers_partial_update_patch(self):
        self.setUp
        # For this kind of test we're using APIRequestFactory, less buggy
        factory = APIRequestFactory()
        # Then we check if the item exists through api get method
        url = reverse('carrers-detail', kwargs={'pk': '1'})
        sol = resolve(url)
        view = sol.func
        # We're changing some things in the model then we're using the HTTP PATCH method
        request = factory.patch(url, kwargs={'pk': '1'}, data={'title': 'some new tilte', 'content': 'some new content'})
        response = view(request, pk=1)
        response.render()
        # We check if the status code first match the test behavior
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Then we check the api response content
        self.assertEqual(response.data['title'], 'some new tilte')
        self.assertEqual(response.data['content'], 'some new content')
    # OK - PASSING
    def test_carrers_destroy_delete(self):
        self.setUp
        url = reverse('carrers-detail', kwargs={'pk': '1'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)