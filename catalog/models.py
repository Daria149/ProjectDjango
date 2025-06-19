from django.db import models


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
        related_name="categories",
    )
    price = models.PositiveIntegerField(verbose_name="Цена продукта", help_text="Укажите цену продукта")
    created_at = models.DateField(
        verbose_name="Дата создания продукта",
        help_text="Укажите дату создания продукта",
        auto_now_add=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения продукта",
        help_text="Укажите дату последнего изменения продукта",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]

    def __str__(self):
        return f"{self.name}: категории {'self.category'}, цена: {'self.price'}"
