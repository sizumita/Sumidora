from django import template
register = template.Library()
from ..models import *
from django.db.models import Q, Sum
import urllib
@register.filter(name="win", is_safe=True, needs_autoescape=True)
@register.inclusion_tag('mfc.html')
def win(win):
    if int(win) == 1:
        return '勝ち'
    else:
        return '負け'

register.filter('win', win)

@register.filter(name="rank", is_safe=True, needs_autoescape=True)
@register.inclusion_tag('playerdata.html')
def rank(name):
    model = MfcBet.objects.all().values("name").annotate(price=Sum('bet'))
    place = model.values(name)

register.filter('rank', rank)

