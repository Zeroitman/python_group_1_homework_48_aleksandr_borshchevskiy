from django.shortcuts import reverse, redirect, get_object_or_404
from webapp.models import Food, Order, OrderFood
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.forms import ProjectForm, OrderForm, OrderFoodForm
from django.urls import reverse_lazy


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s' % reverse('webauth:login'))
        return super().dispatch(request, *args, **kwargs)


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_add.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_food_add', kwargs={'pk': self.object.pk})


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm
    success_url = reverse_lazy('webapp:order_list')


class CourierListView(ListView):
    model = Order
    template_name = 'courier_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s' % reverse('webauth:login'))
        return super().dispatch(request, *args, **kwargs)


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s' % reverse('webauth:login'))
        return super().dispatch(request, *args, **kwargs)


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_add.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


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


class DetailListView(DetailView):
    model = Order
    template_name = 'order_detail.html'


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


class OrderfoodDeleteView(DeleteView):
    model = OrderFood
    template_name = 'order_food_delete.html'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': get_object_or_404(OrderFood, pk=self.kwargs.get('pk')).order.pk})


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