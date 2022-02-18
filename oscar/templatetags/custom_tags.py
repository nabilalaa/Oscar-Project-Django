from django import template

register = template.Library()


def name_to_url(value):
    return value.replace(" ", "-")


register.filter('name_to_url', name_to_url)
