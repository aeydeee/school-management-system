from django import template

register = template.Library()


@register.filter
def pluck(value, arg):
    """
    Extracts the values of a specific key (arg) from a list of dictionaries or objects.
    """
    if isinstance(value, list):
        return [getattr(item, arg) if hasattr(item, arg) else None for item in value]
    return []
