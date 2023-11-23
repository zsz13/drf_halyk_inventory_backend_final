from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestInventoryPermissions(APITestCase):
    admin_user = User.objects.get(username='root')

    def setUp(self):
        self.user = User.objects.create_user(username='user_test', password='qwerty12345678')

    def test_inventoryitem_list_unauthorized(self):
        response = self.client.get('/api/v1/inventoryitem/')
        self.assertEqual(response.status_code, 401)

    def test_inventoryitem_id_unauthorized(self):
        response = self.client.get('/api/v1/inventoryitem/5/')
        self.assertEqual(response.status_code, 401)

    def test_inventoryitemdelete_id_unauthorized(self):
        response = self.client.get('/api/v1/inventoryitemdelete/7/')
        self.assertEqual(response.status_code, 401)

    def test_inventoryitem_list_authorized_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/inventoryitem/')
        self.assertEqual(response.status_code, 200)

    def test_inventoryitem_id_authorized_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/inventoryitem/5/')
        self.assertEqual(response.status_code, 403)

    def test_inventoryitemdelete_id_authorized_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/api/v1/inventoryitemdelete/7/')
        self.assertEqual(response.status_code, 403)

    def test_inventoryitem_list_superuser(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/v1/inventoryitem/')
        self.assertEqual(response.status_code, 200)

    def test_inventoryitem_id_superuser(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/v1/inventoryitem/5/')
        self.assertEqual(response.status_code, 404)

    def test_inventoryitemdelete_id_superuser(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete('/api/v1/inventoryitemdelete/7/')
        self.assertEqual(response.status_code, 404)