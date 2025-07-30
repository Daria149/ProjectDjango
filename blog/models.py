from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(verbose_name="Содержимое", help_text="Заполните содержимое")
    photo = models.ImageField(
        upload_to="blogphotos",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        auto_now_add=True,
        null=True,
    )
    publication_attribute = models.BooleanField(default=False)
    views_quantity = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["title", "created_at", "publication_attribute", "views_quantity"]

    def __str__(self):
        return f"{self.title}: содержимое {'self.content'}, количество просмотров: {'self.views_quantity'}"

