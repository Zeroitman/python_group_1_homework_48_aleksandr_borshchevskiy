from django.shortcuts import reverse
from webapp.models import Food, Order, OrderFood
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from webapp.forms import ProjectForm, OrderForm, OrderFoodForm
from django.urls import reverse_lazy


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_add.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_food_add', kwargs={'pk': self.object.pk})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


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


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = ProjectForm
    success_url = reverse_lazy('food_list')


class OrderfoodCreateView(CreateView):
    model = OrderFood
    template_name = 'order_food_add.html'
    form_class = OrderFoodForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk = self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.kwargs.get('pk')})
