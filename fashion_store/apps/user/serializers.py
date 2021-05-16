from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'city',
                  'state', 'zip']
        #extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
