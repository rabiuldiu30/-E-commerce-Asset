from django.urls import path
from .views import *

urlpatterns = [
    path('', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),

    path('dashboard/', dashboardPage, name='dashboard'),

    path('admin_profile/', adminProfilePage, name='admin_profile'),
    path('customer_profile/', customerProfilePage, name='customer_profile'),

    path('add_category/', categoryAddpage, name='add_category'),
    path('add_product/', productAddPage, name='add_product'),

    path('product/<int:id>/', viewProductPage, name='view_product'),

    path('product_order/<int:id>/',productOrderPage,name='product_order'),
    path('review/<int:id>/',reviewPage,name='review'),
    path('my_orders/', myOrdersPage, name='my_orders'),
    path('all_orders/', allOrdersPage, name='all_orders'),
]