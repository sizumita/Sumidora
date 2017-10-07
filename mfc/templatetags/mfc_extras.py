from django import template

register = template.Library()

@register.filter(name="win", is_safe=True, needs_autoescape=True)
def win(uuid,uuid2,name1,name2):
    if uuid == uuid2:
        return name1
    else:
        return name2

# register.filter('win', win)