from rest_framework import test
from django.urls import reverse
from django.contrib.auth.models import User


class OrderAPITest(test.APITestCase):
    def make_user(self):
        user_data = {
            'username': 'admin',
            'password': 'admin',
        }
        User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
        )

    def make_order(self):
        self.make_user()
        order_data = {
            'buyer': '1',
            'order_number': '10',
        }
        create_url = reverse('orders:orders-api-list')
        return self.client.post(
            path=create_url,
            data=order_data,
        )

    def test_orders_list_returns_successfully(self):
        # 200 = Ok
        list_url = reverse('orders:orders-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_orders_create_returns_successfully(self):
        # 201 = Created
        response = self.make_order()
        self.assertEqual(response.status_code, 201)

    def test_orders_detail_returns_successfully(self):
        # 200 = Ok
        self.make_order()
        detail_url = reverse(
            'orders:orders-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_orders_partial_update_returns_successfully(self):
        # 200 = Ok
        self.make_order()
        partial_update_url = reverse(
            'orders:orders-api-detail',
            kwargs={'pk': 1},
        )
        update_data = {
            'is_paid': True,
        }
        response = self.client.patch(
            path=partial_update_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_orders_destroy_returns_successfully(self):
        # 204 = No Content
        self.make_order()
        destroy_url = reverse(
            'orders:orders-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, 204)
