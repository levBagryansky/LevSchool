from django import template

register = template.Library()


@register.filter(name="add_attrs")
def add_attrs(field, arg):
    attrs = {}
    for pair in arg.split(","):
        if "=" in pair:
            key, value = pair.split("=")
            attrs[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs)
