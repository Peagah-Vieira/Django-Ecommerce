from rest_framework import test
from django.urls import reverse


class CategoriesAPITest(test.APITestCase):
    def make_category(self):
        category_data = {
            'name': 'Category',
            'description': 'Description',
        }
        create_url = reverse('products:categories-api-list')
        return self.client.post(
            path=create_url,
            data=category_data,
        )

    def test_categories_list_returns_successfully(self):
        # 200 = Ok
        list_url = reverse('products:categories-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_categories_create_returns_successfully(self):
        # 201 = Created
        response = self.make_category()
        self.assertEqual(response.status_code, 201)

    def test_categories_detail_returns_successfully(self):
        # 200 = Ok
        self.make_category()
        detail_url = reverse(
            'products:categories-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_categories_partial_update_returns_successfully(self):
        # 200 = Ok
        self.make_category()
        partial_update_url = reverse(
            'products:categories-api-detail',
            kwargs={'pk': 1},
        )
        update_data = {
            'name': 'Updated Category',
            'description': 'Updated Description',
        }
        response = self.client.patch(
            path=partial_update_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_categories_destroy_returns_successfully(self):
        # 204 = No content
        self.make_category()
        destroy_url = reverse(
            'products:categories-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, 204)
