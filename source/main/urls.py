"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('webauth.urls', 'webauth')),
    path('', include('webapp.urls', 'webapp')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
# from webapp.views import OrderListView, OrderCreateView, OrderfoodCreateView, OrderUpdateView,\
#                             FoodCreateView, FoodDeleteView, FoodUpdateView, FoodListView, \
#                             ClientListView, CourierListView, change_status, change_status_courier_1,\
#                             change_status_courier_2, login_view, logout_view
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', OrderListView.as_view(), name='order_list'),
#     path('menu', FoodListView.as_view(), name='food_list'),
#     path('users', ClientListView.as_view(), name='client_list'),
#     path('food/create', FoodCreateView.as_view(), name='food_add'),
#     path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
#     path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),
#     path('order/create', OrderCreateView.as_view(), name='order_add'),
#     path('order/<int:pk>/order_food', OrderfoodCreateView.as_view(), name='order_food_add'),
#     path('courier', CourierListView.as_view(), name='courier_list'),
#     path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
#     path('order/<int:pk>/change_status', change_status, name='change_status'),
#     path('order/<int:pk>/change_status_courier_1', change_status_courier_1, name='change_status_courier_1'),
#     path('order/<int:pk>/change_status_courier_2', change_status_courier_2, name='change_status_courier_2'),
#     path('auth/login', login_view, name='login'),
#     path('auth/login', logout_view, name='logout')
#
# ]
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)