from webapp.models import Food, Order
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from webapp.forms import ProjectForm
from django.urls import reverse_lazy


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_add.html'
    form_class = ProjectForm
    success_url = reverse_lazy('order_list')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    form_class = ProjectForm
    success_url = reverse_lazy('food_list')