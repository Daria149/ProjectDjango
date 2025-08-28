from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Наименование категории",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(verbose_name="Описание категории", help_text="Заполните описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(verbose_name="Описание продукта", help_text="Заполните описание продукта")
    photo = models.ImageField(
        upload_to="photos",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Заполните категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена продукта", help_text="Укажите цену продукта")
    created_at = models.DateField(
        verbose_name="Дата создания продукта",
        help_text="Указывается дата создания продукта",
        auto_now_add=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения продукта",
        help_text="Указывается дата последнего изменения продукта",
        auto_now=True,
        null=True,
    )
    publish_product = models.BooleanField(
        verbose_name="Статус публикации продукта",
        help_text="Укажите статус публикации продукта.",
        default = False
    )
    owner = models.ForeignKey(User,
                              verbose_name="Владелец",
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
           # ("can_delete_product", "Can delete product")
        ]

    def __str__(self):
        return f"{self.name}: категории {'self.category'}, цена: {'self.price'}"