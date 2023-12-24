from django.contrib.auth.models import AbstractUser


class ChildVisitor(AbstractUser):
    pass

    def __str__(self):
        return self.username
