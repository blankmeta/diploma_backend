import pytest


@pytest.fixture
def create_categories(user):
    from events.models import Category

    names = ['Психбольницы', 'Театры', 'Еда', 'Другое']
    categories = []

    for name in names:
        categories.append(Category(name=name))

    Category.objects.bulk_create(categories)
