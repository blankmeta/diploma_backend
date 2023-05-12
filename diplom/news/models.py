from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()


class New(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=2048)
    image = models.ImageField(null=True, upload_to='news/images/')
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                               null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FavouriteNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favourite_news')
    new = models.ForeignKey(New, on_delete=models.CASCADE,
                            related_name='favourited')

    def __str__(self):
        return f'{self.user} | {self.new}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'new'],
                                    name='favourite news unique validator')
        ]
