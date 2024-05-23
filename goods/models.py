from django.db import models


class Categories(models.Model):
    class Meta:
        db_table = 'category'
        ordering = ('id', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150, unique=True, help_text='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL', help_text='URL категории')

    def __str__(self):
        return self.name


class Products(models.Model):
    class Meta:
        db_table = 'product'
        ordering = ('category', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=150, unique=True, help_text='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL', help_text='URL категории')
    description = models.TextField(blank=True, null=True, help_text='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, help_text='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, help_text='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, help_text='Скидка')
    quantity = models.PositiveIntegerField(default=0, help_text='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, help_text='Категория')

    def __str__(self):
        return self.name

    def display_id(self) -> str:
        return f'{self.id:05}'

    def sell_price(self):
        return round(self.price - self.price * self.discount / 100, 2)
