from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ("Customer", "Customer"),
        ("Admin", "Admin"),
    ]

    user_type = models.CharField(choices=USER_TYPE, max_length=50, null=True)

    def __str__(self):
        return self.username


class CustomerProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile/', null=True)

    def __str__(self):
        return self.name or self.user.username


class AdminProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    store_name = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    store_address = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile/', null=True)

    def __str__(self):
        return self.name or self.user.username


class CategoryModel(models.Model):
    user = models.ForeignKey(AdminProfileModel, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.category_name


class ProductManagementModel(models.Model):
    user = models.ForeignKey(AdminProfileModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock = models.IntegerField(default=0)
    description = models.TextField(null=True)
    product_image = models.ImageField(upload_to='product/', null=True)

    def __str__(self):
        return self.product_name


class ProductOrderModel(models.Model):

    PAYMENT_METHOD = [
        ("COD", "COD"),
        ("Online", "Online"),
    ]

    ORDER_STATUS = [
        ("Pending", "Pending"),
        ("In-Progress", "In-Progress"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
    ]

    PAYMENT_STATUS = [
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
    ]

    product = models.ForeignKey(ProductManagementModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfileModel, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50, null=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=50, default='Unpaid')
    order_status = models.CharField(choices=ORDER_STATUS, max_length=50, default='Pending')

    def __str__(self):
        return str(self.product.product_name)


class ReviewModel(models.Model):
    product = models.ForeignKey(ProductManagementModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfileModel, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.review or "Review"