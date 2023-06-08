from _datetime import datetime, timedelta

from rest_framework import status

from events.models import Category


class TestNews:
    def test_create_event(self, user_client, create_categories):
        """Аутентифицированный пользователь может создать мероприятие."""
        payload = {
            'title': 'title',
            'address': 'Йошкар-Ола победы 1',
            'image': 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///'
                     'yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',
            'category': 1,
            'time': str(datetime.now() + timedelta(days=2))
        }

        response = user_client.post('/api/v1/events/', data=payload)

        assert response.status_code == status.HTTP_201_CREATED
