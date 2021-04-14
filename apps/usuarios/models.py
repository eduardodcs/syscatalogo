from django.contrib.auth.models import AbstractUser
from django.db import models
from catalogo.models import Produto

class Usuario(AbstractUser):
    produtos_vendedor = models.ManyToManyField(Produto)

