from django import template

register = template.Library()

@register.filter(name='to_pence')
def to_pence(value):
    return int(value*100)

@register.filter(name='pluralise')
def pluralise(value):
    retval = ""
    if value > 1:
        retval = "s"
    return retval