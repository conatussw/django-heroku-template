from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Pair Serializer especializado para carregar juntamente com o token de acesso
    informações de Grupo/Roles e permissões de usuários.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['roles'] = list(user.groups.values_list('name', flat=True))
        token['permissions'] = list(user.user_permissions.values_list('name', flat=True))

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
