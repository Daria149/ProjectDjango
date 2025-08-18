from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True, help_text="Здесь должен быть Ваш Аватар.")
    phone_number = models.CharField(max_length=35, verbose_name="Ваш телефон.", blank=True, null=True,help_text="Введите номер телефона.")
    country = models.CharField(max_length=70, verbose_name="Страна проживания.", blank=True,null=True, help_text="Введите страну проживания.")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять из цифр!")
        return phone_number

    def __str__(self):
        return self.email