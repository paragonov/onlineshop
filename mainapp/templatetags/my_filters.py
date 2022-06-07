from django.template import Library

register = Library()


@register.filter(name='range')
def times(number):
    return range(1, number+1)
