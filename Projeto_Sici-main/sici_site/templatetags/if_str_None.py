from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='if_str_None')
@stringfilter
def if_str_none(value, arg):
    if value == 'None' or value == None or value == '':
        return arg
    else:
        return value
