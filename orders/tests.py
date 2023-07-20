from rest_framework import test
from django.urls import reverse
from django.contrib.auth.models import User


class OrdersAPITest(test.APITestCase):
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
            'buyer': 1,
            'order_number': 10,
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


class OrderItemsAPITest(test.APITestCase):
    def make_user(self):
        user_data = {
            'username': 'admin',
            'password': 'admin',
        }
        User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
        )

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

    def make_product(self):
        self.make_category()
        product_data = {
            'title': 'Product',
            'description': 'Description',
            'category': 1,
            'price': 100,
        }
        create_url = reverse('products:products-api-list')
        return self.client.post(
            path=create_url,
            data=product_data,
        )

    def make_order(self):
        self.make_user()
        self.make_product()
        order_data = {
            'buyer': 1,
            'order_number': 10,
        }
        create_url = reverse('orders:orders-api-list')
        return self.client.post(
            path=create_url,
            data=order_data,
        )

    def make_order_item(self):
        self.make_order()
        order_item_data = {
            'order': 1,
            'product': 1,
            'quantity': 10,
            'total': 5,
        }
        create_url = reverse('orders:items-api-list')
        return self.client.post(
            path=create_url,
            data=order_item_data,
        )

    def test_order_items_list_returns_successfully(self):
        # 200 = Ok
        list_url = reverse('orders:items-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_order_items_create_returns_successfully(self):
        # 201 = Created
        response = self.make_order_item()
        self.assertEqual(response.status_code, 201)

    def test_order_items_detail_returns_successfully(self):
        # 200 = Ok
        self.make_order_item()
        detail_url = reverse(
            'orders:items-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_order_items_partial_update_returns_sucessful(self):
        # 200 = Ok
        self.make_order_item()
        partial_update_url = reverse(
            'orders:items-api-detail',
            kwargs={'pk': 1},
        )
        update_data = {
            'total': 50,
        }
        response = self.client.patch(
            path=partial_update_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_order_items_destroy_returns_successfully(self):
        # 204 = No Content
        self.make_order_item()
        destroy_url = reverse(
            'orders:items-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, 204)
