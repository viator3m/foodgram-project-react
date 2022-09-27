from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __init__(self, args, kwargs):
        super().__init__(*args, **kwargs)
