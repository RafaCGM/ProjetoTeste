from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, cpf, data_nascimento, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf, data_nascimento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not password:
            raise ValueError('O superusuário precisa de uma senha.')

        return self.create_user(email, nome, cpf, data_nascimento, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'data_nascimento']

    def __str__(self):
        return self.nome
