from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    thumb = models.ImageField(default='default_product.png', null=True)
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('shop.Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'

class Brand(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='brands', null=True, blank=True) 

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'shop_brands'

class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
   address = models.CharField(max_length=255)
   phone = models.CharField(max_length=255)
   total_price = models.IntegerField()
   customer = models.ForeignKey(User, on_delete=models.CASCADE)  # заказчик

   def __str__(self):
       return 'Order # %s' % (str(self.id))

class OrderProduct(models.Model):
   order = models.ForeignKey('shop.Order', on_delete=models.CASCADE, related_name='order_products')
   product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
   amount = models.IntegerField() # общее кол-во
   total = models.IntegerField() # окончательная цена


   def __str__(self):
       return '%s x%s - %s' % (self.product, self.amount, self.order.customer.username)