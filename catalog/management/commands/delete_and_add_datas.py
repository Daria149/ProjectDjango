from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command



class Command(BaseCommand):
    help = 'Add test datas to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        #Создаём и загружаем данные
        category1 = Category.objects.create(name='Смартфоны', description='Полезные гаджеты')
        category2 = Category.objects.create(name='Ноутбуки', description='Для работы и игр')

        id_category_smart = Category.objects.get(name="Смартфоны")
        id_category_notes = Category.objects.get(name="Ноутбуки")

        product1 = Product.objects.create(name='TECNO Spark 20 Pro', description='Встроенная 256 ГБ, оперативная 12 ГБ, 8 ГБ', photo='', category = id_category_smart, price = 34900, created_at = '2025-01-20', updated_at = '2025-05-10')
        product2 = Product.objects.create(name='Ноутбук HP 250', description='Емкость кэш-памяти составляет 10 МБ', photo='', category=id_category_notes, price = 48000, created_at = '2025-02-11', updated_at = '2025-04-18')

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
