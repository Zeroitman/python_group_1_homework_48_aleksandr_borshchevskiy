from django.shortcuts import reverse, redirect, get_object_or_404
from webapp.models import Food, Order, OrderFood, Employee
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from webapp.forms import ProjectForm, OrderForm, OrderFoodForm
from django.urls import reverse_lazy


def change_status(request, pk):
    task = get_object_or_404(Order, pk=pk)
    task.status = 'Отменён'
    task.save()
    return redirect('webapp:order_list')


def change_status_courier_1(request, pk):
    task = get_object_or_404(Order, pk=pk)
    task.status = 'В пути'
    # task.courier =
    task.save()
    return redirect('webapp:courier_list')


def change_status_courier_2(request, pk):
    task = get_object_or_404(Order, pk=pk)
    task.status = 'Доставлен'
    task.save()
    return redirect('webapp:courier_list')


class ClientListView(ListView):
    model = Employee
    template_name = 'client_list.html'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class CourierListView(ListView):
    model = Order
    template_name = 'courier_list.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_add.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_food_add', kwargs={'pk': self.object.pk})


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_add.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:order_list')


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


class OrderfoodCreateView(CreateView):
    model = OrderFood
    template_name = 'order_food_add.html'
    form_class = OrderFoodForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_food_add', kwargs={'pk': self.kwargs.get('pk')})


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm
    success_url = reverse_lazy('webapp:order_list')



