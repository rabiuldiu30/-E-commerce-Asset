from django.contrib import admin
from .models import *

admin.site.register([CustomUserModel,CustomerProfileModel,AdminProfileModel,ProductManagementModel,ProductOrderModel,ReviewModel])
# Register your models here.
