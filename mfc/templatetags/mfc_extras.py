from django import template
register = template.Library()
from ..models import *
from django.db.models import Q
@register.filter(name="win", is_safe=True, needs_autoescape=True)
@register.inclusion_tag('mfc.html')
def win(win):
    if int(win) == 1:
        return '勝ち'
    else:
        return '負け'

register.filter('win', win)

@register.filter(name="fight", is_safe=True, needs_autoescape=True)
@register.inclusion_tag('playerdata.html')
def fight(mfc):
    h = MfcBet.objects.filter(name=mfc).only('')
    return h


register.filter('fight', fight)

