from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})

@register.filter(name='sum')
def sum_values(queryset, field):
    return sum(getattr(item, field) for item in queryset)

@register.filter(name='currency')
def currency(value):
    """Converts a number to a currency format."""
    return f'R$ {value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
