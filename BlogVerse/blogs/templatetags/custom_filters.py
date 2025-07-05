# custom_filters.py
from django import template

register = template.Library()

@register.filter(name = 'split_by_comma')
def split_by_comma(value):
    return value.split(',')

## Option 2

# @register.filter
# def split_by_comma(value):
#     """Splits a comma-separated string into a list"""
#     return [item.strip() for item in value.split(',')]
