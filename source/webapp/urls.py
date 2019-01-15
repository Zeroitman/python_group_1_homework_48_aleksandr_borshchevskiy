from django.urls import path
from webapp.views import OrderListView, OrderCreateView, OrderfoodCreateView, OrderUpdateView,\
                            FoodCreateView, FoodDeleteView, FoodUpdateView, FoodListView, \
                            OrderfoodDeleteView, CourierListView, change_status, change_status_courier_1,\
                            change_status_courier_2, change_status_courier_3, DetailListView, \
                            OrderFoodAjaxCreateView
app_name = 'webapp'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('menu', FoodListView.as_view(), name='food_list'),
    path('food/create', FoodCreateView.as_view(), name='food_add'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),
    path('order_food/<int:pk>/delete_food', OrderfoodDeleteView.as_view(), name='order_food_delete'),
    path('order/create', OrderCreateView.as_view(), name='order_add'),
    path('order/<int:pk>/order_food', OrderfoodCreateView.as_view(), name='order_food_add'),
    path('courier', CourierListView.as_view(), name='courier_list'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/change_status', change_status, name='change_status'),
    path('order/<int:pk>/change_status_courier_1', change_status_courier_1, name='change_status_courier_1'),
    path('order/<int:pk>/change_status_courier_2', change_status_courier_2, name='change_status_courier_2'),
    path('order/<int:pk>/change_status_courier_3', change_status_courier_3, name='change_status_courier_3'),
    path('order_food/<int:pk>/update', DetailListView.as_view(), name='order_detail'),
    # ----------------------------------------------------------------------------------------------------------------
    path('order/<int:pk>/food/create', OrderFoodAjaxCreateView.as_view(), name='order_food_create'),
]

