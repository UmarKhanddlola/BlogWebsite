from django import template

register = template.Library()

@register.simple_tag
def slice(object, value):
    return object[:value]

