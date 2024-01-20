from django.db import models
from django.utils.crypto import get_random_string
from transliterate import translit
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib.postgres.fields import ArrayField
from sellers.models import CustomUser


class Product(models.Model):
    # TODO: УБРАТЬ ЧОЙСЕС ИЗ КЛАССА, ДОДЕЛАТЬ FAVOURITES
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex')
    ]

    name = models.CharField(max_length=255, verbose_name="Name")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')
    # TODO: ОТДЕЛЬНАЯ МОДЕЛЬ ДЛЯ DISCOUNT
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Discount price', blank=True,
                                         null=True)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', blank=True, null=True)
    description = models.CharField(max_length=2048, verbose_name='Description', blank=True, null=True)
    city = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        related_name='products',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='products',
        blank=True,
        null=True
    )
    subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.SET_NULL,
        related_name='products',
        blank=True,
        null=True
    )
    style = models.ForeignKey(
        'Style',
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
        blank=True,
    )
    seller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='products'
    )
    likes = models.PositiveIntegerField(verbose_name='Likes', blank=True, null=True)
    condition = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    uid = models.CharField(unique=True, max_length=15, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=250, blank=True, null=True)
    to_remove = models.BooleanField(default=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='U')

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = get_random_string(length=15, allowed_chars='0123456789')
        if not self.slug:
            name_slug = slugify(unidecode(self.name.lower()))
            self.slug = f'{self.uid}-{name_slug}'
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name', 'posted_at']
        get_latest_by = 'posted_at'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{unidecode(self.name).replace(" ", "-").lower()}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Style(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{unidecode(self.name).replace(" ", "-").lower()}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'


class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subcategories'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{unidecode(self.name).replace(" ", "-").lower()}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='City')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{unidecode(self.name).replace(" ", "-").lower()}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Color(models.Model):
    name = models.CharField(max_length=155)
    image = models.URLField(blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='colors',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Image(models.Model):
    image = models.URLField()
    alt_text = models.CharField(
        verbose_name="Alternative text",
        help_text="Please add alturnative text",
        max_length=255,
        null=True,
        blank=True,
    )
    product_pk = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

# class Size(models.Model):
#     size = models.CharField(max_length=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sizes')



