from django import template
import datetime

register = template.Library()


# Фильтр,который увеличивает переданное значение на 1
@register.filter
def increment(value):
    return int(value) + 1


# Фильтр, которые возвращает все блюда в заказе
# (для использования в теге-цикле {% for %})
@register.filter
def get_foods(order):
    return order.foods.all()


# Фильтр может принимать только 1 или 2 аргумента
# 1 аргумент - значение, к которому применяется фильтр
# 2 аргумент - аргумент для фильтра
# такой фильтр - с двумя аргументами,
# кроме самого значения - работать не будет.
# @register.filter()
# def annotate(value, prefix, suffix):
#     return prefix + value + suffix


# Фильтр, который проверяет,
# может ли текущий пользователь доставить заказ
@register.filter
def can_be_delivered_by(order, user):
    return order.status == 'on_way' and order.courier == user


# Теги - шаблонные теги Django, которые обозначаются {% %}.
# В отличие от фильтров они могут принимать
# сколько угодно аргументов, включая args и kwargs.

# Тег, который выводит текущие дату и время в указанном формате
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


# Тег, который выводит формы для блюд в заказе
# он принимает контекст из шаблона, где используется,
# чтобы получить объект формы form (takes_context=True
# и pk объекта order_food, который сохраняет в форме
# в data-атрибуте тега <form>.

# Это т.н. inclusion-тег, т.е. тег,
# который вставляет на своё место
# в шаблоне другой шаблон.
# В отличие от обычного тега inclusion-тег
# должен вернуть контекст для своего шаблона,
# а не значение для вывода.
@register.inclusion_tag('order_food_form.html', takes_context=True)
def show_food_form(context, pk):
    return {'form': context['form'], 'pk': pk}

