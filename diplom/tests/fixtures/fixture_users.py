import pytest

USER_USERNAME = 'TestUser'
USER_PASSWORD = '12345678'


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username=USER_USERNAME,
                                                 password=USER_PASSWORD,
                                                 email='test@gmail.com')


@pytest.fixture
def user2(django_user_model):
    return django_user_model.objects.create_user(username='TestUser2',
                                                 password='1234567',
                                                 email='test2@gmail.com')


@pytest.fixture
def user_client(user):
    from rest_framework.test import APIClient

    client = APIClient()

    token_response = client.post('/api/v1/auth/jwt/create/', data={
        "username": USER_USERNAME,
        "password": USER_PASSWORD
    })

    # print(token_response.json())

    token = token_response.json()['access']

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
