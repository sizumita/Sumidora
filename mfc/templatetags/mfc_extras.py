from django import template
register = template.Library()

@register.filter(name="win", is_safe=True, needs_autoescape=True)
@register.inclusion_tag('mfc.html')
def win(uuid,uuid2,name1,name2):
    if str(uuid) == str(uuid2):
        return name1
    else:
        return name2

register.filter('win', win)