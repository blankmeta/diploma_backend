import pytest
from rest_framework import status


class TestUsers:
    USER_PASSWORD = '1234567'
    AUTH_PREFIX = '/api/v1/auth/'

    @pytest.mark.django_db(transaction=True)
    def test_register_user(self, client):
        """Пользователь может зарегистрироваться."""
        data = {
            'password': 'test_password',
            'email': 'test_email@gmail.com',
        }
        response = client.post(self.AUTH_PREFIX + 'users/', data=data)

        assert response.status_code == status.HTTP_201_CREATED, (
            'Пользователь должен иметь возможность создать аккаунт'
        )

    def test_get_users(self, user_client):
        """Аутентифицированный пользователь может получить список юзеров."""
        response = user_client.get(self.AUTH_PREFIX + 'users/')
        test_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(test_data) == 1
