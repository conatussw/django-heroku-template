from django.contrib.auth import get_user_model


def create_stub_user(username='joselito', password='123456'):
    user = get_user_model().objects.create(
        username=username,
        email='meu@provedor.com.ru'
    )
    user.set_password(password)
    user.save()
    return user
