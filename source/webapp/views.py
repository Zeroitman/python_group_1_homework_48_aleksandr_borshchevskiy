from django.shortcuts import reverse, redirect, get_object_or_404
from webapp.models import Food, Order, OrderFood
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, FormView
from webapp.forms import ProjectForm, OrderForm, OrderFoodForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'order_add.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_food_add', kwargs={'pk': self.object.pk})


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm
    success_url = reverse_lazy('webapp:order_list')


class CourierListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'courier_list.html'


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    template_name = 'food_add.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = 'food_delete.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:food_list')


class DetailListView(LoginRequiredMixin, DetailView, FormView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderFoodForm


class OrderfoodCreateView(LoginRequiredMixin, CreateView):
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


class OrderfoodDeleteView(LoginRequiredMixin, DeleteView):
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
    task.save()
    return redirect('webapp:courier_list')


def change_status_courier_2(request, pk):
    task = get_object_or_404(Order, pk=pk)
    task.status = 'Доставлен'
    task.save()
    return redirect('webapp:courier_list')


def change_status_courier_3(request, pk):
    task = get_object_or_404(Order, pk=pk)
    task.status = 'Готовиться'
    task.save()
    return redirect('webapp:courier_list')

# ------------------------------------------------------------------------------------------------------


class OrderFoodAjaxCreateView(CreateView):
    model = OrderFood
    form_class = OrderFoodForm

    def form_valid(self, form):
        order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        form.instance.order = order
        order_food = form.save()
        return JsonResponse({
            'food_name': order_food.food.name,
            'food_pk': order_food.food.pk,
            'amount': order_food.amount,
            'pk': order_food.pk,
            'edit_url': reverse('webapp:order_food_update', kwargs={'pk': order_food.pk})
        })

    def form_invalid(self, form):
        return JsonResponse({
            'errors': form.errors
        }, status='422')


class OrderFoodAjaxUpdateView(UpdateView):
    model = OrderFood
    form_class = OrderFoodForm

    def form_valid(self, form):
        order_food = form.save()
        return JsonResponse({
            'food_name': order_food.food.name,
            'food_pk': order_food.food.pk,
            'amount': order_food.amount,
            'pk': order_food.pk
        })

    def form_invalid(self, form):
        return JsonResponse({
            'errors': form.errors
        }, status='422')


class OrderFoodAjaxDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderFood

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': get_object_or_404(OrderFood, pk=self.kwargs.get('pk')).order.pk})
