from rest_framework import status


class TestNews:
    def test_get_news(self, user_client):
        """Аутентифицированный пользователь может получить список новостей."""

        response = user_client.get('/api/v1/news/')

        assert response.status_code == status.HTTP_200_OK

    # def test_create_favourite_new(self, user_client):
    #     """Аутентифицированный пользователь может добавить
    #     новость в избранное."""
    #
    #     response = user_client.post()
