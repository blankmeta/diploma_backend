# from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
#                                    RetrieveModelMixin, DestroyModelMixin)
# from rest_framework.permissions import IsAdminUser
# from rest_framework.viewsets import GenericViewSet
# from django.contrib.auth import get_user_model
#
# from diplom.users.serializers import UserSerializer
#
# User = get_user_model()
#
#
# class UserViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
#                   DestroyModelMixin, GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (CurrentUserOrReadOnly, IsAdminUser)
