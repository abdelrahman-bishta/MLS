from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    status_book=[
        ('available', 'available'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True) #عشان لما تتمسح متمسحش الحاله بتاعتها من جدول الحاله
    status = models.CharField(max_length=20, choices=status_book, default='available',  null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    photo_author= models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_price_day = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    total_rental=models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    pages = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title